aldryn-icon
===========

Plugin that allows to define Icons in the CMS (works with djangocms-text-ckeditor).


Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`_, run ``python setup.py install``.
* Install dependency packages, run ``pip install -r requirements.txt``.
* Add ``'icons_tango'`` and ``'aldryn_icon'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py schemamigration aldryn_icon --initial`` to generate initial schema.
* Run ``manage.py migrate aldryn_icon``.


Usage
-----

There are pre-defined Icons based on icon files (32x32 pixels) from ``'django-icons-tango'`` (https://pypi.python.org/pypi/django-icons-tango/)

or you can define custom icons in your settings.py:

```
CMS_ICON_NAMES = (
    ('icons/info.png', _("info")),
    ('icons/new.png', _("new")),
    ('icons/hint.png', _("hint")),
)
```
