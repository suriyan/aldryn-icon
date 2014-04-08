# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page
from django.conf import settings

ICON_NAMES = getattr(settings, "CMS_ICON_NAMES", (
                     ('my-icon-1', _("my icon 1")),
                     ('my-icon-2', _("my icon 2")),
                     ))


class Icon(CMSPlugin):
    """
    A Icon Plugin
    """
    ICON_TAG = 'i'
    SPAN_TAG = 'span'
    DIV_TAG = 'div'

    ICON_TAG_TYPES = getattr(settings, "CMS_ICON_TAG_TYPES", (
                             (ICON_TAG, _('i')),
                             (SPAN_TAG, _('span')),
                             (DIV_TAG, _('div')),
                             ))

    name = models.CharField(_("icon name"), choices=ICON_NAMES,
                            default=ICON_NAMES[0][0], max_length=50,
                            blank=True, null=True)

    tag_type = models.CharField(
        verbose_name=_('tag Type'), max_length=50,
        choices=ICON_TAG_TYPES, default=ICON_TAG_TYPES[0][0],
        help_text=_("Use this tag type for Icon"))

    url = models.CharField(
        _("link"), max_length=255, blank=True, null=True,
        help_text=_("If present, clicking on icon will take user to link."))

    page_link = models.ForeignKey(
        Page, verbose_name=_("page"), null=True,
        limit_choices_to={'publisher_is_draft': True}, blank=True,
        help_text=_("If present, clicking on icon will take user to "
                    "specified page."))

    def __unicode__(self):
        display = self.get_name_display() or u'<empty>'
        return u"%s" % display

    def clean(self):
        if self.url and self.page_link:
            raise ValidationError(
                _("You can enter a Link or a Page, but not both."))
