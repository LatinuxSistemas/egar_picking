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

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.depends("move_lines")
    def _compute_kg_coil_total(self):
        for picking in self:
            kg_total = 0
            coil_total = 0
            for line in picking.move_lines:
                coil_total += line.coil_qty
                if line.product_uom and line.product_uom.name == 'kg':
                    kg_total += line.product_uom_qty

            picking.kg_total = kg_total
            picking.coil_total = coil_total

    package_qty = fields.Float(string='Package Quantity',
                               digits_compute=dp.get_precision('Product Unit of Measure'))
    insurance_price = fields.Float(string='Insurance Price',
                                   digits_compute=dp.get_precision('Product Price'))
    kg_total = fields.Float(string='Kg. Total', compute="_compute_kg_coil_total", store=True,
                            digits_compute=dp.get_precision('Product Unit of Measure'))
    coil_total = fields.Float(string='Coil Total', compute="_compute_kg_coil_total", store=True,
                              digits_compute=dp.get_precision('Product Unit of Measure'))


class StockMove(models.Model):
    _inherit = 'stock.move'

    coil_qty = fields.Float(string='Coil Quantity',
                            digits_compute=dp.get_precision('Product Unit of Measure'))
