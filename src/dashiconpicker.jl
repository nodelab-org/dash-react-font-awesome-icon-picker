# AUTO GENERATED FILE - DO NOT EDIT

export dashiconpicker

"""
    dashiconpicker(;kwargs...)

A DashIconPicker component.

Keyword arguments:
- `id` (String; required): The ID used to identify this component in Dash callbacks.
- `value` (String; optional): The value displayed in the input.
- `hideSearch` (Bool; optional): If true, the search input is not displayed. Default is false.
- `containerStyles` (Dict with Strings as keys and values of type String; optional): Styles for the picker container
- `buttonStyles` (Dict with Strings as keys and values of type String; optional): Styles for the picker button
- `buttonIconStyles` (Dict with Strings as keys and values of type String; optional): Styles for the picker button icon
- `pickerIconStyles` (Dict with Strings as keys and values of type String; optional): Styles for the icons inside of the picker
- `searchInputStyles` (Dict with Strings as keys and values of type String; optional): Styles for the search input inside of the picker
- `className` (String; optional): CSS class for div
"""
function dashiconpicker(; kwargs...)
        available_props = Symbol[:id, :value, :hideSearch, :containerStyles, :buttonStyles, :buttonIconStyles, :pickerIconStyles, :searchInputStyles, :className]
        wild_props = Symbol[]
        return Component("dashiconpicker", "DashIconPicker", "dash_react_font_awesome_icon_picker", available_props, wild_props; kwargs...)
end

