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


introduction = markdown = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
    '''
###### **Official Name:** Sirtuin 6 [<sup>25</sup>](/references#25)
###### **Official Symbol:** SIRT6[<sup>25</sup>](/references#25)
###### **Other Known Symbols:** SIR2L6, SIR2L6, and LOC51548[<sup>2</sup>](/references#2)
###### **NCBI Gene ID:** [51548](https://www.ncbi.nlm.nih.gov/gene/51548)[<sup>25</sup>](/references#25)
###### **Cytogenetic location:** 19p13.3[<sup>25</sup>](/references#25)
###### **Absolute genomic location:** 4174109 - 4182566[<sup>25</sup>](/references#25)
###### **Genome ID:** GRCh38 - Build 38.p13[<sup>25</sup>](/references#25)
    '''
    ]
)

database_intro = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
        '''
        * **Database:** [AceView](https://www.ncbi.nlm.nih.gov/IEB/Research/Acembly/av.cgi?db=human&q=SIRT6)[<sup>2</sup>](/references#2)
        * **NCBI RefSeqGene Accession #:** [NG_047153.1](https://www.ncbi.nlm.nih.gov/nuccore/1027250684)[<sup>7</sup>](/references#7)
        * **Isoform 1:**
            * ###### **AceView Variant:** A (August 2010)[<sup>2</sup>](/references#2)
            * **NCBI RefSeq Protein Accession #:** [NP_057623.2](https://www.ncbi.nlm.nih.gov/protein/NP_057623.2)[<sup>15</sup>](/references#15)
            * **NCBI RefSeq mRNA Accession #:** [NM_016539.4](https://www.ncbi.nlm.nih.gov/nuccore/NM_016539.4)[<sup>8</sup>](/references#8)
        * **Isoform 2:**
            * ###### **AceView Variant:** L (August 2010)[<sup>2</sup>](/references#2)
            * **NCBI RefSeq Protein Accession #:** [NP_001307992.1](https://www.ncbi.nlm.nih.gov/protein/NP_001307992.1)[<sup>16</sup>](/references#16)
            * **NCBI RefSeq mRNA Accession #:**  [NM_001321063.2](https://www.ncbi.nlm.nih.gov/nuccore/NM_001321063.2)[<sup>35</sup>](/references#35)
        ###### Note: All tables and diagrams were contstructed using AceView. As links to AceView variants are not possible, the above links to corresponding NCBI isoforms are provided. Please be aware that these may not match up exactly with the data found on this website.
            '''
    ]
)

gene_info  = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
'''
___
## Gene Structure
___
### Introduction
___
The above diagrams and tables exhibit data found on AceView for SIRT6 isoforms A & L. Isoform A was selected as it is the primary variant, coding for the longest amino acid chain: 355 amino acids. Isoform L, coding for 187 amino acids was selected by cross-referencing AceView variants with NCBI isoforms. Isoform L was the longest variant found on AceView that matched up to a RefSeq mRNA & Protein.[<sup>2,</sup>](/references#2)[<sup>25</sup>](/references#25)

In Figure 1, genomic data from Table 1, showcasing all 20 isoforms known, was transformed into a diagram. This diagram localizes the promoter region and the elements it contains, along with exons, introns, and the splice signal and site for isoform A, while showing the alternative sites for isoform L.

### The Promoter
___
The promoter region is a 2000 base pair sequence, upstream from the Transcription Start Site (TSS), found at position 1.[<sup>2</sup>](/references#2) Within the promoter, a GC Box, CCAT Box, and TATA Box were identified using the Eukaryotic Promoter Database (EPD).  A p-cutoff of 0.01 was used for the CCAT Box and TATA Box, as more strict cutoffs did not yield any viable results. A 0.001 cutoff was used to identify the GC Box. The TATA Box value chosen was the one closest to the TSS, however this is not likely to be accurate, as TATA Boxes are generally found within thirty bases upstream of the TSS. A CCAT Box was selected upstream of the TSS, and a GC Box was selected upstream of the CCAT Box. Values taken from EPD were incremented by one as the database outputs are relative to the TSS.[<sup>23</sup>](/references#23)

### Identified Signals
___
A variety of signals on the SIRT6 gene were identified, including polyadenylation signals and sites, and nuclear localization signals.

The polyadenylation sites for each isoform was found on AceView, and was then offset by the distance to its respective signal in order to identify the location of the polyadenylation signals. The polyadenylation signal sequence for all Isoforms is "AATAAA", except for Isoform R, which has the sequence "CATGAA." Polyadenylation signals are 23 bps away form the site, with the exception of Isoform R, which is 13 bps away from its site.

Additionally, Isoform A had three potential Nuclear Localization Signals. As AceView reports NLS location in amino acids, manual conversions were performed in order to determine the nucleotide positions of each signal. One potential signal was identified on Exon 7 and two on Exon 8.[<sup>2</sup>](/references#2)

### SIR2 Domain
___
A SIR2 family domain was identified in both Isoform A and L.
* In Isoform A this domain spans amino acids 52 to 221.
* In Isoform L this domain spans amino acids 52 to 65.

These amino acids were converted to the nucleotide positions that code for them. In Isoform A this conserved region is found between (and including parts of) exons 2 and 7.[<sup>2</sup>](/references#2)

For more information about functions relating to the SIR2 family, please see [Protein Structure](/protstruct).

### CDS Variation Between Isoforms
___
Isoform A is known to have 8 exons and 7 introns, whereas isoform L has 7 exons and 6 introns. As isoform A is 355 amino acids and isoform L is 187 amino acids, there are 168 more amino acids being coded for by the primary variant. A comparison of the exons and coding regions can provide insight into this difference.
* Exon 1 of isoform A is 133 bps, and Exon 1 of isoform L is 73 bps.
  * The 5' UTR is 67 bps in isoform A and 7 bps in isoform L.
  * Both coding sequences are 66 bps.
* Exon 2 was 128 bps, and did not vary between isoforms A & L.
* Exon 3 of isoform A is 183 bps, and is not present in isoform L.
* Exons 4, 5, 6, are 60 bps, 96 bps, 81 bps, respectively.
*  Exon 7 is 124 bps within isoform A and 84 bps within isoform L.
* Exon 8 is 838 bps
  * The 3' UTR is 508 bps in Isoform A and 789 bps in isoform L.
  * In isoform A the coding region on Exon 8 is 330 bps and in isoform L it is 49 bps.

Interestingly, Exon 3, one of the larger exons within the SIRT6 gene is not present within isoform L. This difference contributes to the shortened length of isoform L, accounting for 61 of the 168 amino acids not found in this variant. Additionally, the difference in coding regions on the last exon accounts for 94 more amino acids. Lastly, the difference in Exon 7 accounts for the last 13 amino acids.[<sup>2</sup>](/references#2)

### Expression & Its Implications
___
As SIRT6 is predominantly found within the colon, it becomes a primary area of interest. A 2018 study found evidence to suggest that SIRT6 may be involved in the suppression of colon cancer. The study confirmed the protein's role in tumor suppression though its influence on PTEN/AKT signaling, which is involved in a variety of process including metabolism and cell growth.[<sup>28</sup>](/references#28)
Another area of interest for SIRT6 was explored in another 2018 study that looked at the gene's role in obesity. They noted that SIRT6 is known to decrease with age and under "overeating" conditions. Evidence from the study suggested that SIRT6's regulation of glucose and lipids plays a role in diabetes and obesity when its expression is diminished, and that up-regulation of SIRT6 suppressed the progression of diabetes and obesity, even under "overeating" conditions.[<sup>22</sup>](/references#22)
'''
]
)


gene_structure = pd.read_csv("https://raw.githubusercontent.com/rshtirmer/SIRT6_Files/master/data/genestructure.csv")#pd.read_csv("data/genestructure.csv")
mrna_structure = pd.read_csv("https://raw.githubusercontent.com/rshtirmer/SIRT6_Files/master/data/pre_mrna.csv")
variant_data = pd.read_csv("https://raw.githubusercontent.com/rshtirmer/SIRT6_Files/master/data/variants.csv")
expression_data = pd.read_csv("https://raw.githubusercontent.com/rshtirmer/SIRT6_Files/master/data/expression.csv")

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

expression_table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in expression_data.columns],
    data=expression_data.to_dict('records'),
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
        html.H2("Figure 2: SIRT6 Aligned pre-mRNA Diagrams:"),
        html.Hr(),
        dbc.Row(graph),
        html.Hr(),
        dbc.Row(mrna_structure),
        html.Hr(),
        mrna_table,
        html.Hr(),
        html.H2('Table 4: Expression of SIRT6 Variants: '),
        html.Hr(),
        expression_table,
        gene_info,
        html.Hr(),
        html.H2('Development Differential Expression'),
        html.H3('Figure 3: Differential SIRT6 Expression During Fetal Development'),
        html.Hr(),
        html.Img(src='https://i.imgur.com/w3Gaz8h.png', width="80%"),
        html.Hr(),
        dcc.Markdown(
            dangerously_allow_html=True,
                children=['Figure 3 highlights the differences in gene expression of SIRT6 Variant A in a variety of tissues across several intervals during gestation. Measurements were recorded within the adrenal glands, heart, intestine, kidney, lungs, and stomach. Expression of SIRT6 increases through the development of the organisms in all tissues, which is inline with the SIRT6 function of DNA Repair. It is of note that gene expression dropped off from a maximum to a minimum within the heart at 20 weeks. This can not be written off as an outlier either, as multiple measurements within that range were observed[<sup>25</sup>](/references#25)'])
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
