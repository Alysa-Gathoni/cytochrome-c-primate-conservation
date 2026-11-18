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
| Alysa Macharia | Tool selection, alignment and core analysis (Stage 5); repository owner |
| Scott Katana | Notebook setup and machine learning (Stage 7) |

## Repository contributions

Every member uploaded part of this repository.

| Member | Files added |
|---|---|
| Alysa Macharia | `README.md` (first version), `requirements.txt`, `cytochrome_c_primates.ipynb`, `data/cytc_aligned.fasta`, `results/plot5_primate_identity.png`, `results/plot6_entropy.png`, `dashboard/` |
| Scott Katana | `results/plot10_ml.png`, `results/plot11_confusion.png`, `results/table_ml_results.csv`, `results/plot7_mantel.png`, `results/plot8_nj_tree.png`, `results/cytc_nj_tree.nwk` |
| Abraham Seleshi | `data/raw_tier1_core.tsv`, `data/raw_tier2_primates.tsv`, `data/raw_tier3_vertebrates.tsv`, `results/plot1_groups_lengths.png`, `results/plot2_composition.png`, `results/plot3_identity_to_human.png` |
| Fatma Marsa | `data/cytc_clean.fasta`, `data/P99999_features.json`, `results/qc_steps.csv`, `results/plot9_logo.png`, `results/plot4_pca.png` |
| Nicole Njeri | `data/retrieval_log.json`, `data/source_log.csv`, `results/table_identity_by_group.csv`, this updated `README.md`; final check and submission |

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
| `dashboard/index.html` | Interactive results dashboard; opens in any web browser, works offline |
| `dashboard/make_data.py` | Script that built the dashboard's data from `data/cytc_aligned.fasta` and `results/` |
| `requirements.txt` | Python packages used |

## How to run

1. Click **Open in Colab** above.
2. Choose **Runtime > Run all**. The first cell installs MAFFT, Biopython and Logomaker.
3. When asked, allow access to Google Drive. Without the group's Drive folder, the notebook saves files in temporary Colab storage and downloads the data from UniProt.

The saved outputs in the notebook come from data downloaded on 9 November 2026. Re-downloading later may return slightly different records if UniProt has been updated; the files in `data/` are the exact ones analysed.

## Interactive dashboard

`dashboard/index.html` shows the main results interactively: the protein as a chain of conserved and variable positions, every species placed by its distance from human, a sequence comparison for any species, the quality-control funnel, the machine-learning results and the verdict on each hypothesis.

- **Online:** https://alysa-gathoni.github.io/cytochrome-c-primate-conservation/dashboard/ (served by GitHub Pages).
- **On your own computer:** download `dashboard/index.html` and double-click it. It opens in your web browser and needs no internet connection or installation.

## Data source

UniProtKB, https://www.uniprot.org, licensed under CC BY 4.0. Core records: P99999 (human), P99998 (chimpanzee), Q6WUX8 (gorilla), Q5RFH4 (Sumatran orangutan), plus wider primate and vertebrate cytochrome c records selected by the queries in the notebook.

## Main tools

Python, Biopython, MAFFT, pandas, SciPy, scikit-learn, matplotlib, seaborn and Logomaker, run in Google Colab.

## Intended use

This project is for education only. The models show how well taxonomic group can be read from one protein in this dataset; they are not a validated tool for identifying species or samples. Cytochrome c is identical across the great apes, so it cannot tell them apart. Real species identification should use DNA barcoding in an accredited laboratory.

## AI assistance

We used an AI assistant (Claude) to help plan the workflow, draft code and check written explanations. Every member reviewed the code and results, and we take responsibility for all work in this repository.
