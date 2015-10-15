# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2015 Latinux S.A. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Picking extension for E.G.A.R.',
    'description': """
        * Extend picking to add coil info and total kilos.
        * Also add a custom report header layout.
    """,
    'author': 'Latinux S.A.',
    'website': 'http://www.latinux.com.ar/',
    'depends': ['stock'],
    'init_xml': [],
    'data': [
        'views/stock_picking_view.xml',
        'views/layouts.xml',
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
