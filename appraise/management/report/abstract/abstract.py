# Copyright (c) 2024, appraiseSite and contributors
# For license information, please see license.txt
import frappe
import pandas as pd
from frappe.utils import today
import numpy as np


def execute(filters=None):
    # filters
    academic_year = filters.get('academic_year', "")
    semester = filters.get('semester', "")
    department = filters.get('department', '')
    faculty_designation = filters.get('designation', "")
    bucket = filters.get('bucket', "")
    
    # bucket_list
    bucket_info = frappe.db.get_list('Bucket mapping',filters = {'bucket':['like', f'%{bucket}%']}, fields=["name", "bucket", "abbreviation", "maximum_marks_possible"], as_list=True, ignore_permissions=True)
    bucket_df = pd.DataFrame(bucket_info, columns=["form_name", "bucket", "abbreviation", "maximum_marks_possible"])
    
    custom_order = {
        'AI': 0,
        'SD': 1,
        'AB': 2,
        'RB': 3,
        'CB': 4,
        'PDB': 5}
    
    bucket_df['abbr_prefix'] = bucket_df['abbreviation'].str.extract(r'([A-Za-z]+)')
    bucket_df['abbr_suffix'] = bucket_df['abbreviation'].str.extract(r'([0-9.]+)').astype(float)
    
    bucket_df['abbr_prefix_order'] = bucket_df['abbr_prefix'].map(custom_order)
    
    sorted_df = bucket_df.sort_values(by=['abbr_prefix_order', 'abbr_suffix'])
    
    if faculty_designation == 'Professor':
        filters_user = {'department': ['like', f'%{department}%'], 'designation': faculty_designation}
    else:
        filters_user = {'department': ['like', f'%{department}%'], 'designation': ['like', f'%{faculty_designation}%']}
    
    user_info = frappe.db.get_list('User', filters=filters_user,fields=["full_name", "department", "designation", "email"], as_list=True, ignore_permissions=True)    
    reviewer_names = frappe.db.get_list('Department', 'reviewer', as_list = True)

    user_info = [i for i in user_info if all(i[3] != j[0] for j in reviewer_names)]
    
    user_info = [tuple(i[:-1]) for i in user_info]

    user_df = pd.DataFrame(user_info, columns=["full_name", "department", "designation"])
    
    unique_form_names = sorted_df['form_name'].unique()
    
    # Add new columns to user_df based on unique form_name values
    for form_name in unique_form_names:
        user_df[form_name] = None

    sql = """SELECT full_name, academic_year, semester, document_type, department, designation, approved, self_appraisal_score FROM tabAggregator
            WHERE academic_year like '%{ay}%' AND semester like '%{sem}%' AND bucket like '%{buk}%' 
            AND department like '%{dept}%' AND designation like '%{facd}%'""".format(ay=academic_year, sem=semester, buk=bucket, dept=department, facd=faculty_designation)
    data = frappe.db.sql(sql, as_list=True)
    sql_df = pd.DataFrame(data, columns=["full_name", "academic_year", "semester", "document_type", "department", "designation", "approved", "self_appraisal_score"])
    
    # Loop through each row in user_df
    for index, row in user_df.iterrows():
        full_name = row['full_name']
        # Loop through each unique form_name in bucket_df
        for form_name in bucket_df['form_name'].unique():
            # Check if the combination of full_name and form_name exists in sql_df
            matching_rows = sql_df[(sql_df['full_name'] == full_name) & (sql_df['document_type'] == form_name)]
            # If there's a match, get the self_appraisal_score and update user_df
            if not matching_rows.empty:
                self_appraisal_score = matching_rows['self_appraisal_score'].values[0]
                # Update user_df with the self_appraisal_score for the corresponding full_name and form_name
                user_df.at[index, form_name] = self_appraisal_score

    user_df = user_df.fillna("NA")
    # Delete rows with full_name "Administrator
    user_df = user_df[user_df['full_name'] != "Administrator"]
    
	# If you want to reset the index after deletion
    user_df.reset_index(drop=True, inplace=True)
    
	# Convert non-numeric values to numeric for score columns
    # Extracting score columns
    score_columns = [col for col in user_df.columns if col not in ['full_name', 'department', 'designation']]
    user_df[score_columns] = user_df[score_columns].apply(pd.to_numeric, errors='coerce')

	# Fill NA values with 0 before calculating the sum
    user_df[score_columns] = user_df[score_columns].fillna(0)

	# Add a new column 'Total_score' to user_df with the sum of scores across all score_columns
    user_df['Total_score'] = user_df[score_columns].sum(axis=1)

	# If you want to handle cases where all scores are NA and set the total score to 0, you can use np.where
    user_df['Total_score'] = np.where(user_df[score_columns].eq(0).all(axis=1), 0, user_df['Total_score'])
    
    # Insert the Total_score column at the specified position
    user_df.insert(3, 'Total_score', user_df.pop('Total_score'))
    
    columns = [{"label": col, "fieldname": col, "fieldtype": "Data"} for col in user_df.columns]
    
	# Identify columns for which 0s should be replaced with 'NA'
    columns_to_replace_na = [col for col in user_df.columns if col not in ['full_name', 'department', 'designation']]

	# Replace all 0s with 'NA' in specified columns
    user_df[columns_to_replace_na] = user_df[columns_to_replace_na].replace(0, 'NA')
    
    # Convert the filtered DataFrame to a list of lists
    data = [list(row) for row in user_df.itertuples(index=False, name=None)]
    
    return columns, data