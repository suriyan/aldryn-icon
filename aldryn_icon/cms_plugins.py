# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Icon
from .forms import IconPluginForm


class IconPlugin(CMSPluginBase):
    model = Icon
    name = _("Icon")
    render_template = False
    form = IconPluginForm
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('style', 'name',)
        }),
        (_('Optional Settings'), {
            'classes': ('collapse',),
            'fields': (
                'url', 'page_link',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        self.render_template = 'aldryn_icon/plugins/%s/icon.html' % instance.style
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
        })
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + "aldryn_icon/icons/icon.gif"

plugin_pool.register_plugin(IconPlugin)
