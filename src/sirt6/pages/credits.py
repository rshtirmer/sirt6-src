import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app

markdown = dcc.Markdown('''
# Contributions
___
Ryan Shtirmer:

* Ryan focused on information in regards to the gene.  This included all gene topics given as well as the discussion involving the gene. Ryan helped with the design and format of the website as well as tools and methods associated with the project.  The contributions for the project as a whole were 50/50.

Daniel Lemchak:

* Daniel focused on information in regards to the protein.  This involved both protein structure and function.  Daniel also worked on mutations and diseases associated with the protein/gene as well as the discussion and conclusions associated with these topics.  He also made the background and the homepage.  Once again, the contributions for the project as a whole were 50/50.

Each person formatted their own references in the references page that contributed to the findings discussed on this website.


'''
)




jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                markdown
            ],
            fluid=False,
        )
    ],
    fluid=False,
)


layout = html.Div(
    [
        jumbotron
    ]
)
