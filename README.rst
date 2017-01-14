.. _autobreadcrumbs: http://pypi.python.org/pypi/autobreadcrumbs
.. _Django: https://www.djangoproject.com/
.. _django-braces: https://github.com/sveetch/django-braces
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _django-simple-captcha: https://github.com/mbi/django-simple-captcha
.. _django-registration: http://pypi.python.org/pypi/django-registration
.. _Pillow: https://pypi.python.org/pypi/Pillow

Introduction
============

**Sveetchies-account** is a `Django`_ application to embed all the registration stuff using
`django-registration`_ and `django-simple-captcha`_.

This is not really intended to be a generic app, so use it at your own risk.

It is an implementation of a `django-registration`_ backend with
`django-simple-captcha`_ and a ``UserProfileBase`` abstract model (and his
form, and his form view) that can be used as a base for user profiles.

Also it implements `autobreadcrumbs`_, optionnal user profile form, optionnal password
reset views, `django-crispy-forms`_ is fully supported and it contains all needed
templates to demonstrate usage.

Links
*****

* Download his `PyPi package <http://pypi.python.org/pypi/sveeaccounts>`_;
* Clone it on his `Github repository <https://github.com/sveetch/sveeaccounts>`_;

Requires
========

* `Django`_ >=1.5, <1.7;
* `autobreadcrumbs`_ <2.0.0;
* `django-braces`_ >= 1.0.0, <1.8.0;
* `django-registration`_ >= 1.0, <2.0;
* `django-simple-captcha`_ >= 0.4.1, <0.4.7;

Optionnal
*********

* `django-crispy-forms`_ >= 1.1.x;

Install
=======

    pip install sveeaccounts

Settings
********

In your *settings* file add the app to your installed apps :

::

    INSTALLED_APPS = (
        'registration',
        'captcha'
        'sveeaccounts',
        ...
    )

Then you have to mount its urls map in your webapp urls. It is recommended to add them **before** 'django.contrib.auth'.

Usage
=====

If you have installed `django-crispy-forms`_ you can specify your own form helper for registration and login forms. To do this you will have to specify the full Python path to your helper methods to use.

In your settings you can add the following variables, all of them are optionnal :

* ``REGISTRATION_FORM_HELPER`` for the registration form;
* ``REGISTRATION_LOGIN_HELPER`` for the login form;
* ``REGISTRATION_USERPROFILE_HELPER`` for the userprofile edit form;
* ``REGISTRATION_PASSWORD_RESET_HELPER`` for the password reset form (where it asks your email);
* ``REGISTRATION_PASSWORD_RESET_CHANGE_HELPER`` for the password change form (where it asks you for a new password);
* ``REGISTRATION_BLOCKED`` if ``True`` the registration form is blocked, users can't register but still can log in, default is ``False``.
* ``PASSWORD_RESET_BLOCKED`` if ``True`` the password reset views will be disabled, default is ``False``.
* ``USER_PROFILE_BLOCKED`` if ``True`` the user profile form will be disabled, default is ``False``.

The methods which these Python path point just have to return the helper you did, see the ``sveeaccounts.crispies`` code for samples.

Note that if you use `django-crispy-forms`_ you will have to override template form like ``login.html`` and ``registration.html`` to add the `django-crispy-forms`_ tags usage.

Changes
=======

Version 0.5.0
*************

* Drop uidb36 in favor of uidb64 (support for django 1.6+);
* Fixed requirements versions;


Version 0.4
***********

* Drop version support for ``Django < 1.5`` and ``django-registration < 1.0``;
* Some changes in default templates to use Foundation5 column names;
* Add a ``menu.html`` for a full sample menu in default templates;
* Update french translation catalog (PO file);
