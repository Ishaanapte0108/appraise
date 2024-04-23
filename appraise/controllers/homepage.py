import frappe
import pandas as pd
import numpy as np
import json

@frappe.whitelist()
def get_professor_info():

  # obtain metadata
  session_user = frappe.session.user
  metadata = frappe.get_doc('Academic Year and Semester')
  ay = metadata.academic_year
  sem = metadata.semester

  #get buckets and forms information
  bucket_info = frappe.db.get_list('Bucket mapping', fields = ["name", "bucket", "abbreviation", "maximum_marks_possible"], as_list=True, ignore_permissions = True)  
  bucket_df = pd.DataFrame(bucket_info, columns=["form_name", "bucket", "abbreviation", "maximum_marks_possible"])

  #get data about user filled forms
  doc_info = frappe.db.get_list('Aggregator', fields = ["document_type", "self_appraisal_score", "approved_score", "approved"], filters={'form_owner': session_user, 'academic_year': ay, 'semester': sem}, as_list=True, ignore_permissions = True)
  agg_df = pd.DataFrame(doc_info, columns=["form_name", "self_appraisal_score", "approved_score", "approved"])
  
  #left join and subsquent operations
  merged_df = pd.merge(bucket_df, agg_df, left_on="form_name", right_on="form_name", how='left')
  merged_df = merged_df.sort_values(by='bucket')
  # Convert specified columns to float
  merged_df['approved'] = merged_df['approved'].astype(float)
  merged_df['approved_score'] = merged_df['approved_score'].astype(float)
  merged_df['self_appraisal_score'] = merged_df['self_appraisal_score'].astype(float)
  merged_df['maximum_marks_possible'] = merged_df['maximum_marks_possible'].astype(float)
  merged_df = merged_df.replace({None: np.nan})  

  max_marks_per_bucket = merged_df.groupby('bucket')['maximum_marks_possible'].sum().to_dict()
  max_forms_per_bucket = merged_df['bucket'].value_counts().to_dict()
  total_forms = merged_df.shape[0]
  total_maximum_marks = merged_df['maximum_marks_possible'].sum()  
  sas_per_bucket = merged_df.groupby('bucket')['self_appraisal_score'].sum().to_dict()
  as_per_bucket = merged_df.groupby('bucket')['approved_score'].sum().to_dict()
  forms_submitted_per_bucket = merged_df.groupby('bucket')['self_appraisal_score'].count().to_dict()
  forms_approved_per_bucket = merged_df.groupby('bucket')['approved'].sum().to_dict()
  forms_pending_submission = {}
  try:
      for key in max_forms_per_bucket:
          forms_pending_submission[key] = max_forms_per_bucket[key] - forms_submitted_per_bucket[key]
  except Exception as e:
      for key in max_forms_per_bucket:
          forms_pending_submission[key] = None
  total_forms_submitted = int(merged_df['self_appraisal_score'].count())
  total_forms_approved = merged_df['approved'].sum()
  cumulative_approved_score = merged_df['approved_score'].sum()
  cumulative_self_appraisal_score = merged_df['self_appraisal_score'].sum()
  unique_buckets = merged_df['bucket'].unique().tolist()


  data = {
    "meta_data": {"ay": ay, "sem": sem},
    "max_marks_per_bucket": max_marks_per_bucket,
    "max_forms_per_bucket": max_forms_per_bucket,
    "total_forms": total_forms,
    "total_maximum_marks": total_maximum_marks,
    "sas_per_bucket": sas_per_bucket,
    "as_per_bucket": as_per_bucket,
    "forms_submitted_per_bucket": forms_submitted_per_bucket,
    "forms_approved_per_bucket": forms_approved_per_bucket,
    "forms_pending_submission": forms_pending_submission,
    "total_forms_submitted": total_forms_submitted,
    "total_forms_approved": total_forms_approved,
    "total_forms_pending_submission": total_forms - total_forms_submitted,
    "cumulative_approved_score": cumulative_approved_score,
    "cumulative_self_appraisal_score": cumulative_self_appraisal_score,
    "unique_buckets": unique_buckets
  } 

  return data