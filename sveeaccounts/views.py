# -*- coding: utf-8 -*-
"""
Accounts views
"""
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse

from braces.views import UserFormKwargsMixin, LoginRequiredMixin

from sveeaccounts.models import UserProfileBase
from sveeaccounts.forms import UserProfileBaseForm

class MyAccountBaseView(LoginRequiredMixin, UserFormKwargsMixin, UpdateView):
    """
    The form view to edit the user account and his profile
    
    The following attributes are required and you have also to define a 
    'get_success_url' method.
    """
    template_name = None # Required
    form_class = UserProfileBaseForm
    model = None # Required. This should be assigned with your profile model
    
    def get_object(self, *args, **kwargs):
        return self.request.user.get_profile()
    
    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        return {
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email,
        }
