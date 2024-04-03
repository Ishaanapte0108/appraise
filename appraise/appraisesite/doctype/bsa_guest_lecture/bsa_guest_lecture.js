let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "BSA guest lecture");
eval(modifiedString);
