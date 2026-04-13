import frappe

def get_previous_manufacture_data(work_order, entry_type, posting_date, posting_time):
    result = {}
    previous_entries = frappe.get_all(
        doctype = "Stock Entry",
        filters = {
            "stock_entry_type" : entry_type,
            "work_order" : work_order,
            "posting_date" : ["<=", posting_date],
            "docstatus" : 1,
        },
        fields = ["name"]
    )
    if len(previous_entries) > 0:
        total_issued_qty = 0
        total_pure_qty = 0
        for entry in previous_entries:
            doc = frappe.get_doc("Stock Entry", entry.name)
            if doc != None:
                if doc.posting_date == frappe.utils.getdate(posting_date) and frappe.utils.get_time(doc.posting_time) >= frappe.utils.get_time(posting_time):
                    continue
                for item in doc.items:
                    total_issued_qty = total_issued_qty + item.qty
                    total_pure_qty = total_pure_qty + item.custom_pure_qty
                result.update({
                    "total_issued_qty" : total_issued_qty,
                    "total_pure_qty" : total_pure_qty
                })
    return result

def get_previous_issued_and_received_manufacture_data(work_order, entry_type, posting_date, posting_time):
    result = {}
    previous_entries = frappe.db.get_all(
        doctype = "Stock Entry",
        filters = {
            "stock_entry_type" : entry_type,
            "work_order" : work_order,
            "posting_date" : ["<=", posting_date],
            "docstatus" : 1,
        },
        fields = ["name"]
    )
    if len(previous_entries) > 0:
        total_previous_issued_qty = 0
        total_previous_issued_pure_qty = 0
        total_previous_received_qty = 0
        total_previous_received_pure_qty = 0
        for entry in previous_entries:
            doc = frappe.get_doc("Stock Entry", entry.name)
            if doc != None:
                if doc.posting_date == frappe.utils.getdate(posting_date) and frappe.utils.get_time(doc.posting_time) >= frappe.utils.get_time(posting_time):
                    continue
                for item in doc.items:
                    if item.s_warehouse == None:
                        total_previous_received_qty = total_previous_received_qty + item.qty
                        total_previous_received_pure_qty = total_previous_received_pure_qty + item.custom_pure_qty
                    elif item.t_warehouse == None:
                        total_previous_issued_qty = total_previous_issued_qty + item.qty
                        total_previous_issued_pure_qty = total_previous_issued_pure_qty + item.custom_pure_qty
        result.update({
            "total_previous_issued_qty" : total_previous_issued_qty,
            "total_previous_issued_pure_qty" : total_previous_issued_pure_qty,
            "total_previous_received_qty" : total_previous_received_qty,
            "total_previous_received_pure_qty" : total_previous_received_pure_qty,
        })
    return result

def get_previous_manufacture_qty(work_order, entry_type, posting_date, posting_time):
    result = {}
    previous_entries = frappe.get_all(
        doctype = "Stock Entry",
        filters = {
            "stock_entry_type" : entry_type,
            "work_order" : work_order,
            "posting_date" : ["<=", posting_date],
            "docstatus" : 1,
        },
        fields = ["name"]
    )
    if len(previous_entries) > 0:
        total_manufacture_qty = 0
        for entry in previous_entries:
            doc = frappe.get_doc("Stock Entry", entry.name)
            if doc != None:
                if doc.posting_date == frappe.utils.getdate(posting_date) and frappe.utils.get_time(doc.posting_time) >= frappe.utils.get_time(posting_time):
                    continue
                total_manufacture_qty = total_manufacture_qty + doc.custom_manufacture_qty
                result.update({
                    "total_previous_manufacture_qty" : total_manufacture_qty
                })
    return result