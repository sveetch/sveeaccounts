# -*- coding: utf-8 -*-
"""
Accounts views
"""
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from braces.views import LoginRequiredMixin
from registration.backends.default.views import RegistrationView as DefaultRegistrationView

from sveeaccounts.forms import UserForm, RegistrationWithCaptchaForm

class RegistrationView(DefaultRegistrationView):
    form_class = RegistrationWithCaptchaForm

class AccountUserForm(LoginRequiredMixin, UpdateView):
    """
    The form view to edit the user account and his profile
    
    The following attributes are required and you have also to define a 
    'get_success_url' method.
    """
    template_name = "registration/user_form.html"
    form_class = UserForm
    model = User
    
    def get_object(self, *args, **kwargs):
        return self.request.user
    
    def get_success_url(self):
        return reverse('auth_user_form')
    
    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        u = self.get_object()
        return {
            'first_name': u.first_name,
            'last_name': u.last_name,
            'email': u.email,
        }

