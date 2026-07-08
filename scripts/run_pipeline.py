from pathlib import Path
import pandas as pd
root=Path(__file__).resolve().parents[1]
print(pd.read_csv(root/'outputs/gene_signature_ranking.csv').head(20))
