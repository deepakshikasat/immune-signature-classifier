# Immune Gene Signature Classifier

    Transcriptomics ML-style feature ranking for IFN-treated versus control samples.

    ## Dataset

    Synthetic IFN-stimulation expression matrix using canonical public ISG names.

    ## Methods

    - DEG-style log2FC ranking
- Known ISG annotation
- ML feature-importance comparison scaffold

    ## Reproduce

    ```bash
    python scripts/run_pipeline.py
    ```

    ## Outputs

    - `data/expression_log2.csv`
- `outputs/gene_signature_ranking.csv`
- `figures/top_signature_genes.svg`

    ## Portfolio Note

    This repository uses public or synthetic demonstration data only. It is
    intended to show reproducible computational biology and AI/ML workflow
    design without relying on confidential or employer-owned material.
