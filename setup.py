from setuptools import setup, find_packages

setup(
    name='sveeaccounts',
    version=__import__('sveeaccounts').__version__,
    description=__import__('sveeaccounts').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='sveetch@gmail.com',
    url='http://pypi.python.org/pypi/sveeaccounts',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'autobreadcrumbs',
        'django-registration>=0.8',
        'django-simple-captcha>=0.3.4',
        'django-braces>=0.2.1',
    ],
    include_package_data=True,
    zip_safe=False
)