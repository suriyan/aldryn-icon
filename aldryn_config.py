from aldryn_client import forms


class Form(forms.BaseForm):
    icon_styles = forms.CharField('List of additional icon styles (comma separated)',
                                  required=False)
    icon_names = forms.CharField('List of additional icon names (comma separated)',
                                 required=False)

    def to_settings(self, data, settings):
        settings['ICON_STYLES'] = data['icon_styles']
        settings['ICON_NAMES'] = data['icon_names']
        return settings
