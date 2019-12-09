import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app

markdown = dcc.Markdown('''
# References
''')

links = [
'''
1. “5X16: Sirt6 Apo Structure.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/Structure/pdb/5X16](http://http://www.ncbi.nlm.nih.gov/Structure/pdb/5X16).
''',
'''
2. “AceView: Gene:SIRT6, a Comprehensive Annotation of Human, Mouse and Worm Genes with MRNAs or ESTsAceView.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/IEB/Research/Acembly/av.cgi?db=human&q=SIRT6](http://www.ncbi.nlm.nih.gov/IEB/Research/Acembly/av.cgi?db=human&q=SIRT6).
''',
'''
3. Bagga, Paramjeet. S. Bioinformatics, Genomics & Proteomics. December 7, 2019. Ramapo College of New Jersey.
''',
'''
4. “CDD Conserved Protein Domain Family: SIR2.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=350940](http://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=350940).
''',
'''
5. Database, Gene. “SIRT6 Gene (Protein Coding).” GeneCards, [http://www.genecards.org/cgi-bin/carddisp.pl?gene=SIRT6](http://www.genecards.org/cgi-bin/carddisp.pl?gene=SIRT6).
''',
'''
6. Fung, Kevin Y. “Frequently Asked Questions.” International Registry of Werner Syndrome, [http://www.wernersyndrome.org/registry/faq.html](http://www.wernersyndrome.org/registry/faq.html).
''',
'''
7. “Homo Sapiens Sirtuin 6 (SIRT6), RefSeqGene on Chromosome 19 - Nucleotide - NCBI.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/nuccore/1027250684](http://www.ncbi.nlm.nih.gov/nuccore/1027250684).
''',
'''
8. “Homo Sapiens Sirtuin 6 (SIRT6), Transcript Variant 1, MRNA - Nucleotide - NCBI.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/nuccore/NM_016539.4](http://www.ncbi.nlm.nih.gov/nuccore/NM_016539.4).
''',
'''
9. Jiang, Hong, et al. “SIRT6 Regulates TNF-α Secretion through Hydrolysis of Long-Chain Fatty Acyl Lysine.” Nature News, Nature Publishing Group, 3 Apr. 2013, [http://www.nature.com/articles/nature12038](http://www.nature.com/articles/nature12038).
''',
'''
10. Kaluski , S. “Neuroprotective Functions for the Histone Deacetylase SIRT6.” Cell Reports, 2017, [http://www.cell.com/cell-reports/fulltext/S2211-1247(17)30325-X](http://www.cell.com/cell-reports/fulltext/S2211-1247(17)30325-X).
''',
'''
11. Khan, Rubayat Islam, et al. “A Review of the Recent Advances Made with SIRT6 and Its Implications on Aging Related Processes, Major Human Diseases, and Possible Therapeutic Targets.” Biomolecules, MDPI, 29 June 2018, [http://www.ncbi.nlm.nih.gov/pmc/articles/PMC6164879/](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC6164879/).
''',
'''
12. Mao, Zhiyong, et al. “SIRT6 Promotes DNA Repair Under Stress by Activating PARP1.” Science, American Association for the Advancement of Science, 17 June 2011, [https://science.sciencemag.org/content/332/6036/1443.long](https://science.sciencemag.org/content/332/6036/1443.long).
''',
'''
13. Michishita, Eriko, et al. “SIRT6 Is a Histone H3 Lysine 9 Deacetylase That Modulates Telomeric Chromatin.” Nature News, Nature Publishing Group, 12 Mar. 2008, [http://www.nature.com/articles/nature06736](http://www.nature.com/articles/nature06736).
''',
'''
14. Mostoslavsky, Raul, et al. “Genomic Instability and Aging-like Phenotype in the Absence of Mammalian SIRT6.” Cell, Cell Press, 26 Jan. 2006, [http://www.sciencedirect.com/science/article/pii/S0092867406000493?via%3Dihub#bib39](http://www.sciencedirect.com/science/article/pii/S0092867406000493?via%3Dihub#bib39).
''',
'''
15. “NAD-Dependent Protein Deacetylase Sirtuin-6 Isoform 1 [Homo Sapiens] - Protein - NCBI.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/protein/NP_057623.2](http://www.ncbi.nlm.nih.gov/protein/NP_057623.2).
''',
'''
16. “NAD-Dependent Protein Deacetylase Sirtuin-6 Isoform 8 [Homo Sapiens] - Protein - NCBI.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/protein/NP_001307992.1](http://www.ncbi.nlm.nih.gov/protein/NP_001307992.1).
''',
'''
17. “NAD-Dependent Protein Deacetylase Sirtuin-6 Isoform X1 [Homo Sapiens] - Protein - NCBI.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/protein/XP_024307307.1](http://www.ncbi.nlm.nih.gov/protein/XP_024307307.1).
''',
'''
18. “OMIM Entry: SIRT6.” OMIM, [https://omim.org/entry/606211](https://omim.org/entry/606211).
''',
'''
19. Pan, Patricia W, et al. “Structure and Biochemical Functions of SIRT6.” The Journal of Biological Chemistry, American Society for Biochemistry and Molecular Biology, 22 Apr. 2011, [http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3077655/](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3077655/).
''',
'''
20. “rs107251.” SNPedia, [http://www.snpedia.com/index.php/Rs107251](http://www.snpedia.com/index.php/Rs107251).
''',
'''
21. Sebastián, Carlos, et al. “The Histone Deacetylase SIRT6 Is a Tumor Suppressor That Controls Cancer Metabolism.” Cell, Cell Press, 6 Dec. 2012, [http://www.sciencedirect.com/science/article/pii/S0092867412013517](http://www.sciencedirect.com/science/article/pii/S0092867412013517).
''',
'''
22. “SIRT6 Over-Expression May Prevent Progression of Diabetes, Study Finds.” ScienceDaily, ScienceDaily, 18 July 2019, [http://www.sciencedaily.com/releases/2019/07/190718140443.htm](http://www.sciencedaily.com/releases/2019/07/190718140443.htm).
''',


'''
23. “SIRT6 Promoter.” EPD, [http://epd.epfl.ch/cgi-bin/get_doc?db=hgEpdNew&format=genome&entry=SIRT6_1](http://epd.epfl.ch/cgi-bin/get_doc?db=hgEpdNew&format=genome&entry=SIRT6_1).
''',
'''
24. “SIRT6 Recruits SNF2H to DNA Break Sites, Preventing Genomic Instability through Chromatin Remodeling.” Molecular Cell , [http://www.cell.com/molecular-cell/fulltext/S1097-2765(13)00475-9](http://www.cell.com/molecular-cell/fulltext/S1097-2765(13)00475-9).
''',
'''
25. “SIRT6 Sirtuin 6 [Homo Sapiens (Human)] - Gene - NCBI.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/gene/51548](http://www.ncbi.nlm.nih.gov/gene/51548).
''',
'''
26. “SIRT6 Sirtuin 6 [Homo Sapiens (Human)] - Gene - NCBI.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/gene?cmd=retrieve&list_uids=51548](http://www.ncbi.nlm.nih.gov/gene?cmd=retrieve&list_uids=51548).
''',
'''
27. “Sirtuin Family.” interpro7-Client, [http://www.ebi.ac.uk/interpro/entry/InterPro/IPR026590/](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR026590/).
''',
'''
28. Tian, Junhong, and Leilei Yuan. “Sirtuin 6 Inhibits Colon Cancer Progression by Modulating PTEN/AKT Signaling.” Biomedicine & Pharmacotherapy, vol. 106, 2018, pp. 109–116., doi:10.1016/j.biopha.2018.06.070, [https://http://www.sciencedirect.com/science/article/pii/S0753332218332232](https://http://www.sciencedirect.com/science/article/pii/S0753332218332232).
''',
'''
29. “Types of Cancer Treatment.” National Cancer Institute, [http://www.cancer.gov/about-cancer/treatment/types](http://www.cancer.gov/about-cancer/treatment/types).
''',
'''
30. UniProt ConsortiumEuropean Bioinformatics InstituteProtein Information ResourceSIB Swiss Institute of Bioinformatics. “NAD-Dependent Protein Deacetylase Sirtuin-6.” UniProt ConsortiumEuropean Bioinformatics InstituteProtein Information ResourceSIB Swiss Institute of Bioinformatics, 16 Oct. 2019, [http://www.uniprot.org/uniprot/Q8N6T7#structure](http://www.uniprot.org/uniprot/Q8N6T7#structure).
''',
'''
31. UniProt ConsortiumEuropean Bioinformatics InstituteProtein Information ResourceSIB Swiss Institute of Bioinformatics. “SIRT6 Links Histone H3 Lysine 9 Deacetylation to NF-KappaB-Dependent Gene Expression and Organismal Life Span.” UniProt ConsortiumEuropean Bioinformatics InstituteProtein Information ResourceSIB Swiss Institute of Bioinformatics, [http://www.uniprot.org/citations/19135889](http://www.uniprot.org/citations/19135889).
''',
'''
32. Zhang, Weiqi, et al. “SIRT6 Deficiency Results in Developmental Retardation in Cynomolgus Monkeys.” Nature News, Nature Publishing Group, 22 Aug. 2018, [http://www.nature.com/articles/s41586-018-0437-z](http://www.nature.com/articles/s41586-018-0437-z).
''',
'''
33. Zhang, Yingjie, et al. “SIRT6, a Novel Direct Transcriptional Target of FoxO3a, Mediates Colon Cancer Therapy.” Theranostics, Ivyspring International Publisher, 13 Apr. 2019, [http://www.ncbi.nlm.nih.gov/pmc/articles/PMC6531295/](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC6531295/).
''',
'''
34. Zhong, Lei, et al. “The Histone Deacetylase Sirt6 Regulates Glucose Homeostasis via Hif1α.” Cell, Cell Press, 21 Jan. 2010, [http://www.sciencedirect.com/science/article/pii/S0092867409016274](http://www.sciencedirect.com/science/article/pii/S0092867409016274).
''',
'''
35. “Homo Sapiens Sirtuin 6 (SIRT6), Transcript Variant 8, MRNA - Nucleotide - NCBI.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/nuccore/NM_001321063.2](http://www.ncbi.nlm.nih.gov/nuccore/NM_001321063.2).
''',
'''
36. “CDD Conserved Protein Domain Family: SIR2.” National Center for Biotechnology Information, U.S. National Library of Medicine, [http://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=350940](http://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=350940).
''',
'''
37. Shamanna, Raghavendra A., et al. “Recent Advances in Understanding Werner Syndrome.” F1000Research, F1000Research, 28 Sept. 2017, [http://www.f1000research.com/articles/6-1779](http://www.f1000research.com/articles/6-1779).
'''
]


formated_links = [
    html.H2('References'),
    html.Hr()
]

for i,l in enumerate(links):
    link = html.Div([dcc.Markdown(f"{l}")], id=str(i+3))
    formated_links.append(link)
    formated_links.append(html.Br())
    formated_links.append(html.Br())

jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            formated_links,
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
