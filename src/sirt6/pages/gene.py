import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_bio as dashbio
import plotly.graph_objects as go
import dash_table
import pandas as pd
import os
import base64
from dash.dependencies import Input, State, Output

from ..app import app


introduction = dcc.Markdown(
    '''
        ###### **Official Name:** Sirtuin 6\n
        ###### **Official Symbol:** SIRT6\n
        ###### **Other Known Symbols:** SIR2L6, SIR2L6, and LOC51548\n
        ###### **NCBI Gene ID:** [51548](https://www.ncbi.nlm.nih.gov/gene/51548)\n

        ###### **Cytogenetic location:** 19p13.3
        ###### **Absolute genomic location:** 4174109 - 4182566
        ###### **Genome ID:** GRCh38 - Build 38.p13
    '''
)

database_intro = dcc.Markdown(
        '''
        * **Database:** [AceView](https://www.ncbi.nlm.nih.gov/IEB/Research/Acembly/av.cgi?db=human&q=SIRT6)
        * **NCBI RefSeqGene Accession #:** [NG_047153.1](https://www.ncbi.nlm.nih.gov/nuccore/1027250684)
        * **Isoform 1:**
            * ###### **AceView Variant:** A (August 2010)
            * **NCBI RefSeq Protein Accession #:** [NP_057623.2](https://www.ncbi.nlm.nih.gov/protein/NP_057623.2)
            * **NCBI RefSeq mRNA Accession #:** [NM_016539.4](https://www.ncbi.nlm.nih.gov/nuccore/NM_016539.4)
        * **Isoform 2:**
            * ###### **AceView Variant:** L (August 2010)
            * **NCBI RefSeq Protein Accession #:** [NP_001307992.1](https://www.ncbi.nlm.nih.gov/protein/NP_001307992.1)
            * **NCBI RefSeq mRNA Accession #:**  [NM_001321063.2](https://www.ncbi.nlm.nih.gov/nuccore/NM_001321063.2)
        ###### Note: All tables and diagrams were contstructed using AceView. As links to AceView variants are not possible, the above links to corresponding NCBI isoforms are provided. Please be aware that these may not match up exactly with the data found on this website.
            '''
)

gene_structure = pd.read_csv("https://raw.githubusercontent.com/rshtirmer/SIRT6_Files/master/data/genestructure.csv")#pd.read_csv("data/genestructure.csv")
mrna_structure = pd.read_csv("https://raw.githubusercontent.com/rshtirmer/SIRT6_Files/master/data/pre_mrna.csv")
variant_data = pd.read_csv("https://raw.githubusercontent.com/rshtirmer/SIRT6_Files/master/data/variants.csv")

gene_structure_table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in gene_structure.columns],
    data=gene_structure.to_dict('records'),
    style_as_list_view=True,
    style_cell={'padding': '5px',
                'textAlign': 'left'
    },
    style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'
    },
    style_table={
        'maxHeight': '500px',
        'overflowY': 'scroll'
    },
)

mrna_table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in mrna_structure.columns],
    data=mrna_structure.to_dict('records'),
    style_as_list_view=True,
    style_cell={'padding': '5px',
                'textAlign': 'left'
    },
    style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'
    },
    style_table={
        'maxHeight': '500px',
        'overflowY': 'scroll'
    },
)

variant_table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in variant_data.columns],
    data=variant_data.to_dict('records'),
    style_as_list_view=True,
    style_cell={'padding': '5px',
                'textAlign': 'left'
    },
    style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'
    },
    style_table={
        'maxHeight': '500px',
        'overflowY': 'scroll'
    },
    style_data_conditional=[
        {"if": {"row_index": 0},
            "backgroundColor": "#3D9970",
            'color': 'white'
        },
        {"if": {"row_index": 11},
            "backgroundColor": "#3D9970",
            'color': 'white'
        }
    ]
)


gene_structure = [
    html.H2('Table 1: SIRT6 Gene Structure: \n'),
]


mrna_structure = [
    html.H2('Table 3: SIRT6 pre-mRNA Composite: '),
]

variant_info = [
    html.H2('Table 2: SIRT6 pre-mRNA Variants: '),
]

fig = go.Figure()

## Isoform L
five_utr = 7
three_utr = 789
exons_introns = [66, 1564,
                 128, 3643,
                 60, 1141,
                 96, 81,
                 81, 568,
                 84, 81,
                 49]

total = five_utr

fig.add_trace(go.Bar(
    y=['Isoform L'],
    x=[50],
    text=f"1-{total}",
    textposition='auto',
    name='5\' UTR',
    orientation='h',
    showlegend=False,
    marker=dict(
        color='lightpink',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))


for i,e in enumerate(exons_introns):
  start = total + 1
  total = total + e
  text = total
  show_legend = False if i > 1 else True

  if i%2 == 0:
    is_type = "CDS"
    color = "lightseagreen"
    distance = e
  else:
    is_type = "Intron"
    color = "lightsalmon"
    distance = e/10 if e/10 > 50 else 50

  fig.add_trace(go.Bar(
      y=['Isoform L'],
      x=[distance],
      text=f"{start}-{total}",
      textposition='auto',
      name=is_type,
      orientation='h',
      showlegend=False,
      marker=dict(
          color=color,
          line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
      )
  ))

fig.add_trace(go.Bar(
    y=['Isoform L'],
    x=[three_utr],
    text=f"{total+1}-{total+three_utr}",
    textposition='auto',
    name='3\' UTR',
    orientation='h',
    showlegend=False,
    marker=dict(
        color='lightskyblue',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))


## Isoform A UTR
five_utr = 67
three_utr = 508
exons_introns = [66, 1564,
                 128, 1495,
                 183, 1965,
                 60, 1141,
                 96, 81,
                 81, 528,
                 124, 81,
                 330]

total = five_utr

fig.add_trace(go.Bar(
    y=['Isoform A'],
    x=[five_utr],
    text=f"1-{total}",
    textposition='auto',
    name='5\' UTR',
    orientation='h',
    marker=dict(
        color='lightpink',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))

for i,e in enumerate(exons_introns):
  start = total + 1
  total = total + e
  text = total
  show_legend = False if i > 1 else True

  if i%2 == 0:
    is_type = "CDS"
    color = "lightseagreen"
    distance = e
  else:
    is_type = "Intron"
    color = "lightsalmon"
    distance = e/10 if e/10 > 50 else 50

  fig.add_trace(go.Bar(
      y=['Isoform A'],
      x=[distance],
      text=f"{start}-{total}",
      textposition='auto',
      name=is_type,
      orientation='h',
      showlegend=show_legend,
      marker=dict(
          color=color,
          line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
      )
  ))

fig.add_trace(go.Bar(
    y=['Isoform A'],
    x=[three_utr],
    text=f"{total+1}-{total+three_utr}",
    textposition='auto',
    name='3\' UTR',
    orientation='h',
    marker=dict(
        color='lightskyblue',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))


y1 = 1.23
y2 = 0.23

fig.update_layout(
    annotations=[
            go.layout.Annotation(
            x=0,
            y=y1,
            ax=0,
            text="TSS @ 1"),
            go.layout.Annotation(
            x=0,
            y=y2,
            ax=0,
            text="TSS @ 1"),
            go.layout.Annotation(
            x=1460,
            y=y1,
            ax=0,
            text="Potential NLS @ 7516→7539"),
            go.layout.Annotation(
            x=1850,
            y=y1,
            ax=0,
            ay=-45,
            text="Potential NLS @ 7913→7936"),
            go.layout.Annotation(
            x=1880,
            y=y1,
            ax=0,
            ay=-90,
            text="Potential NLS @ 7955→7978"),
            go.layout.Annotation(
            x=2412-23,
            y=y1,
            ax=0,
            text="Poly-A Signal @ 8469→84784"),
            go.layout.Annotation(
            x=2412,
            y=y1,
            ax=0,
            ay=-60,
            text="Poly-A Site @ 8497"),
            go.layout.Annotation(
            x=2195-24,
            y=y2,
            ax=0,
            text="Poly-A Signal @ 8414→8474"),
            go.layout.Annotation(
            x=2195,
            y=y2,
            ax=0,
            ay=-60,
            text="Poly-A Site @ 8437"),
            go.layout.Annotation(
            x=350,
            y=y2,
            ax=0,
            ay=-40,
            text="SIR2 Domain Start @ 1724"),
            go.layout.Annotation(
            x=773,
            y=y2,
            ax=0,
            ay=-60,
            text="SIR2 Domain End @ 5411"),
              go.layout.Annotation(
            x=350,
            y=y1,
            ax=0,
            ay=-40,
            text="SIR2 Domain Start @ 1784"),
            go.layout.Annotation(
            x=1450,
            y=y1,
            ax=0,
            ay=-60,
            text="SIR2 Domain End @ 7503")

    ],
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        zeroline=False,
    ),
    margin=dict(l=120, r=0, t=60, b=0),
    bargap=0.55,
    dragmode=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)

fig.update_layout(barmode='stack')

graph = dcc.Graph(
    id='example-graph',
    figure=fig,
    style={'width': '100%', 'overflowY': 'scroll'},
    config={
        'displayModeBar': False
    }
)

rows = html.Div(
    [
        html.H1("Introduction to SIRT6"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(introduction),
                dbc.Col(database_intro),
            ],
        ),
        dbc.Row(gene_structure),
        html.Hr(),
        gene_structure_table,
        html.Hr(),
        dbc.Row(html.H2('Figure 1: SIRT6 Gene Diagram: \n')),
        html.Hr(),
        dbc.Row(html.Img(src="https://i.imgur.com/DQeNlVQ.jpg",
                         style={'height':'100%',
                                'width': '100%'})
        ),
        html.Hr(),
        dbc.Row(variant_info),
        html.Hr(),
        variant_table,
        html.Hr(),
        html.H2("Figure 2: SIRT6 Aligned pre-mRNA Diagrams"),
        html.Hr(),
        dbc.Row(graph),
        html.Hr(),
        dbc.Row(mrna_structure),
        html.Hr(),
        mrna_table,

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
