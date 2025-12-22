import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True, pages_folder="src/pages")

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(children=page['name'],
                     href=page["relative_path"],
                     style={}),
        ) for page in dash.page_registry.values()
    ],
    style={"display": "flex", "gap":"32px"}),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)