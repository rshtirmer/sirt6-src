import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app

markdown = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
'''
# Major Diseases Associated with SIRT6
___
 1. Werner Syndrome[<sup>13</sup>](/references#13)
 2. Alzheimer’s Disease[<sup>10</sup>](/references#10)
 3. Human Perinatal Lethality Syndrome[<sup>32</sup>](/references#32)
 4. Lymphopenia with Severe Metabolic Defects[<sup>14</sup>](/references#14)
 5. Cancers[<sup>21</sup>](/references#21)

# Major Mutations
___
While there is not much information noted about mutations associated with SIRT6, one study found individuals with either the CC or CT genotype at rs107251 within SIRT6 to display greater than 5-year mean survival advantages as compared to the TT genotype.[<sup>20</sup>](/references#20)

When cells were depleted of SIRT6, they exhibited abnormal telomere structures that resemble defects observed in Werner syndrome, a premature aging disorder. At telomeric chromatin, SIRT6 deacetylates H3K9 and is required for the stable association of WRN, the factor that is mutated in Werner syndrome[<sup>13</sup>](/references#13)

# Most Common Diseases
___
## Age Related Disorders
___
While SIRT6 does not have any diseases that are directly associated with, it has involvement in many age related disorders including Werner syndrome and Alzheimer’s disease.  Therefore, rather than choosing one specific disease which there is not much information on, we chose to classify them into one category.

In SIRT6-depleted cells, abnormal telomere structures that resemble defects observed in Werner syndrome, a premature aging disorder, were shown. At the telomeric chromatin, SIRT6 deacetylates H3K9 and is needed for stable association of WRN, the factor that becomes mutated in Werner syndrome.  WRN is associated with telomeres and regulates processing during S-phase.[<sup>13</sup>](/references#13)  Werner syndrome is a hereditary disease due to disturbances in genetic information.  Being that SIRT6 has a large role in DNA repair and many aging processes, it is not much of a surprise that SIRT6-depleted cells would exhibit similar responses as Werner syndrome.  While patients with Werner syndrome are treated for their various symptoms, including heart disease, removal of cataracts, and treatment of cancers, there is no cure available.[<sup>6</sup>](/references#6)

![Image result for werner syndrome pathway](https://f1000researchdata.s3.amazonaws.com/manuscripts/13105/4900a17c-019d-48ca-bdf2-8e1388da751f_figure1.gif)
Image Source: [https://f1000research.com/articles/6-1779](https://f1000research.com/articles/6-1779)

The pathway shown above represents sensor proteins Ku70/Ku80, WRN, MRN, and PARP1 to mediate repair in a DNA double stranded break.  This process is required for genomic stability and to prevent the loss of genetic information.[<sup>37</sup>](/references#37)

Alzheimer's disease is another age related disorder associated with SIRT6.  While there is not a direct relationship that is noted, patients with Alzheimer's disease show a severe lack of SIRT6.  Being that the primary factor leading to neurodegenerative diseases is aging, once again it is not surprising that SIRT6-deficient cells showed these signs.  DNA damage is also higher in patients with Alzheimer's disease, as well as Parkinson’s disease and amyotrophic lateral sclerosis.  While there is no cure for these diseases either, it is worth noting that SIRT6 helps protect the brain from the natural buildup of DNA damage and could be targeted in age related neurodegeneration.[<sup>10</sup>](/references#10)

## Cancers
___
While SIRT6 does not have a direct relation with any specific cancer, it has been shown that SIRT6 deficiency leads to increased tumor growth.  As discussed in Protein Function, SIRT6 has a role in the process tumorigenesis and overall suppression of tumors.  More specifically, it is shown to be a tumor suppressor involved in the regulation of aerobic glycolysis in cancer cells.  While loss of SIRT6 led to tumor formation without activation of known oncogenes, transformed SIRT6-deficient cells showed increased tumor growth and glycolysis. Research has also shown that SIRT6 deletion leads to more aggressive, large, and abundant tumor growth.[<sup>21</sup>](/references#21)  SIRT6 is not known to be associated with any hereditary cancers.  While there is no cure, there are many treatments.  This includes surgery, radiation therapy, chemotherapy, immunotherapy, targeted therapy, hormone therapy, stem cell transplants, and precision medication.[<sup>29</sup>](/references#29)

![](https://ars.els-cdn.com/content/image/1-s2.0-S0092867412013517-fx1.jpg)
Image Source: [https://www.sciencedirect.com/science/article/pii/S0092867412013517](https://www.sciencedirect.com/science/article/pii/S0092867412013517)

While previously shown under Protein Function, this diagram gives a good representation of SIRT6 and its influence on tumor growth.[<sup>21</sup>](/references#21)
'''])




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
