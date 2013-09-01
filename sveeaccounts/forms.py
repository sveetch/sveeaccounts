# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext

from registration.forms import RegistrationFormUniqueEmail

from captcha.fields import CaptchaField

from sveeaccounts.crispies import get_form_helper, default_helper

class RegistrationWithCaptchaForm(RegistrationFormUniqueEmail):
    captcha = CaptchaField()
    
    def __init__(self, *args, **kwargs):
        helper = get_form_helper(getattr(settings, 'REGISTRATION_FORM_HELPER', None), default=default_helper)
        if helper is not None:
            self.helper = helper()
        
        super(RegistrationWithCaptchaForm, self).__init__(*args, **kwargs)


class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        helper = get_form_helper(getattr(settings, 'REGISTRATION_LOGIN_HELPER', None), default=default_helper)
        if helper is not None:
            self.helper = helper()
        
        super(LoginForm, self).__init__(*args, **kwargs)


class UserForm(forms.Form):
    """
    User form
    """
    # Bind only some fields from the user model
    first_name = forms.CharField(label=ugettext('first name'), max_length=30, required=True)
    last_name = forms.CharField(label=ugettext("last name"), max_length=30, required=True)
    email = forms.EmailField(label=ugettext("E-mail"), max_length=75, required=True)
    new_password1 = forms.CharField(label=ugettext("Password"), widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label=ugettext("Password (again)"), widget=forms.PasswordInput, required=False)
    
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        
        helper = get_form_helper(getattr(settings, 'REGISTRATION_USER_EDIT_HELPER', None), default=default_helper)
        if helper is not None:
            self.helper = helper()
        
        super(UserForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(ugettext("The two password fields didn't match."))
        return password2
    
    def save(self, *args, **kwargs):
        self.instance.first_name = self.cleaned_data["first_name"]
        self.instance.last_name = self.cleaned_data["last_name"]
        self.instance.email = self.cleaned_data["email"]
        self.instance.save()
        if self.cleaned_data.get("new_password2", None) and len(self.cleaned_data["new_password2"].strip())>0:
            self.instance.set_password(self.cleaned_data["new_password2"])
        
        return self.instance
