import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app
markdown = dcc.Markdown(
    dangerously_allow_html=True,
        children=[
    '''
    # Tools and Methods
    ___
    ## Bioinformatics Tools
    ___
    [NCBI](https://www.ncbi.nlm.nih.gov/): (National Center for Biotechnology Information) contains many databases in which information regarding amino acid comparison is stored.

    [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi): basic local alignment search tool that finds similarity between sequences in order to identify a protein.

    [RefSeq](https://www.ncbi.nlm.nih.gov/refseq/): database that contains reference genome and mRNA sequences.[<sup>25</sup>](/references#25)

    [AceView](https://www.ncbi.nlm.nih.gov/IEB/Research/Acembly/): contains cDNA gene and transcripts for a given gene.[<sup>2</sup>](/references#2)

    [GeneCards](https://www.genecards.org/): database that provides information on all annotated and predicted human genes[<sup>5</sup>](/references#5)

    [OMIM](https://www.ncbi.nlm.nih.gov/omim): (Online Mendelian Inheritance in Man) database that provides human genes and phenotypes along with disease association.[<sup>18</sup>](/references#18)

    [UniProt](https://www.uniprot.org/): (Universal Protein Resource) a resource for protein sequence and functional information related to a specific protein.[<sup>30</sup>](/references#30) [<sup>31</sup>](/references#31)

    [iCn3D](https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html): a molecule viewer that allows for the 3D visualization of a protein.

    [DashBio](https://dash.plot.ly/dash-bio): a bioinformatics tool kit for visualizing biological data.

    [EPD](https://epd.epfl.ch//index.php): (Eukaryotic Promoter Database) a database used to determine cis-regulatory elements on an gene.[<sup>23</sup>](/references#23)

    [SNPedia](https://www.snpedia.com/index.php/SNPedia): a database of variation mutations associated with a specific locus on a gene.[<sup>20</sup>](/references#20)

    ## Methods
    ___
    After receiving the partial amino acid sequence, a P-BLAST search was performed in order to identify the protein. Because the sequence was known to be incomplete, the specific isoform was disregarded, and the protein was identified to be SIRT6. Having identified the protein, a variety of sources were explored in order to obtain preliminary information on the protein. First, the NCBI gene page for SIRT6 was used to obtain the genomic sequence and mRNA sequences, along with the introductory information, including the cytogenetic and absolute genomic locations. From NCBI, the AceView page specific to SIRT6 was located. Within AceView, the "Alternative mRNAs features, proteins, introns, exons, sequences" link was used to explore the variants available. The variants on AceView where cross-referenced with the protein isoforms on NCBI, and the two longest were selected.

    To construct the gene diagram and table, AceView was used to source the data downstream from the promoter. The cis-regulatory elements within the promoter where identified using EPD. As the TATA Box provided by EPD was several hundred bases of upstream of the promoter, the true locations of the cis-regulatory elements are likely unknown. With that said, the TATA box closest to the promoter was selected, and the GC and CCAT Boxes upstream of the TATA box where selected. All values in EPD where incremented by one as they are reported relative to the TSS.

    Using the AceView pages specific to the variants selected, utrs, exons, introns, signals, and domains where identified. AceView provides exon and intron lengths and positions, along with the lengths of the untranslated regions. Using this data a gene diagram was constructed, displaying the alternative transcripts. To complete the gene diagram, the polyadenylation sites where found on AceView for each isoform, and their positions where offset by the distance to the signal, in order to identify the nucleotide locations of the signal.

    Additionally the data on AceView allowed us to construct the lengths and positions of the coding regions for the two variants selected. The SIR2 domain was identified on both variants, along with potential transport signals. These regions where reported by AceView in amino acids, so the coding regions where used to determine the nucleotide positions. This was done by determining how many amino acids are present in each coding region in order to find which nucleotide positions code for which amino acids.

    After identifying the gene using the BLAST search and finding our specific gene on NCBI, there were many links to the right side associated with SIRT6.  NCBI gave direct links to our protein structure as well as links to UniProt, which was used for most of the protein structure as well as function. UniProt listed our protein as UniProtKB - Q8N6T7 (SIR6_HUMAN), associated with sirtuin-6 in humans.  Here, information about the binding sites, active sites, and secondary structure were discussed. UniProt listed reference websites and journals as well that were useful for determining both protein structure and function.

    The information given about protein function once again started on the NCBI website.  Here, information regarding the major functions could be found as well as listing many other websites that were helpful, including both bioinformatics websites as well as research articles pertaining to SIRT6.  This included links to UniProt once again, which listed many functions and other articles associated with SIRT6 function.  UniProt also gave sub-cellular localization of our protein. OMIM was also used as there were many full articles listed that described both protein function as well as diseases that have association with SIRT6.  Major tissue expression for our specific isoforms was taken from data provided by AceView.  Developmental stages that SIRT6 is involved in was taken from both AceView and charts provided by NCBI.  GeneCards finally used to determine protein-protein interactions.

    To determine mutations and diseases associated with our protein, we visited OMIM in a link attached to the NCBI gene website.  Here there was plenty of information talking about diseases associated with SIRT6, even if the mutation was not directly involved in the disease.  There were plenty of links to research articles that could be found on OMIM that were used to talk about SIRT6-deficient cells and how they could have association with different diseases.  The main diseases that we focused on mostly came from information found on OMIM.  However, some further information about the diseases was found in other articles and websites.  While only one specific mutation was noted for SIRT6, this information was found on SNPedia.

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
