# Comparative Analysis of Cytochrome c in Humans and Non-Human Primates

Computing for Bioinformatics group project, Strathmore University (2026).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Alysa-Gathoni/cytochrome-c-primate-conservation/blob/main/cytochrome_c_primates.ipynb)

## Research question

How conserved is the cytochrome c protein sequence across humans and selected non-human primates, and do sequence similarities reflect their evolutionary relationships?

## Group members and roles

| Member | Role |
|---|---|
| Nicole Njeri | Project coordination; research question, objectives and conclusions (Stages 1 and 8) |
| Abraham Seleshi | Data retrieval from UniProtKB and exploratory analysis (Stages 2 and 4) |
| Fatma Marsa | Quality control and biological interpretation (Stages 3 and 6) |
| Alysa Macharia | Tool selection, alignment and core analysis (Stage 5) |
| Scott Katana | Notebook setup, machine learning and GitHub repository (Stage 7) |

## Repository contents

| Path | Contents |
|---|---|
| `cytochrome_c_primates.ipynb` | The analysis notebook, Stages 1 to 8, with all outputs saved |
| `data/raw_*.tsv` | Unedited UniProt downloads, one per query |
| `data/retrieval_log.json` | Exact queries, URLs and download dates |
| `data/source_log.csv` | Accession, organism and review status for every downloaded record |
| `data/P99999_features.json` | UniProt functional annotation of human cytochrome c |
| `data/cytc_clean.fasta` | Sequences that passed the seven-step quality checklist |
| `data/cytc_aligned.fasta` | MAFFT multiple sequence alignment |
| `results/` | Figures (PNG), tables (CSV) and the neighbour-joining tree (Newick) |
| `requirements.txt` | Python packages used |

## How to run

1. Click **Open in Colab** above.
2. Choose **Runtime > Run all**. The first cell installs MAFFT, Biopython and Logomaker.
3. When asked, allow access to Google Drive. Without the group's Drive folder, the notebook saves files in temporary Colab storage and downloads the data from UniProt.

The saved outputs in the notebook come from data downloaded on 9 November 2026. Re-downloading later may return slightly different records if UniProt has been updated; the files in `data/` are the exact ones analysed.

## Data source

UniProtKB, https://www.uniprot.org, licensed under CC BY 4.0. Core records: P99999 (human), P99998 (chimpanzee), Q6WUX8 (gorilla), Q5RFH4 (Sumatran orangutan), plus wider primate and vertebrate cytochrome c records selected by the queries in the notebook.

## Main tools

Python, Biopython, MAFFT, pandas, SciPy, scikit-learn, matplotlib, seaborn and Logomaker, run in Google Colab.
