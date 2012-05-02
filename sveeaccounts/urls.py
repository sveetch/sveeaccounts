"""
URLconf for WithCaptchaBackend behaviors
"""
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

from registration.views import activate
from registration.views import register

from sveeaccounts.forms import LoginForm

urlpatterns = patterns('',
    url(r'^activate/complete/$',
        direct_to_template,
        {'template': 'registration/activation_complete.html'},
        name='registration_activation_complete'),
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^activate/(?P<activation_key>\w+)/$',
        activate,
        {'backend': 'sveeaccounts.backends.WithCaptchaBackend'},
        name='registration_activate'),
    url(r'^register/$',
        register,
        {'backend': 'sveeaccounts.backends.WithCaptchaBackend'},
        name='registration_register'),
    url(r'^register/complete/$',
        direct_to_template,
        {'template': 'registration/registration_complete.html'},
        name='registration_complete'),
    url(r'^register/closed/$',
        direct_to_template,
        {'template': 'registration/registration_closed.html'},
        name='registration_disallowed'),

    #(r'', include('registration.auth_urls')),
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'registration/login.html', 'authentication_form': LoginForm},
        name='auth_login'),
    url(r'^logout/$',
        auth_views.logout_then_login,
        {'login_url': '/'},
        name='auth_logout'),
)
