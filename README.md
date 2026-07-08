# Immune Gene Signature Classifier

Upgraded to include a public interferon-signature reference set and explicit overlap analysis. The expression matrix is still synthetic, so this is not yet a full public RNA-seq analysis, but the biological validation layer now uses public canonical IFN alpha/gamma response genes.

## Reproduce

```bash
python scripts/run_pipeline.py
```

## Outputs

- `data/expression_log2.csv`
- `data/public_ifn_signature_genes.csv`
- `outputs/gene_signature_ranking.csv`
- `figures/top_signature_genes.svg`

## Analysis Report

Open `reports/analysis_report.html` for the hypothesis, public data provenance, process, outputs, and interpretation.

## Portfolio Note

This repository uses public data sources or clearly labelled synthetic demonstration data only. No employer-owned or confidential data are included.
