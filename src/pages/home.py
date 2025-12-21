import dash
import pandas as pd
import numpy as np
import plotly.express as px
from dash import html, dcc, Input, Output, callback

dash.register_page(__name__, path="/")

df = pd.read_csv("data/cleaned/DS_ETAT_CIVIL_NAIS_COMMUNES.csv")

def layout():
    return html.Div([
        html.H2("Distribution des valeurs par commune"),
        dcc.Dropdown(
            id="year-dropdown",
            options=[{"label": year, "value": year} for year in reversed(df.columns[2:])],
            value=df.columns[-1],
            clearable=False,
        ),
        dcc.Graph(id="histogramme"),
        dcc.RangeSlider(
            id="value-slider",
            min=df[df.columns[-1]].min(),
            max=df[df.columns[-1]].max(),
            value=[df[df.columns[-1]].min(), df[df.columns[-1]].max()],
            tooltip={"placement": "bottom", "always_visible": True}
        )
    ])

@callback(
    Output(component_id="histogramme", component_property="figure"),
    [Input(component_id="year-dropdown", component_property="value"),
     Input(component_id="value-slider", component_property="value")]
)
def update_histogramme(selected_year, selected_range):
    values = df[selected_year].where((df[selected_year] >= selected_range[0]) & (df[selected_year] <= selected_range[1]))
    fig = px.histogram(
        values,
        title="Distribution des valeurs en " + selected_year
    )

    fig.update_layout(
        xaxis_title="Valeur",
        yaxis_title="Nombre de communes"
    )

    return fig
