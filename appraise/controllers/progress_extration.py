import re
import frappe
import pandas as pd
import numpy as np
import json

@frappe.whitelist()
def get_progress(buttonValue, bucket):

    # obtain metadata
    session_user = frappe.session.user
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
    
    nums_list = [float(num) for num in nums_list]
    # returning the list or using it further in your logic
    return nums_list
