# AUTO GENERATED FILE - DO NOT EDIT

dashIconPickerItem <- function(id=NULL, icon=NULL, size=NULL, color=NULL, className=NULL) {
    
    props <- list(id=id, icon=icon, size=size, color=color, className=className)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashIconPickerItem',
        namespace = 'dash_react_font_awesome_icon_picker',
        propNames = c('id', 'icon', 'size', 'color', 'className'),
        package = 'dashReactFontAwesomeIconPicker'
        )

    structure(component, class = c('dash_component', 'list'))
}
