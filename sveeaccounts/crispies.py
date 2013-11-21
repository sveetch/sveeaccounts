# -*- coding: utf-8 -*-
"""
Stuff for form helpers with ``crispy_forms``

``crispy_forms`` import and usage is optionnal and no exception should be raised if 
you don't have installed it.
"""
import warnings

from django import forms
from django.conf import settings
from django.utils.importlib import import_module
from django.utils.translation import ugettext

def get_form_helper(helper_path, default=None):
    """
    Get the crispy_forms Helper from the given Python path
    
    @helper_path is a string containing a Python path to the wanted helper, @default is 
    a callable used as the default layout if the @helper_path import fails. @default 
    could be None if you don't want a default layout (and use the automated one 
    from crispy_forms).
    
    You should only use the None value for @default if you don't plan to use crispy_forms.
    
    Return a callable or None
    """
    if helper_path is None:
        return default
    
    dot = helper_path.rindex('.')
    module_name = helper_path[:dot]
    class_name = helper_path[dot + 1:]
    try:
        _class = getattr(import_module(module_name), class_name)
        return _class
    except (ImportError, AttributeError):
        warnings.warn('%s cannot be imported' % helper_path,
                      RuntimeWarning)
    return default

try:
    from crispy_forms.helper import FormHelper
    from crispy_forms.layout import Layout, Fieldset, Div, Submit
    from crispy_forms.bootstrap import FormActions
except ImportError:
    def default_helper():
        return None
    def UserProfileBaseHelper():
        return None
else:
    def default_helper(form_tag=True):
        helper = FormHelper()
        helper.form_action = '.'
        helper.form_tag = form_tag
        helper.form_style = 'inline'
        helper.add_input(Submit('submit', ugettext('Submit')))
        return helper
