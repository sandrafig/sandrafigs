# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Stock Picking by Mail",
    "summary": """
	    Send stock picking by email
	""",
    "description": """
        This module allows you to send the picking order report by email
    """
    "version": "1.0",
    "author": "Sandra Figueroa Varela",
    "website": "",
    "category": "Warehouse Management",
    "license": "GPL-3",
    "depends": [
        "base",
        "stock",
        "email_template",
    ],
    "data": [
        'views/stock_picking_mail.xml',
        'views/stock_picking_view.xml',
    ],
    "installable": True
}
