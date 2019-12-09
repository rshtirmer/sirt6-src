import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app

markdown1 = dcc.Markdown('''
# 3D Model of SIRT6
''')

markdown2 = markdown = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
'''
The protein shown to the left represents the SIRT6 protein isoform 1 structure.  This protein consists of a 355 amino acid structure, containing 13 alpha helices with 87 residues and 14 beta strands with 60 residues.  It has an active site at position 133 with four zinc metal binding sites at 141, 144, 166, and 177.  It also has a NAD binding site at position 258.[<sup>30</sup>](/references#30)

SIRT6 protein is shown to have a Quaternary structure with association to the RELA protein.[<sup>31</sup>](/references#31) While another research article by Kaidi et al. (2010) showed potential relation to RBBP8 associated with its quaternary structure, this information was retracted due to falsified data and will not be discussed.[<sup>30</sup>](/references#30) [<sup>18</sup>](/references#18)
''']
)

markdown3 = dcc.Markdown('''
# Functional Domain
''')

markdown4 = markdown = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
'''
According to information found on UniProt, SIRT6 has one main deacetylase sirtuin-type domain. This is a 240 amino acid sequence at position 35-274.[<sup>30</sup>](/references#30)  When in complex with NAD, this domain consists of a Rossmann fold and a small domain containing a three-stranded zinc ribbon motif.[<sup>27</sup>](/references#27)

This deacetylase sirtuin-type domain falls under the SIR2 superfamily of proteins also classified as sirtuins.  This includes silent information regulator 2 (Sir2) enzymes responsible for catalyzing NAD+ dependent protein and histone deacetylation, where the acetyl group from the lysine epsilon-amino group is transferred to the ADP-ribose within the NAD+. This produces nicotinamide and a novel metabolite O-acetyl-ADP-ribose.[<sup>27</sup>](/references#27) [<sup>36</sup>](/references#36)

Sirtuins are found in all eukaryotes as well as many archaea and prokaryotes.  These proteins have been shown to be associated with regulating gene silencing, DNA repair, metabolic enzymes, and life span.[<sup>36</sup>](/references#36)
'''])

iFrame = html.Iframe(src="https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?mmdbid=163934&width=500&height=500&showcommand=0&mobilemenu=1&showtitle=1",
            height=400,
            width=400,
            style={'border': 'none'})


jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                markdown1,
                html.Hr(),
                dbc.Row([
                    dbc.Col(
                        iFrame
                    ),
                    dbc.Col(
                        markdown2
                    )
                ]),
                html.A("Image Source: https://www.ncbi.nlm.nih.gov/Structure/pdb/5X16", href="https://www.ncbi.nlm.nih.gov/Structure/pdb/5X16"),
                markdown3,
                html.Hr(),
                markdown4,
                html.Img(src="https://i.imgur.com/9WWLj7s.png",
                        width="50%"),
                html.Br(),
                html.A("Image Source: https://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=350940", href="https://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=350940"),

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
