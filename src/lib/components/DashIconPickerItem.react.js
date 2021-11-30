import React from 'react';
import { IconPickerItem } from 'react-fa-icon-picker'
import PropTypes from 'prop-types';

function DashIconPickerItem(props) {
    return (
        <div id={props.id} class={props.className}>
            <IconPickerItem
                icon={props.icon}
                size={props.size}
                color={props.color}
                onChange={(e) => {
                    props.setProps({icon:e.target.icon})
                    props.setProps({size:e.target.size})
                    props.setProps({color:e.target.color})
                }}
            />
        </div>
    )
}
        
DashIconPickerItem.defaultProps = {
    size: 24,
    color: "#000"
};

DashIconPickerItem.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string.isRequired,

    /**
     * The name of the icon to render. Example: "FaAdobe"
     */
    icon: PropTypes.string.isRequired,

    /**
     * The size of the icon
     */
    size: PropTypes.number,

    /**
     * The color of the icon. Default: "#000"
     */
    color: PropTypes.string,
    
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

export default DashIconPickerItem