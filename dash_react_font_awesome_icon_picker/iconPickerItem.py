# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class iconPickerItem(Component):
    """An iconPickerItem component.


Keyword arguments:
- id (string; required): The ID used to identify this component in Dash callbacks.
- icon (string; required): The name of the icon to render. Example: "FaAdobe"
- size (number; default 24): The size of the icon
- color (string; default "#000"): The color of the icon. Default: "#000"
- className (string; optional): CSS class for div"""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, icon=Component.REQUIRED, size=Component.UNDEFINED, color=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'icon', 'size', 'color', 'className']
        self._type = 'iconPickerItem'
        self._namespace = 'dash_react_font_awesome_icon_picker'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'icon', 'size', 'color', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id', 'icon']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(iconPickerItem, self).__init__(**args)
