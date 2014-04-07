# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Icon


class IconPlugin(CMSPluginBase):
    model = Icon
    name = _("Icon")
    render_template = "cms/plugins/icon.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Optional Settings'), {
            'classes': ('collapse',),
            'fields': ('url', 'page_link', 'alt', 'float',),
        }),
    )

    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'object': instance,
            'link': link,
            'placeholder': placeholder,
            'STATIC_URL': settings.STATIC_URL,
        })
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + instance.name

plugin_pool.register_plugin(IconPlugin)
