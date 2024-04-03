import frappe

@frappe.whitelist()
def get_user_info():
		
		data = frappe.db.get_list('User', fields = ["full_name", "department", "designation"], filters={'name': ['=', frappe.session.user]}, as_list=True, ignore_permissions = True)
		full_name = data[0][0]
		department = data[0][1]
		designation = data[0][2]
		metadata = frappe.get_doc('Academic Year and Semester')
		ay = metadata.academic_year
		sem = metadata.semester
		reviewer_info = frappe.get_doc('Department', data[0][1])
		reviewer = reviewer_info.reviewer
		return [full_name, department, designation, ay, sem, reviewer]
