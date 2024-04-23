import re
import frappe
import pandas as pd
import numpy as np
import json

@frappe.whitelist()
def get_forms(bucket):

    # get buckets and forms information
    bucket_info = frappe.db.get_list('Bucket mapping', fields=["name", "bucket", "abbreviation"], filters={"bucket": bucket}, as_list=True, ignore_permissions=True)

    bucket_df = pd.DataFrame(bucket_info, columns=["form_name", "bucket", "abbreviation"])
    bucket_df['title'] = bucket_df['bucket'] + ' ' + bucket_df['abbreviation']
    bucket_df.drop(columns=['bucket', 'abbreviation'], inplace=True)

    # Extract 'title' column as a list
    title_list = bucket_df['title'].tolist()

    # Define a regex pattern to extract numeric values
    pattern = r'\d+\.\d+|\d+'

    # Extract numeric values from each element in the list
    nums_list = []
    for title in title_list:
        nums = re.findall(pattern, title)
        nums_list.extend(nums)
    
    # Convert the extracted numeric values to floats
    nums_list = [float(num) for num in nums_list]
    
    # Add nums_list as a new column to merged_df
    bucket_df['nums_list'] = nums_list
    
    # Sort merged_df based on the 'nums_list' column in ascending order
    bucket_df.sort_values(by='nums_list', inplace=True)

    bucket_df.drop(columns=['nums_list'], inplace=True)    
    
    df_data = bucket_df.to_dict(orient='records')
    doc_list = []
    for row in df_data:
        doc_dict = {
            "name": row['form_name'],
            "number": row['title'],
            "urlEnd": "/app/" + row['form_name'].replace(" ", "-").lower()
        }
        doc_list.append(doc_dict)
    
    return doc_list
    


@frappe.whitelist()
def get_progress(value, bucket):

    # obtain metadata
    session_user = frappe.session.user
    # session_user = "prakash.parmar@appraisepro.com"
    metadata = frappe.get_doc('Academic Year and Semester')
    ay = metadata.academic_year
    sem = metadata.semester

    # get buckets and forms information
    bucket_info = frappe.db.get_list('Bucket mapping', fields=["name", "bucket", "abbreviation", "maximum_marks_possible"], filters={"bucket": bucket}, as_list=True, ignore_permissions=True)

    bucket_df = pd.DataFrame(bucket_info, columns=["form_name", "bucket", "abbreviation", "maximum_marks_possible"])
    bucket_df['title'] = bucket_df['bucket'] + ' ' + bucket_df['abbreviation']
    bucket_df.drop(columns=['bucket', 'abbreviation'], inplace=True)

    # get data about user filled forms
    doc_info = frappe.db.get_list('Aggregator', fields=["document_type", "self_appraisal_score", "approved_score", "approved"], filters={'form_owner': session_user, 'academic_year': ay, 'semester': sem}, as_list=True, ignore_permissions=True)
    agg_df = pd.DataFrame(doc_info, columns=["form_name", "self_appraisal_score", "approved_score", "approved"])

    # left join and subsequent operations
    merged_df = pd.merge(bucket_df, agg_df, left_on="form_name", right_on="form_name", how='left')

    # Extract 'title' column as a list
    title_list = merged_df['title'].tolist()

    # Define a regex pattern to extract numeric values
    pattern = r'\d+\.\d+|\d+'

    # Extract numeric values from each element in the list
    nums_list = []
    for title in title_list:
        nums = re.findall(pattern, title)
        nums_list.extend(nums)
    
    # Convert the extracted numeric values to floats
    nums_list = [float(num) for num in nums_list]
    
    # Add nums_list as a new column to merged_df
    merged_df['nums_list'] = nums_list
    
    # Sort merged_df based on the 'nums_list' column in ascending order
    merged_df.sort_values(by='nums_list', inplace=True)

    merged_df.drop(columns=['nums_list'], inplace=True)
    # print(merged_df)
    submitted_df = merged_df[merged_df['self_appraisal_score'].notna()]
    # print(submitted_df)
    populate_df = merged_df[merged_df['self_appraisal_score'].isna()]
    # print(populate_df)
    approved_df = merged_df[merged_df['approved'] == 1]
    # print(approved_df)

    
    document_types = {}

    # Define a list of DataFrames and corresponding keys
    dataframes = [populate_df,submitted_df, approved_df]
    keys = ["Populate", "Submitted", "Approved"]

    # Iterate over the DataFrames and keys simultaneously
    for df, key in zip(dataframes, keys):
        if not df.empty:
            df_data = df.to_dict(orient='records')
            doc_list = []
            for row in df_data:
                doc_dict = {
                    "name": row['form_name'],
                    "number": row['title'],
                    "urlEnd": "/app/" + row['form_name'].replace(" ", "-").lower()
                }
                doc_list.append(doc_dict)
            document_types[key] = doc_list
        else:
            document_types[key] = []

    # print(document_types)
    return document_types[value]
    