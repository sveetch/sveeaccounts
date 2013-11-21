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
    'auth_user_form': ugettext_lazy('Your account'),
    
    'auth_password_reset': ugettext_lazy('Password reset'),
    'auth_password_reset_confirm': ugettext_lazy('Give a new password'),
    'password_reset_done': ugettext_lazy('Email sended'),
    'password_reset_complete': ugettext_lazy('Complete'),
})
