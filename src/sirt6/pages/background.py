import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app

markdown = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
    '''
    # The Importance of Bioinformatics
    ___
    Bioinformatics is a very important modern interdisciplinary science that incorporates the use of many computational techniques that help with framing and solving biological problems.  Bioinformatics is associated with many scientific advancements in recent years, involving gene discovery, assignment of functions to these new genes and proteins, diagnosis and treatment of diseases, new drug and vaccine design, custom drugs, and even virtual models for research and drug trials.  This builds on foundations in molecular biology, computer science, chemistry, and mathematics.[<sup>3</sup>](/references#3)

    The use of bioinformatics tools incorporate large scale biological information that holds information in order to answer questions involving proteins and genes.  These websites are all freely accessible as well, making them very useful to the scientific community.  Through the storage of this large-scale biological information, it can be properly managed and analyzed. This allows scientists to solve scientific problems, make new discoveries, and better understand human disease models in order to make new medicines for treatment.  These tools help structure tons of genomic data that becomes easily retrievable, searchable, and integrated with related data. Without the availability of these online tools, these questions would take many years of study and the information would not be structured as it is today.[<sup>3</sup>](/references#3)

    Many bioinformatics tools were used heavily in the completion of this project.  Using BLAST, we were able to first identify our protein and then use that information to identify our gene.  Databanks such as AceView allowed us to further find information pertaining to our gene.  NCBI and UniProt allowed us to find information that helped with determining the structure and function of our protein.  Other bioinformatics databanks such as OMIM were used to determine mutations and diseases associated with our gene/protein.  The use of all these databanks allowed us to discover and study our gene and protein structure and function as well as find further information that was necessary for this project.

    The significance of this project is shown by the incorporation of these bioinformatics tools in a revolutionizing society.  As previously mentioned, we were able to take just a partial amino acid sequence and determine the protein structure, protein function, gene, as well as many mutations and diseases associated with it.  Without the use of these readily available online databanks, this information would not be easily obtained.  The study of this information and the use of bioinformatics tools allows scientists to make further discoveries and analyze information, that would normally take years of research, in a matter of minutes.  This truly does revolutionize scientific advancement.

    '''
])




jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                markdown,
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
