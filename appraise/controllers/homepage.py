import frappe

@frappe.whitelist()

def get_info():
  
  #get user role
  session_user = frappe.session.user
  session_user = "prakash.parmar@appraisepro.com"
  
  roles = frappe.get_roles(session_user)
  if 'employee' in roles:
    role = "employee"
  elif 'reviewer' in roles:
    role = "reviewer"
  elif 'Administrator' in roles:
    roles = "Administrator"
  
  #get document information

  doc_mapping = frappe.db.get_list('Bucket mapping', fields = ["name", "bucket", "abbreviation", "maximum_marks_possible"], as_list=True, ignore_permissions = True)  
  sorted_data = sorted(doc_mapping, key=lambda x: x[1])

  max_scores = {}
  
  key = doc_mapping[0][1]
  sum = 0
  total = 0

  for tuple in sorted_data:
      total += tuple[3]

      if tuple[1] == key:
        sum+= tuple[3]
      else:
        max_scores[key] = sum
        key = tuple[1]
        sum = tuple[3]  
        
  max_scores[key]=sum
  max_scores['cumulative'] = total
  
  return max_scores