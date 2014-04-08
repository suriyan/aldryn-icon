aldryn-icon
===========

Plugin that allows to define Icons in the CMS (works with djangocms-text-ckeditor).


Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install -e git+https://github.com/aldryn/aldryn-icon#egg=aldryn-icon``.
* Add ``'aldryn_icon'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate aldryn_icon``.


Usage
-----

You can define icons in your settings.py:

```
CMS_ICON_NAMES = (
    ('my-icon-1', _("my icon 1")),
    ('my-icon-2', _("my icon 2")),
)
```

Where as ``'my-icon-1'`` and ``'my-icon-2'`` are your CSS class name defined for the icons.
