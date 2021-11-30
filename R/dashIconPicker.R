# AUTO GENERATED FILE - DO NOT EDIT

dashIconPicker <- function(id=NULL, value=NULL, hideSearch=NULL, containerStyles=NULL, buttonStyles=NULL, buttonIconStyles=NULL, pickerIconStyles=NULL, searchInputStyles=NULL, className=NULL) {
    
    props <- list(id=id, value=value, hideSearch=hideSearch, containerStyles=containerStyles, buttonStyles=buttonStyles, buttonIconStyles=buttonIconStyles, pickerIconStyles=pickerIconStyles, searchInputStyles=searchInputStyles, className=className)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashIconPicker',
        namespace = 'dash_react_font_awesome_icon_picker',
        propNames = c('id', 'value', 'hideSearch', 'containerStyles', 'buttonStyles', 'buttonIconStyles', 'pickerIconStyles', 'searchInputStyles', 'className'),
        package = 'dashReactFontAwesomeIconPicker'
        )

    structure(component, class = c('dash_component', 'list'))
}
