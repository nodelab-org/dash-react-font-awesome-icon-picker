# AUTO GENERATED FILE - DO NOT EDIT

dashIconPickerItem <- function(id=NULL, className=NULL, color=NULL, icon=NULL, size=NULL) {
    
    props <- list(id=id, className=className, color=color, icon=icon, size=size)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashIconPickerItem',
        namespace = 'dash_react_font_awesome_icon_picker',
        propNames = c('id', 'className', 'color', 'icon', 'size'),
        package = 'dashReactFontAwesomeIconPicker'
        )

    structure(component, class = c('dash_component', 'list'))
}
