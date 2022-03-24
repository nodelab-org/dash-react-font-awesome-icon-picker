# AUTO GENERATED FILE - DO NOT EDIT

export dashiconpicker

"""
    dashiconpicker(;kwargs...)

A DashIconPicker component.

Keyword arguments:
- `id` (String; required): The ID used to identify this component in Dash callbacks.
- `buttonIconStyles` (Dict with Strings as keys and values of type String; optional): Styles for the picker button icon
- `buttonStyles` (Dict with Strings as keys and values of type String; optional): Styles for the picker button
- `className` (String; optional): CSS class for div
- `containerStyles` (Dict with Strings as keys and values of type String; optional): Styles for the picker container
- `hideSearch` (Bool; optional): If true, the search input is not displayed. Default is false.
- `pickerIconStyles` (Dict with Strings as keys and values of type String; optional): Styles for the icons inside of the picker
- `searchInputStyles` (Dict with Strings as keys and values of type String; optional): Styles for the search input inside of the picker
- `value` (String; optional): The value displayed in the input.
"""
function dashiconpicker(; kwargs...)
        available_props = Symbol[:id, :buttonIconStyles, :buttonStyles, :className, :containerStyles, :hideSearch, :pickerIconStyles, :searchInputStyles, :value]
        wild_props = Symbol[]
        return Component("dashiconpicker", "DashIconPicker", "dash_react_font_awesome_icon_picker", available_props, wild_props; kwargs...)
end

