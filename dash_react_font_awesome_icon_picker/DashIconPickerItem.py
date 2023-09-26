# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashIconPickerItem(Component):
    """A DashIconPickerItem component.


Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    CSS class for div.

- color (string; default "#000"):
    The color of the icon. Default: \"#000\".

- icon (string; required):
    The name of the icon to render. Example: \"FaAdobe\".

- size (number; default 24):
    The size of the icon."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_react_font_awesome_icon_picker'
    _type = 'DashIconPickerItem'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, icon=Component.REQUIRED, size=Component.UNDEFINED, color=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'color', 'icon', 'size']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'color', 'icon', 'size']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'icon']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashIconPickerItem, self).__init__(**args)
