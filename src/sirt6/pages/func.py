import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app

markdown = markdown = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
'''
# Major Functions of SIRT6
___
 1. ADP-Ribosyl Transferase
 2. Histone Deacetylase
 3. DNA Repair
 4. Telomeric Chromatin Maintenance
 5. Inflammation
 6. Lipid Metabolism
 7. Glucose Metabolism[<sup>25</sup>](/references#25)

## DNA Repair
___
Mammalian SIRT6 protein plays an important role in DNA repair and cells overall genomic stability.  It deals with both DNA double stranded breaks as well as base excision repairs. In mammalian cells under oxidative stress, it was shown that SIRT6 is recruited to DNA double strand breaks and starts the repair process.  This is through the use of both non-homologous end joining and homologous recombination. SIRT6 associates with PARP1, starting poly-ADP-ribosylase activity and improving DNA repair while under oxidative stress. SIRT6 is also associated with chromatin. Cells that have low levels of chromatin display higher levels of genomic instability, linked to both aging and tumor suppression in mammals.[<sup>24</sup>](/references#24) [<sup>14</sup>](/references#14)

![Figure thumbnail fx1](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/c82b9faf-484b-4fc7-be6a-3318f709565e/fx1.jpg)  
Image Source: [https://www.cell.com/molecular-cell/fulltext/S1097-2765(13)00475-9](https://www.cell.com/molecular-cell/fulltext/S1097-2765(13)00475-9)

The above diagram shows SIRT6 as one of the first factors recruited to a double-strand break in a DNA molecule.  SIRT6 then brings SNF2H, a chromatin remodeler, which deacetylates histone H3K56.  This chromatin remodeling at the respective sites of damage help prevent the recruitment of downstream factors, including RPA, BRCA1, and S3BP1.[<sup>24</sup>](/references#24)


## Histone Deacetylase Activities
___
Human SIRT6 is an NAD+ dependent, histone H3 lysine 9 (H3K9) deacetylase that regulates telomeric chromatin. More specifically, SIRT6 deals with end-to-end chromosomal fusion as well as cellular senescence. In SIRT6 depleted cells, telomere structures appear abnormal. Further research has also showed SIRT6 to directly decrease expression of multiple glucose-metabolic genes through the deacetylation of H3K9 at their promoters.[<sup>13</sup>](/references#13)

![Figure thumbnail fx1](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/1f7d3963-d43c-44da-ad76-a10af4419c31/fx1.jpg)   
Image Source: [https://www.cell.com/cell-reports/fulltext/S2211-1247(17)30325-X](https://www.cell.com/cell-reports/fulltext/S2211-1247(17)30325-X)

The diagram above shows SIRT6 as a histone deacetylase that promotes DNA repair.  SIRT6 helps regulate Tau protein stability and phosphorylation by increasing the activation of kinase GSK3α/β.[<sup>10</sup>](/references#10)

# Major Biological Pathways
___
 1. Removal of long-chain fatty acyl groups from lysine residues[<sup>9</sup>](/references#9)
 2. DNA Repair
 3. Glycolysis
 4. Gluconeogenesis
 5. Tumorigenesis
 6. Neurodegeneration
 7. Cardiac Hypertrophic Responses[<sup>11</sup>](/references#11)
 8. Gene Expression
 9. Apoptosis
 10. Cellular Senescence[<sup>31</sup>](/references#31)

## Glycolysis
___
![](https://ars.els-cdn.com/content/image/1-s2.0-S0092867409016274-fx1.jpg)   
\nImage Source: [https://www.sciencedirect.com/science/article/pii/S0092867409016274](https://www.sciencedirect.com/science/article/pii/S0092867409016274)

As previously stated, SIRT6 functions as a histone H3K9 deacetylase.  This controls the expression of many glycolytic genes. It is noted that SIRT6 appears to function as a corepressor of the transcription factor Hif1α.  This transcription factor is a very important regulator of the nutrient stress responses.  When there is lower amounts of SIRT6, Hif1α activity is increased.  This leads to higher levels of glucose uptake with up-regulation of glycolysis and lower mitochondrial respiration. Studies have also shown that lack of SIRT6 led to an increase in serum lactate, further supporting its role in glucose uptake regulation and a glycolytic switch.[<sup>34</sup>](/references#34)

## Tumorigenesis
___
![](https://ars.els-cdn.com/content/image/1-s2.0-S0092867412013517-fx1.jpg)  
Image Source: [https://www.sciencedirect.com/science/article/pii/S0092867412013517](https://www.sciencedirect.com/science/article/pii/S0092867412013517)

SIRT6 has been identified as a tumor suppressor, regulating aerobic glycolysis in many cancer cells.  Research suggests that SIRT6 plays a role in the establishment and maintenance of cancer.  This is due to tumor formation without activation of any known oncogenes associated with a loss of SIRT6.  Transformed SIRT6 deficient cells also displayed both increased glycolysis and tumor growth, with studies in vivo showing SIRT6 deletion leads to increased number, size, and aggressiveness of tumors.  It also functions as a regulator of ribosome metabolism and is selectively suppressed in many human cancers, showing its importance in reducing cancer metabolism.[<sup>21</sup>](/references#21)


# Major Tissue Expression
___
### Isoform A
 1. Brain
 2. Lung
 3. Stomach
 4. Ascites
 5. Spleen
 6. Kidney
 7. Eye
 8. Skin
 9. Placenta
 10. Heart
 11. Testes
 12. Ovaries[<sup>2</sup>](/references#2)

### Isoform L
 1. Lung
 2. Chondrosarcoma
 3. Colon
 4. Cell Lines
 5. Duodenum
 6. Prostate[<sup>2</sup>](/references#2)

# Developmental Stages

 1. Fetal Brain
 2. Placenta
 3. Adrenal
 4. Heart
 5. Intestine
 6. Kidney
 7. Lung
 8. Stomach[<sup>2</sup>](/references#2) [<sup>25</sup>](/references#25)

# Sub-Cellular Localization
___
SIRT6 is a predominantly nuclear protein. This is associated mostly with telomeric heterochromatin regions, having a strong association with DNA repair and regulation of telomeric chromatin.[<sup>30</sup>](/references#30)

# Protein Interactions
___
SIRT6 has many protein interactions, functioning in DNA repair, cell cycle regulation, and NF-kB transcription.  The top 5 proteins that SIRT6 is known to interact with include: CHD3, MYC, RELA, AHR, and AKT1[<sup>5</sup>](/references#5)

CHD3: This protein is a component of a histone deacetylase complex known as the Mi-2/NuRD complex, which participates in the remodeling of chromatin by deacetylating histones.  This process is important for many processes including transcription.

MYC: This protein has a role in cell cycle progression, apoptosis and cellular transformation.  Amplification of this gene is associated with many human cancers.

RELA: This protein binds with NF-kappa-B to form a heterodimeric complex.  This complex is related to many biological processes, including inflammation, immunity, differentiation, cell growth, tumorigenesis and apoptosis.

AHR: This protein is a transcription factor involved in the regulation of biological responses to halogenated aromatic hydrocarbons by mediating biochemical and toxic effects of them.

AKT1: This protein is a serine/threonine-protein kinase responsible for regulating many processes.  This includes metabolism, proliferation, cell survival, growth and angiogenesis.[<sup>5</sup>](/references#5)
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
