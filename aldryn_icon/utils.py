# -*- coding: utf-8 -*-

from django.conf import settings


def get_additional_styles():
    """
    Get additional style choices from settings
    """
    choices = []
    raw = getattr(settings, 'ICON_STYLES', False)
    if raw:
        if isinstance(raw, basestring):
            raw = raw.split(',')
        for choice in raw:
            clean = choice.strip()
            choices.append((clean.lower(), clean.title()))
    return choices


def get_additional_names():
    """
    Get additional icon name choices from settings
    """
    choices = []
    raw = getattr(settings, 'ICON_NAMES', False)
    if raw:
        if isinstance(raw, basestring):
            raw = raw.split(',')
        for choice in raw:
            clean = choice.strip()
            choices.append((clean.lower(), clean.title()))
    return choices
