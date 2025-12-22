import dash
from dash import Dash, html, dcc

def layout():
    return html.Div([
        html.H1('Dashboard des naissances en France'),
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