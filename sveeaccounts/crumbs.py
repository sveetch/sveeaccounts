# -*- coding: utf-8 -*-
"""
Application Crumbs
"""
from autobreadcrumbs import site
from django.utils.translation import ugettext_lazy

site.update({
    'registration_activation_complete': ugettext_lazy('Registration activation success'),
    'registration_activate': ugettext_lazy('Registration activation fail'),
    'registration_register': ugettext_lazy('Register'),
    'registration_complete': ugettext_lazy('Registration complete'),
    'registration_disallowed': ugettext_lazy('Registration disallowed'),
    'auth_login': ugettext_lazy('Login'),
})
