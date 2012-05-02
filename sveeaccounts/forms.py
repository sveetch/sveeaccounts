# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext

from registration.forms import RegistrationFormUniqueEmail

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from captcha.fields import CaptchaField

class RegistrationWithCaptchaForm(RegistrationFormUniqueEmail):
    #captcha = CaptchaField(label=u"Anti", help_text=u"Veuillez entrer les quatres lettres que vous voyez dans l'image ci-dessus.")
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
