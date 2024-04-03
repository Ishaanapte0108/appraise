let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Papers published in national or international journal");
eval(modifiedString);
