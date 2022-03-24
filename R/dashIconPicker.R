# AUTO GENERATED FILE - DO NOT EDIT

dashIconPicker <- function(id=NULL, buttonIconStyles=NULL, buttonStyles=NULL, className=NULL, containerStyles=NULL, hideSearch=NULL, pickerIconStyles=NULL, searchInputStyles=NULL, value=NULL) {
    
    props <- list(id=id, buttonIconStyles=buttonIconStyles, buttonStyles=buttonStyles, className=className, containerStyles=containerStyles, hideSearch=hideSearch, pickerIconStyles=pickerIconStyles, searchInputStyles=searchInputStyles, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashIconPicker',
        namespace = 'dash_react_font_awesome_icon_picker',
        propNames = c('id', 'buttonIconStyles', 'buttonStyles', 'className', 'containerStyles', 'hideSearch', 'pickerIconStyles', 'searchInputStyles', 'value'),
        package = 'dashReactFontAwesomeIconPicker'
        )

    structure(component, class = c('dash_component', 'list'))
}
