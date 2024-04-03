let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Expert for reputed committee");
eval(modifiedString);
