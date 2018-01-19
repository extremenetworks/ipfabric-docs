# -*- coding: utf-8 -*-
#
# This file contains values that differ between open-source
# to commercial (EWC) documentation. Everything that might
# change from one version to another in conf.py should be
# placed here, otherwise you WILL break the build.

master_doc = 'index'

project = u'bwc-docs'
copyright = u'2018, Extreme Networks, Inc'
author = u'Extreme Networks, Inc'

base_url = u'https://bwc-docs.brocade.com/'
htmlhelp_basename = 'bwc-doc'

man_pages = [
    ('index', 'bwc-docs', u'EWC Documentation',
     [u'Extreme Networks'], 1)
]
latex_documents = [
    (master_doc, 'bwc-docs.tex', u'bwc-docs Documentation',
     u'Extreme Networks, Inc', 'manual'),
]
texinfo_documents = [
    (master_doc, 'bwc-docs', u'EWC Documentation',
     u'Extreme Networks', 'bwc-docs', 'One line description of project.',
     'Miscellaneous'),
]

# Over-ride this in page github_url metadata
github_user = 'StackStorm'
github_repo = 'st2docs'
github_version = 'master'

theme_base_url = u'https://bwc-docs.brocade.com/'
