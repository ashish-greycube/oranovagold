import frappe

@frappe.whitelist()
def calculate_purity_qty_on_save_of_stock_entry(self, method=None):
   if len(self.items) > 0:
      for item in self.items:
         if item.item_code:
            doc = frappe.get_doc("Item", item.item_code, "name")
            if len(doc.uoms) >= 2:
               purity_uom = doc.uoms[1].uom
               main_conversion_factor = doc.uoms[0].conversion_factor
               purity_conversion_factor = doc.uoms[1].conversion_factor
               purity_qty = (main_conversion_factor / purity_conversion_factor) * item.qty

               item.custom_uom_for_purity = purity_uom
               item.custom_conversion_factor_of_purity_uom = purity_conversion_factor
               item.custom_pure_qty = purity_qty    