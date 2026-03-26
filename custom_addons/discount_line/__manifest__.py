{
    'name': 'Account Move Line Discount',
    'version': '2.0.2',
    'sequence': '1',
    'category': 'Accounting',
    'summary': 'Accounting Reports, Asset Management and Budget, Recurring Payments, '
               'Lock Dates, Fiscal Year, Accounting Dashboard, Financial Reports, '
               'Customer Follow up Management, Bank Statement Import',
    'description': "Custom discount add account move line",
                   'license': 'LGPL-3',
'depends': [
    'base',
    'mrp',
    'account'
],
'data': [
    'views/line_discount.xml'
],
'application': True,
}
