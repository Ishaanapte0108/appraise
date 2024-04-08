let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Service to community through product development");
eval(modifiedString);
