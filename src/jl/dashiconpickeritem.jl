# AUTO GENERATED FILE - DO NOT EDIT

export dashiconpickeritem

"""
    dashiconpickeritem(;kwargs...)

A DashIconPickerItem component.

Keyword arguments:
- `id` (String; required): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): CSS class for div
- `color` (String; optional): The color of the icon. Default: "#000"
- `icon` (String; required): The name of the icon to render. Example: "FaAdobe"
- `size` (Real; optional): The size of the icon
"""
function dashiconpickeritem(; kwargs...)
        available_props = Symbol[:id, :className, :color, :icon, :size]
        wild_props = Symbol[]
        return Component("dashiconpickeritem", "DashIconPickerItem", "dash_react_font_awesome_icon_picker", available_props, wild_props; kwargs...)
end

