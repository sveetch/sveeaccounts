"""
URLconf for WithCaptchaBackend behaviors
"""
from django.conf import settings
from django.conf.urls import *
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from registration.backends.default.views import ActivationView

from sveeaccounts.forms import LoginForm, PasswordResetForm, PasswordResetChangeForm
from sveeaccounts.views import AccountUserForm, RegistrationView

REGISTRATION_BLOCKED = getattr(settings, 'REGISTRATION_BLOCKED', False)
PASSWORD_RESET_BLOCKED = getattr(settings, 'PASSWORD_RESET_BLOCKED', False)
USER_PROFILE_BLOCKED = getattr(settings, 'USER_PROFILE_BLOCKED', False)

if REGISTRATION_BLOCKED:
    urlpatterns = patterns('',
        url(r'^activate/complete/$', TemplateView.as_view(template_name="registration/blocked.html"), name='registration_activation_complete'),
        url(r'^activate/complete/$', TemplateView.as_view(template_name="registration/blocked.html"), name='registration_activation_complete'),
        url(r'^activate/(?P<activation_key>\w+)/$', TemplateView.as_view(template_name="registration/blocked.html"), name='registration_activate'),
        url(r'^register/$', TemplateView.as_view(template_name="registration/blocked.html"), name='registration_register'),
        url(r'^register/complete/$', TemplateView.as_view(template_name="registration/blocked.html"), name='registration_complete'),
        url(r'^register/closed/$', TemplateView.as_view(template_name="registration/blocked.html"), name='registration_disallowed'),
    )
else:
    urlpatterns = patterns('',
        url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
        # Activation keys get matched by \w+ instead of the more specific
        # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
        # that way it can return a sensible "invalid key" message instead of a
        # confusing 404.
        url(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='registration_activate'),
        # Register views
        url(r'^register/$', RegistrationView.as_view(), name='registration_register'),
        url(r'^register/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
        url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed'),
    )

urlpatterns += patterns('',
    # Login/logout views
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'registration/login.html', 'authentication_form': LoginForm},
        name='auth_login'),
    url(r'^logout/$',
        auth_views.logout_then_login,
        {'login_url': '/'},
        name='auth_logout'),
)

if not USER_PROFILE_BLOCKED:
    urlpatterns += patterns('',
        # User profile form
        url(r'^profile/$',
            AccountUserForm.as_view(),
            name='auth_user_form'),
    )

if not PASSWORD_RESET_BLOCKED:
    urlpatterns += patterns('',
        # Password reset views for anonymous (copy paste from contrib.auth)
        url(r'^password/$', auth_views.password_reset, {'password_reset_form': PasswordResetForm}, name='auth_password_reset'),
        url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
        url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {'set_password_form': PasswordResetChangeForm}, name='auth_password_reset_confirm'),
        url(r'^password/reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    )
