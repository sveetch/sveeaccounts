# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext

from registration.forms import RegistrationFormUniqueEmail

from captcha.fields import CaptchaField

from sveeaccounts.models import UserProfileBase
from sveeaccounts.crispies import get_form_helper, default_helper, UserProfileBaseHelper

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



class UserProfileBaseForm(forms.ModelForm):
    """
    User profile form
    """
    # Bind only some fields from the user model
    first_name = forms.CharField(label=ugettext('first name'), max_length=30, required=True)
    last_name = forms.CharField(label=ugettext("last name"), max_length=30, required=True)
    email = forms.EmailField(label=ugettext("E-mail"), max_length=75, required=True)
    new_password1 = forms.CharField(label=ugettext("Password"), widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label=ugettext("Password (again)"), widget=forms.PasswordInput, required=False)
    
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('user')
        
        helper = get_form_helper(getattr(settings, 'REGISTRATION_USERPROFILE_HELPER', None), default=UserProfileBaseHelper)
        if helper is not None:
            self.helper = helper()
        
        super(UserProfileBaseForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(ugettext("The two password fields didn't match."))
        return password2
    
    def save(self, *args, **kwargs):
        instance = super(UserProfileBaseForm, self).save(commit=True, *args, **kwargs)
        
        u = instance.user
        u.first_name = self.cleaned_data["first_name"]
        u.last_name = self.cleaned_data["last_name"]
        u.email = self.cleaned_data["email"]
        u.save()
        if self.cleaned_data.get("new_password2", None) and len(self.cleaned_data["new_password2"].strip())>0:
            u.set_password(self.cleaned_data["new_password2"])
        
        return instance
    
    class Meta:
        model = UserProfileBase
        exclude = ('user',)
