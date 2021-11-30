# AUTO GENERATED FILE - DO NOT EDIT

export iconpickeritem

"""
    iconpickeritem(;kwargs...)

An iconPickerItem component.

Keyword arguments:
- `id` (String; required): The ID used to identify this component in Dash callbacks.
- `icon` (String; required): The name of the icon to render. Example: "FaAdobe"
- `size` (Real; optional): The size of the icon
- `color` (String; optional): The color of the icon. Default: "#000"
- `className` (String; optional): CSS class for div
"""
function iconpickeritem(; kwargs...)
        available_props = Symbol[:id, :icon, :size, :color, :className]
        wild_props = Symbol[]
        return Component("iconpickeritem", "iconPickerItem", "dash_react_font_awesome_icon_picker", available_props, wild_props; kwargs...)
end

