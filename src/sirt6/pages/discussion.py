import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app

markdown = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
'''
# Discussion
___
### The Gene
___
Using the partial amino acid sequence, a BLAST search allowed us to identify our gene as SIRT6. The SIRT6 gene's main variant, isoform A, is 8498 base pairs and the protein it codes is 355 amino acids long. Isoform A is compared to a shorter variant, isoform L, which is 8438 bp and codes for 187 amino acids. The two isoforms differ in both number exons and have unique lengths of untranslated regions. Isoform A was also found to contain several possible Nuclear Localization Signals, none of which where found within Isoform L. Lastly, Isoform A had a much more conservation with SIR2, where it spanned over 500 nucleotides of the coding sequence, as opposed to isoform L, where it spanned less than 50 nucleotides.[<sup>25</sup>](/references#25)

SIRT6 was expressed in a variety of tissues, and is predominantly expressed in the colon, lung, and thymus.[<sup>2</sup>](/references#2) Evidence suggests that decreased expression of SIRT6 can promote tumorigenesis and was demonstrably linked to decreased survival rates in patients with colon cancer, indicating its role in tumor suppression.[<sup>28</sup>](/references#28) Interestingly, over-expression of SIRT6 was found to suppress weight gain in mice, under conditions that would normally lead to obesity. While these are just two examples of the potential implications associated with the study of this gene, it also appears to show promise in understanding mechanisms behind the aging process along with other mechanisms in which DNA repair is involved.[<sup>22</sup>](/references#22)

### Protein Structure
___
Identifying the protein structure of SIRT6 gave great insight into the function and binding sites associated with it.  This protein consists of a 355 amino acid structure, containing 13 alpha helices with 87 residues and 14 beta strands with 60 residues. Information provided by UniProt showed the active site, zinc metal binding sites, and an NAD binding site, directly associated with SIRT6 function.  This is also common to the SIR2 superfamily of proteins in which SIRT6 is a part of, involved in catalyzing NAD+ dependent protein and histone deacetylation.  This domain is a 240 amino acid sequence at position 35-274 in our protein.

### Protein Function
___
Using information obtained through the use of UniProt and many research articles, our protein function was able to be determined.  The major functions identified for SIRT6 were histone deacetylase activities and overall DNA repair, including both double stranded breaks as well as base excision repairs.  In double stranded breaks specifically, SIRT6 was shown to be one of the first factors to respond to the break site, recruiting SNF2H, a chromatin remodeler, which deacetylates histone H3K56.  This prevents the recruitment of other downstream factors that are associated with cancers and other diseases. When SIRT6 is not abundant in cells, more DNA breaks can be observed with faulty repair, and cancer is more prevalent.  This protein also has involvement in many biological pathways, including glycolysis and tumorigenesis as two of the main ones.  Isoform A and L that were focused on are found in many tissues such as brain, lung, stomach, and colon.  It is a predominately nuclear protein, having involvement with CHD3, MYC, RELA, AHR, and AKT1 proteins.

### Mutations and Diseases
___
SIRT6 was not found to have direct correlation to any diseases and did not have major mutations that were associated with diseases either.  However, it has been linked to Werner syndrome, Alzheimer’s disease, human perinatal lethality syndrome, Lymphopenia with severe metabolic defects, and cancers. Most of these diseases are associated with a loss or depletion of SIRT6 rather than a mutation of it.  Studies showed that in SIRT6-depleted cells, abnormal telomere structures that resemble defects in many age related disorders were found.  Being that SIRT6 is directly related to DNA repair, lack of it would show more of these diseases typically found older humans.  This is normally due to relative SIRT6 depletion with age as well as buildup of mutations.  Cancer is also more prevalent with SIRT6 depletion, associated with larger, more abundant, and more aggressive tumors.  Being that SIRT6 helps protect the brain from the natural buildup of DNA damage, it could potentially be targeted in age related neurodegeneration.


# Conclusion
___
Our findings did fulfill the objectives given to us at the start of this project through the use of many bioinformatics databases.  These databases allowed us to study and research our protein and gene in order to discover the necessary information relating to our given partial amino acid sequence.  The use of databanks and bioinformatics software has given plenty of information and has provided knowledge that can be further explored in the future.  Bioinformatics is an extremely relevant and useful scientific field.  What used to take years of research to discover information relating to genes and proteins can now be done much faster, simply just by typing a partial amino acid sequence as was done here.  Within a couple of minutes, we knew what our protein was and were able to find information relating to our gene, protein structure, protein function, and mutations/diseases.
'''
]
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
