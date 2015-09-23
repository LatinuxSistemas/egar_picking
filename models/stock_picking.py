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

from openerp import models, fields
from openerp.addons import decimal_precision as dp


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    coil_qty = fields.Float(string='Coil Quantity',
                            digits_compute=dp.get_precision('Product Unit of Measure'))
    package_qty = fields.Float(string='Package Quantity',
                               digits_compute=dp.get_precision('Product Unit of Measure'))
    insurance_price = fields.Float(string='Insurance Price',
                                   digits_compute=dp.get_precision('Product Price'))
