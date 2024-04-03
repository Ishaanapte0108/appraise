let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", 'Institute Level Academic Activities Organized');
eval(modifiedString);
