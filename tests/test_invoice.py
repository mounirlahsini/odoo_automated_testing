# -*- coding: utf-8 -*-
 
from odoo.tests import common
 
class Test_invoice(common.TransactionCase):
    def test_create_data(self):
        # Add record in test module
        Module_invoicing = self.env['odoo_automated_testing.odoo_automated_testing'].create({'name': 'Invoicing'})

        # Add a test customer to the invoice
        test_invoice_customer = self.env['res.partner'].create({'name': 'ExampleCustomer'})

        # Add a test product to the invoice
        category = self.env['product.category'].search([('name', '=', 'All')])
        test_invoice_product = self.env['product.product'].create({'name': 'ExampleProduct','type': 'consu','categ_id': category.id,'lst_price': 50})

        # Create a new invoice with the test
        test_invoice = self.env['account.invoice'].create({'name': 'Testinvoice', 'partner_id': test_invoice_customer.id, 'product_id': test_invoice_product.id})
 
        # Check if the invoice name, the customer name and product name match
        test01 = self.assertEqual(test_invoice_customer.name, 'ExampleCustomer')
        Module_invoicing.write({'test01': 'Create Customer:' + test01})
        test02 = self.assertEqual(test_invoice_product.name, 'ExampleProduct')
        Module_invoicing.write({'test02': 'Create Product:' + test02})
        test03 = self.assertEqual(test_invoice.name, 'Testinvoice')
        Module_invoicing.write({'test03': 'Create Invoice:' + test03})

        # Check if the invoice untaxed amount, tax and total match
        test04 = self.assertEqual(test_invoice.amount_untaxed, 50)
        Module_invoicing.write({'test04': 'Untaxed Amount Correct:' + test04})
        test05 = self.assertEqual(test_invoice.amount_tax, 11)
        Module_invoicing.write({'test05': 'Tax Correct:' + test05})
        test06 = self.assertEqual(test_invoice.amount_total, 61)
        Module_invoicing.write({'test06': 'Total Correct:' + test06})

        # Check if the customer and product added in the invoice are in fact the correct ids
        test07 = self.assertEqual(test_invoice_customer.id, test_invoice.partner_id)
        Module_invoicing.write({'test07': 'Right Customer in Invoice:' + test07})
        test08 = self.assertEqual(test_invoice_product.id, test_invoice.product_id)
        Module_invoicing.write({'test08': 'Right Product in Invoice:' + test08})

        # Trasnsfer test result to the table test module field results
        Module_invoicing.write({'result': 'The test was succesfull!'})