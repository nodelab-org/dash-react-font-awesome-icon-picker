import React, {useState} from 'react';
import { IconPicker } from 'react-fa-icon-picker'
import PropTypes from 'prop-types';

function DashIconPicker(props) {
    const [value, setValue] = useState(props.value)
    return (
        <div id={props.id} className={props.className}>
            <IconPicker
                value={value}
                hideSearch={props.hideSearch}
                containerStyles={props.containerStyles}
                buttonStyles={props.buttonStyles}
                buttonIconStyles={props.buttonIconStyles}
                pickerIconStyles={props.pickerIconStyles}
                searchInputStyles={props.searchInputStyles}
                onChange={v => {
                    setValue(v)
                    props.setProps({value:v})
                }}
            />
        </div>
    )
}
        
DashIconPicker.defaultProps = {
    value: "FaSquare"
};

DashIconPicker.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string.isRequired,

    /**
     * The value displayed in the input.
     */
    value: PropTypes.string,

    /**
     * If true, the search input is not displayed. Default is false.
     */
    hideSearch: PropTypes.bool,

    /**
     * Styles for the picker container
     */
    containerStyles: PropTypes.objectOf(PropTypes.string),

    /**
     * Styles for the picker button
     */
    buttonStyles: PropTypes.objectOf(PropTypes.string),

    /**
     * Styles for the picker button icon
     */
    buttonIconStyles: PropTypes.objectOf(PropTypes.string),

    /**
     * Styles for the icons inside of the picker
     */
    pickerIconStyles: PropTypes.objectOf(PropTypes.string),

    /**
     * Styles for the search input inside of the picker
     */
    searchInputStyles: PropTypes.objectOf(PropTypes.string),

    /**
     * CSS class for div
     */
    className: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default DashIconPicker