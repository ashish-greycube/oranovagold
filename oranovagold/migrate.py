import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.desk.page.setup_wizard.setup_wizard import make_records

def after_migrate():
    custom_fields = {
        "Stock Entry Detail" : [
            dict(
                fieldname = "custom_uom_for_purity",
                fieldtype = "Link",
                label = "UOM Of Purity",
                is_custom_field = 1,
                is_system_generated_field = 0,
                insert_after = "uom",
                options = "UOM",
            ),
            dict(
                fieldname = "custom_conversion_factor_of_purity_uom",
                fieldtype = "Float",
                label = "Purity UOM Conversion Factor",
                is_custom_field = 1,
                is_system_generated_field = 0,
                insert_after = "custom_uom_for_purity",
            ),
            dict(
                fieldname = "custom_pure_qty",
                fieldtype = "Float",
                label = "Pure Qty",
                is_custom_field = 1,
                is_system_generated_field = 0,
                insert_after = "custom_conversion_factor_of_purity_uom",
            ),
        ]
    }

    print("Adding Custom Fields In SO, SI and DN.....")
    for dt, fields in custom_fields.items():
        print("*******\n %s: " % dt, [d.get("fieldname") for d in fields])
    create_custom_fields(custom_fields)