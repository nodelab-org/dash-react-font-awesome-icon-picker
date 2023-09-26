# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashIconPicker(Component):
    """A DashIconPicker component.


Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- buttonIconStyles (dict with strings as keys and values of type string; optional):
    Styles for the picker button icon.

- buttonStyles (dict with strings as keys and values of type string; optional):
    Styles for the picker button.

- className (string; optional):
    CSS class for div.

- containerStyles (dict with strings as keys and values of type string; optional):
    Styles for the picker container.

- hideSearch (boolean; optional):
    If True, the search input is not displayed. Default is False.

- pickerIconStyles (dict with strings as keys and values of type string; optional):
    Styles for the icons inside of the picker.

- searchInputStyles (dict with strings as keys and values of type string; optional):
    Styles for the search input inside of the picker.

- value (string; default "FaSquare"):
    The value displayed in the input."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_react_font_awesome_icon_picker'
    _type = 'DashIconPicker'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, value=Component.UNDEFINED, hideSearch=Component.UNDEFINED, containerStyles=Component.UNDEFINED, buttonStyles=Component.UNDEFINED, buttonIconStyles=Component.UNDEFINED, pickerIconStyles=Component.UNDEFINED, searchInputStyles=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'buttonIconStyles', 'buttonStyles', 'className', 'containerStyles', 'hideSearch', 'pickerIconStyles', 'searchInputStyles', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'buttonIconStyles', 'buttonStyles', 'className', 'containerStyles', 'hideSearch', 'pickerIconStyles', 'searchInputStyles', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashIconPicker, self).__init__(**args)
