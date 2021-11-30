import dash_react_font_awesome_icon_picker
import dash
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    style={"marginLeft":"100px"},
    children=[    
        dash_react_font_awesome_icon_picker.DashIconPicker(
            id='icon-picker',
            # value='my-value',
            hideSearch=False,

        ),
        
        html.Div(id="output")
    ]
)


@app.callback(
    Output('output', 'children'), 
    [
        Input('icon-picker', 'value')
    ])
def display_output(value):
    if value == None:
        raise PreventUpdate
    print("")
    print(f"value: {value}")
    return dash_react_font_awesome_icon_picker.DashIconPickerItem(
        id = "icon-picker-item",
        icon=value,
        size=24,
        color="#291bbc"
    ) 

if __name__ == '__main__':
    app.run_server(debug=True)
