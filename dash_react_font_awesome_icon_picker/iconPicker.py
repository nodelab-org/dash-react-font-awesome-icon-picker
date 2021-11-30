# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class iconPicker(Component):
    """An iconPicker component.


Keyword arguments:
- id (string; required): The ID used to identify this component in Dash callbacks.
- value (string; optional): The value displayed in the input.
- hideSearch (boolean; optional): If true, the search input is not displayed. Default is false.
- containerStyles (dict with strings as keys and values of type string; optional): Styles for the picker container
- buttonStyles (dict with strings as keys and values of type string; optional): Styles for the picker button
- buttonIconStyles (dict with strings as keys and values of type string; optional): Styles for the picker button icon
- pickerIconStyles (dict with strings as keys and values of type string; optional): Styles for the icons inside of the picker
- searchInputStyles (dict with strings as keys and values of type string; optional): Styles for the search input inside of the picker
- className (string; optional): CSS class for div"""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, value=Component.UNDEFINED, hideSearch=Component.UNDEFINED, containerStyles=Component.UNDEFINED, buttonStyles=Component.UNDEFINED, buttonIconStyles=Component.UNDEFINED, pickerIconStyles=Component.UNDEFINED, searchInputStyles=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'hideSearch', 'containerStyles', 'buttonStyles', 'buttonIconStyles', 'pickerIconStyles', 'searchInputStyles', 'className']
        self._type = 'iconPicker'
        self._namespace = 'dash_react_font_awesome_icon_picker'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'value', 'hideSearch', 'containerStyles', 'buttonStyles', 'buttonIconStyles', 'pickerIconStyles', 'searchInputStyles', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(iconPicker, self).__init__(**args)
