# -*- coding: utf-8 -*-
#
# This file contains values that differ between open-source
# to commercial (EWC) documentation. Everything that might
# change from one version to another in conf.py should be
# placed here, otherwise you WILL break the build.

master_doc = 'index'

project = u'ewc-docs'
copyright = u'2018, Extreme Networks, Inc'
author = u'Extreme Networks, Inc'

base_url = u'https://ewc-docs.extremenetworks.com/'
htmlhelp_basename = 'ewc-doc'

man_pages = [
    ('index', 'ewc-docs', u'EWC Documentation',
     [u'Extreme Networks'], 1)
]
latex_documents = [
    (master_doc, 'ewc-docs.tex', u'EWC Documentation',
     u'Extreme Networks, Inc', 'manual'),
]
texinfo_documents = [
    (master_doc, 'ewc-docs', u'EWC Documentation',
     u'Extreme Networks', 'ewc-docs', 'Extreme Workflow Composer.',
     'Miscellaneous'),
]

# Over-ride this in page github_url metadata
github_user = 'StackStorm'
github_repo = 'st2docs'
github_version = 'master'

theme_base_url = u'https://ewc-docs.extremenetworks.com/'
