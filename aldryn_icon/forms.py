from django import forms
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _
from .models import Icon

class IconPluginForm(forms.ModelForm):
    model = Icon

    def clean_style(self):
        style = self.cleaned_data.get('style')
        # Check if template for style exists:
        try:
            select_template(['aldryn_icon/plugins/%s/icon.html' % style])
        except TemplateDoesNotExist:
            raise forms.ValidationError(_('Template not found'))
        return style
