import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask import current_app as server

from .utils import get_url, component

def fa(className):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=className)


@component
def make_brand(**kwargs):
    return html.Header(
        className="brand",
        children=dcc.Link(
            href=get_url(""),
            children=[
                dcc.Markdown(server.config["TITLE2"]),
                html.H4("Daniel Lemchak & Ryan Shtirmer"),
                html.H4("Published online December 8th, 2019")
            ]
        ),
        **kwargs,
    )
@component
def make_header(**kwargs):
    return dbc.Navbar(
        id="header",
        className="sticky-top",
        color="success",
        dark=True,
        sticky=True,
        children=[
            dbc.Row([
                make_brand(),
                html.Ul(id=server.config["NAVBAR_CONTAINER_ID"], className="navbar-nav ml-auto")
            ])
        ],
        **kwargs,
    )


@component
def make_sidebar(**kwargs):
    return html.Nav(
        id=f"sidebar",
        className="nav navbar-dark bg-dark flex-column align-items-start",
        children=[make_brand(), html.Div(id=server.config["NAVBAR_CONTAINER_ID"])],
        **kwargs,
    )
