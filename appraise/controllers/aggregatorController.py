import frappe

def modify(self, dt):
    
    bucket = frappe.get_value('Bucket mapping', dt, 'bucket')
    existing_record = frappe.db.exists('Aggregator', {'name': self.name})
    
    if existing_record:
        doc = frappe.get_doc('Aggregator', self.name)
        doc.update({
            "name1": self.name,
            "document_type": dt,
            "form_owner": self.owner,
            "full_name": self.professor,
            "department": self.department,
            "designation": self.designation,
            "approved": self.approved,
            "bucket": bucket,
            "academic_year": self.academic_year,
            "semester": self.semester,
            "self_appraisal_score": self.self_appraisal_score,
            "approved_score": self.reviewer_score,
            "reviewer": self.reviewer
        })
    else:        
        doc = frappe.new_doc("Aggregator")
        doc.update({
            "name1": self.name,
            "document_type": dt,
            "form_owner": self.owner,
            "full_name": self.professor,
            "department": self.department,
            "designation": self.designation,
            "approved": self.approved,
            "bucket": bucket,
            "academic_year": self.academic_year,
            "semester": self.semester,
            "self_appraisal_score": self.self_appraisal_score,
            "approved_score": self.reviewer_score,
            "reviewer": self.reviewer
        })
    try:
        doc.save(ignore_permissions=True)
        frappe.db.commit()
    except Exception as e:
        frappe.throw(str(e))

def delete(self):
    
    roles = frappe.get_roles(frappe.session.user)
    is_admin = True if 'Administrator' in roles else False
    is_system_manager = True if 'System Manager' in roles else False
    
    if self.approved == 1 and (not is_admin or not is_system_manager):
        frappe.throw('Cannot delete document post approval')	

    try:     
        frappe.delete_doc("Aggregator", self.name, ignore_permissions=True)
        frappe.db.commit()
    except Exception as e:
        frappe.throw(str(e))
