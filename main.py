"""
Plotly Dash based LIBRA dashboard
"""
from dash import Dash, html
from dash_bootstrap_components import themes
from src.components.layout import create_layout

def main():
    app = Dash(external_stylesheets=[themes.SPACELAB])
    app.title = "LIBRA Dashboard (based on LIBRA v2.2)"
    app.layout = create_layout(app)
    app.run_server(debug=True)

if __name__=="__main__":
    main()