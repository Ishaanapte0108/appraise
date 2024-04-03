let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Administrative Co-Curricular Activities");
eval(modifiedString);
