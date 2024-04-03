let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Funding generated through research projects");
eval(modifiedString);
