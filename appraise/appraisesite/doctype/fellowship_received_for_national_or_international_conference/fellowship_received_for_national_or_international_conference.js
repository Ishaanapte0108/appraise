let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Fellowship received for national or international conference");
eval(modifiedString);
