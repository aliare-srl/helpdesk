# -*- coding: utf-8 -*-
#    Copyright (C) 2007  pronexo.com  (https://www.pronexo.com)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################## # 

from . import controller


def post_install_hook_ensure_team_forms(cr, registry):
    """ Ensure that a form template is generated for each helpdesk team using website helpdesk form.
        Two use cases :
            * After manual desinstall/reinstall of the module we have to regenerate form for concerned teams.
            * When the option is selected on a team for the first time, causing the module to be installed.
              In that case, the override on write/create that invokes the form generation does not apply yet
              and the team does not get its form generated.
    """
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    teams = env['helpdesk.team'].search([('use_website_helpdesk_form', '=', True)])
    teams._ensure_submit_form_view()
