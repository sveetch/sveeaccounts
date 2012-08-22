# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext

from registration.forms import RegistrationFormUniqueEmail

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit
from crispy_forms.bootstrap import FormActions

from captcha.fields import CaptchaField

from sveeaccounts.models import UserProfileBase

class RegistrationWithCaptchaForm(RegistrationFormUniqueEmail):
    captcha = CaptchaField()
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.form_style = 'inline'
        self.helper.add_input(Submit('submit', ugettext('Continue')))
        
        super(RegistrationWithCaptchaForm, self).__init__(*args, **kwargs)

class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.form_style = 'inline'
        self.helper.form_class = 'tiny'
        self.helper.add_input(Submit('submit', ugettext('Ok')))
        
        super(LoginForm, self).__init__(*args, **kwargs)

def UserProfileBaseLayout():
    """
    Return the default layout, this must be wrapped in a function to correct 
    translations
    """
    return Layout(
        Fieldset(
            ugettext('account'),
            'new_password1',
            'new_password2',
        ),
        Fieldset(
            ugettext('identity'),
            'first_name',
            'last_name',
            'email',
            'adress',
            'town',
            'zipcode',
            'phone_number',
            'mobile_number',
        ),
    )
    
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
        
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.form_class = 'form-horizontal well'
        self.helper.form_style = 'inline'
        self.helper.layout = Layout(
            kwargs.pop('layout', UserProfileBaseLayout()),
            FormActions(
                Submit('submit', 'Submit'),
            )
        )
        
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
