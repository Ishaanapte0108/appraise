let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Developing and imparting people skills");
eval(modifiedString);
