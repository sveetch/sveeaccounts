# -*- coding: utf-8 -*-
from registration.backends.default import DefaultBackend

from sveeaccounts.forms import RegistrationWithCaptchaForm

class WithCaptchaBackend(DefaultBackend):
    def get_form_class(self, request):
        """
        Return the default form class used for user registration.
        
        """
        return RegistrationWithCaptchaForm
