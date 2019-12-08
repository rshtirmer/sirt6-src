from collections import Counter
from textwrap import dedent

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

import dash_bio as dashbio

from ..app import app

objective = [
    dcc.Markdown(
        dedent(
            """
            Given the following partial amino acid sequence, our goal was to determine:
             - The identity of our unknown protein using bioinformatics databases.
             - The structure of the gene associated with our protein.
             - The structure of the protein.
             - The function of the protein.
             - Diseases associated with the gene or protein when mutated.
            """
        )
    )
]

seq_view = dashbio.SequenceViewer(
    id='my-dashbio-sequenceviewer',
    title="SIRT6 - Partial Amino Acid Sequnce",
    search=False,
    sequence="PEIFDPPEELERKVWELARLVWQSSSVVFHTGAGISTASGIPDFRGPHGVWTMEERGLAPKFDTTFESARPTQTHMALVQLERVGLLRFLVSQNVDGLHVRSGFPRDKLAELHGNMFVEECAKCKTQYVRDTVVGTMGLKATGRLCTVAKARGLRACRGELRDTILDWEDSLPDRDLALADEASRNADLSITLGTSLQIRPSGNLPLATKRRGGRLVIVNLQPTKHDRHADLRIHGYVDEVMTRLMKHLGLEIPAWDGPRVLERALPPLPRPPTPKLEPKEESPTRINGSIPAGPKQEPCAQHNGSEPASPKRERPTSPA"
)

project_data = [
    html.H1('The Project'),
    html.Hr(),
    dcc.Markdown(
        dedent(
            """
            This website is for the Cell and Molecular Biology final lab project taught by Dr. Paramjeet S. Bagga at Ramapo College of New Jersey.

            Given a purified protein by a combination of Gel-Filtration, Ion-Exchange and Affinity chromatography from cultured HeLa cells, a partial amino acid sequence of a purified protein was able to be determined.  The goal is to determine if this protein has been cloned using protein databases and to study the structure and function of the gene and protein.
            """
        )
    ),
]

rows = html.Div(
    [
        dbc.Row(
            dbc.Col(project_data)
        ),
        html.H1('Objective'),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(objective),
                dbc.Col(seq_view),
            ]
        ),
    ]
)


jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                rows
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
