import dash
from dash import html

dash.register_page(__name__, path="/birth_map")

def layout():
    return html.Div([
        html.H2("Distribution des valeurs par commune"),
        html.Iframe(
            src="/assets/map.html",
            style={"width": "100%", "height": "800px"})
    ])