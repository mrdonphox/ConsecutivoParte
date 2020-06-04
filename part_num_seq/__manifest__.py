# -*- coding: utf-8 -*-
{
    'name': 'Consecutivo de Productos',
    'summary': 'Consecutivo Alterno de Productos',
    'description': 'Crea un consecutivo alterno para los productos en un campo nuevo',
    'author': "EZ Consulting",
    'website': "http://www.dolmen360.com",
    'licence': 'APGL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/product_view.xml',
        'data/sequence.xml'
    ],
}
