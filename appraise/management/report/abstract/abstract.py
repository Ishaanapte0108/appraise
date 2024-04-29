# Copyright (c) 2024, appraiseSite and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns = [{'fieldname': 'name', 'label': 'name'},
	{'fieldname': 'full_name', 'label': 'full_name'},
	{'fieldname': 'faculty_designation', 'label': 'faculty_designation'},
	{'fieldname': 'Certification for courses allotted',
	'label': 'Certification for courses allotted'},
	{'fieldname': 'Courses taught', 'label': 'Courses taught'},
	{'fieldname': 'BSA guest lecture', 'label': 'BSA guest lecture'},
	{'fieldname': 'BSA industrial visit', 'label': 'BSA industrial visit'},
	{'fieldname': 'BSA-Co-curricular', 'label': 'BSA-Co-curricular'},
	{'fieldname': 'Laboratory Work Or Case Studies',
	'label': 'Laboratory Work Or Case Studies'},
	{'fieldname': 'Course-lab outcome attainment',
	'label': 'Course-lab outcome attainment'},
	{'fieldname': 'ME Projects', 'label': 'ME Projects'},
	{'fieldname': 'Average Student Attendance',
	'label': 'Average Student Attendance'},
	{'fieldname': 'Exam related work', 'label': 'Exam related work'},
	{'fieldname': 'BSA-Mini Prj', 'label': 'BSA-Mini Prj'},
	{'fieldname': 'Innovation in TLP', 'label': 'Innovation in TLP'},
	{'fieldname': 'Contribution in learning resources development',
	'label': 'Contribution in learning resources development'},
	{'fieldname': 'Subject head-mini project',
	'label': 'Subject head-mini project'},
	{'fieldname': 'BE Projects', 'label': 'BE Projects'},
	{'fieldname': 'PhD', 'label': 'PhD'},
	{'fieldname': 'Grades in preceding semester preview',
	'label': 'Grades in preceding semester preview'},
	{'fieldname': 'Grades in preceding semester review',
	'label': 'Grades in preceding semester review'}]

	data = [{'name': 'ninad.rao@appraisepro.awsapps.com',
  'full_name': 'Ninad Rao',
  'faculty_designation': 'Executive',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'rakesh.pathak@appraisepro.awsapps.com',
  'full_name': 'Rakesh Pathak',
  'faculty_designation': 'Executive',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'kiyara.sharma@appraisepro.awsapps.com',
  'full_name': 'Kiyara Sharma',
  'faculty_designation': 'Appraisal team',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'aniket.datar@appraisepro.awsapps.com',
  'full_name': 'Aniket Datar',
  'faculty_designation': 'Principal',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'ishita.chatterjee@appraisepro.awsapps.com',
  'full_name': 'Ishita Chatterjee',
  'faculty_designation': 'Associate Professor',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'kabir.kapoor@appraisepro.awsapps.com',
  'full_name': 'Kabir Kapoor',
  'faculty_designation': 'Assistant Professor',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'nandini.mehta@appraisepro.awsapps.com',
  'full_name': 'Nandini Mehta',
  'faculty_designation': 'Professor',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'arjun.singh@appraisepro.awsapps.com',
  'full_name': 'Arjun Singh',
  'faculty_designation': 'Associate Professor',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'riya.sharma@appraisepro.awsapps.com',
  'full_name': 'Riya Sharma',
  'faculty_designation': 'Assistant Professor',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'aarav.patel@appraisepro.awsapps.com',
  'full_name': 'Aarav Patel',
  'faculty_designation': 'Professor',
  'Certification for courses allotted': '150',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': '166',
  'Exam related work': '45',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'aditi.birla@appraisepro.awsapps.com',
  'full_name': 'Aditi Birla',
  'faculty_designation': 'Not Applicable',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'},
 {'name': 'ishaanmapte@gmail.com',
  'full_name': 'Ishaan Apte',
  'faculty_designation': 'Trustee',
  'Certification for courses allotted': 'Pending',
  'Courses taught': 'Pending',
  'BSA guest lecture': 'Pending',
  'BSA industrial visit': 'Pending',
  'BSA-Co-curricular': 'Pending',
  'Laboratory Work Or Case Studies': 'Pending',
  'Course-lab outcome attainment': 'Pending',
  'ME Projects': 'Pending',
  'Average Student Attendance': 'Pending',
  'Exam related work': 'Pending',
  'BSA-Mini Prj': 'Pending',
  'Innovation in TLP': 'Pending',
  'Contribution in learning resources development': 'Pending',
  'Subject head-mini project': 'Pending',
  'BE Projects': 'Pending',
  'PhD': 'Pending',
  'Grades in preceding semester preview': 'Pending',
  'Grades in preceding semester review': 'Pending'}]

	return columns, data

'''
import frappe
import pandas as pd
from frappe.utils import today

def execute(filters=None):

	academic_year = filters.get('academic_year', today()[0:4])
	semester = filters.get('semester', 'Odd')
	department = filters.get('department', '')
	faculty_designation = filters.get('designation', '')
	bucket = filters.get('bucket', 'bytenba')

	# sql = """SELECT p.full_name as Faculty, p.user_id as 'Employee Code', p.department as Department, p.faculty_designation as Designation, COALESCE(c.reviewer_score, "Pending") as "AI 1", COALESCE(co.reviewer_score, "Pending") as "AI 2",  COALESCE(b.reviewer_score, "Pending") as "AI 3.1"
  # FROM tabProfessors as p
  # JOIN tabCertification for courses allotted as c
  # ON p.name = c.owner
	# JOIN tabCourses taught as co
	# ON p.name = co.owner
	# JOIN tabBSA guest lecture as b
	# ON p.name = b.owner
	# WHERE p.department like '{department}'
  # AND p.faculty_designation like '{faculty_designation}'
	# AND c.academic_year = '{academic_year}'
	# AND c.semester = '{semester}'
	# AND co.academic_year = '{academic_year}'
	# AND co.semester = '{semester}'
	# AND b.academic_year = '{academic_year}'
	# AND b.semester = '{semester}'
  # """.format(department = department + "%", faculty_designation = faculty_designation + "%", academic_year = academic_year, semester = semester)

	# print(sql)

	# data = frappe.db.sql(sql, as_dict=True)

  # # Convert data to Pandas DataFrame
	# result = [dict(row) for row in data]
	# df = pd.DataFrame(result)
	# column_names = df.columns.tolist()
	

	# """SEND DATA as a report	"""
	# columns = []
	# for name in column_names:
	# 	columns.append({"fieldname": name,"label": name})
	# data_dict = df.to_dict('records')	

	# return columns, data_dict
	
	filters_faculty={'Active': ['=', '1']}
	# filters_doctype = {'module': ['=', 'bytenba']}

	data = frappe.db.get_list("Professors", fields = ['name', 'full_name', 'faculty_designation'], filters = filters_faculty)
	# doctypes = frappe.db.get_list("DocType", pluck= "name", filters = {'module': ['=', 'bytenba'], 'istable': ['!=', 1]})

	doctypes = ['Certification for courses allotted', 'Courses taught', 'BSA guest lecture','BSA industrial visit', 'BSA-Co-curricular', 		'Laboratory Work Or Case Studies', 'Course-lab outcome attainment', 'ME Projects', 'Average Student Attendance',  'Exam related work',  'BSA-Mini Prj', 'Innovation in TLP','Contribution in learning resources development', 'Subject head-mini project','BE Projects', 'PhD', 'Grades in preceding semester preview', 'Grades in preceding semester review']

	#		Excluded temporarily
	#  'Summer internships and projects'
	#  'MMS FY Projects',

	
	for i in data:
		
		for doc in doctypes:

				rs = frappe.db.get_value(doc, filters={'owner': ['=', i['name']], 'academic_year': ['=', '2024'], 'semester': ['=', 'Odd']}, fieldname='reviewer_score') or 'Pending'
				i[doc] = rs
	
	
	column_names = data[0].keys()
	columns = []
	for name in column_names:
		columns.append({"fieldname": name,"label": name})

	return columns, data'''