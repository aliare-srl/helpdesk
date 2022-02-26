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
{
    'name': 'Online Ticket Submission custom',
    'category': 'Website/Website',
    'version': '15.0.1.0',
    'sequence': 17,
    'summary': 'Qualify helpdesk queries with a website form',
    'depends': [
        'website_helpdesk','website_helpdesk_form',
    ],
    'description': """
Add default partner email value on email input. Extend Generate tickets in Helpdesk app from a form published on your website. This form can be customized thanks to the *Website Builder*.
    """,
    'data': [
        'views/helpdesk_templates.xml'
    ],
    'post_init_hook': 'post_install_hook_ensure_team_forms',
    'author': 'Pronexo',
    'license': 'AGPL-3',
    'maintainer': 'Pronexo',
    'website': 'https://www.pronexo.com',
    'application': True
}
