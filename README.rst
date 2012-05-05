.. _autobreadcrumbs: http://pypi.python.org/pypi/autobreadcrumbs
.. _Django: https://www.djangoproject.com/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _django-simple-captcha: https://github.com/mbi/django-simple-captcha
.. _django-registration: http://pypi.python.org/pypi/django-registration

Introduction
============

**Sveetchies-account** is a `Django`_ application to embed all the registration stuff using 
`django-registration`_ and `django-simple-captcha`_.

This is not really intended to be a generic app, so use it at your own risk.

Actually this is just an implementation of an inherited `django-registration`_ backend with 
`django-simple-captcha`_ usage.

Links
*****

* Download his `PyPi package <http://pypi.python.org/pypi/sveeaccounts>`_;
* Clone it on his `Github repository <https://github.com/sveetch/sveeaccounts>`_;
* Documentation and demo to come on his 
  `DjangoSveetchies page <http://sveetchies.sveetch.net/sveeaccounts/>`_.

Requires
========

* `autobreadcrumbs`_;
* `django-registration`_ >= 0.8;
* `django-simple-captcha`_ >= 0.3.4;
* `django-crispy-forms`_ >= 1.1.x;

Install
=======

Settings
********

In your *settings* file add the app to your installed apps :

::

    INSTALLED_APPS = (
        ...
        'sveeaccounts',
        ...
    )

