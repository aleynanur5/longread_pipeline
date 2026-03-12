import pandas as pd
from Bio import SeqIO
import os
import sys

input_fastq = sys.argv[1]
output_file = sys.argv[2]

os.makedirs(os.path.dirname(output_file), exist_ok=True)

def calc_gc(seq):
    g = seq.count("G")
    c = seq.count("C")
    return 100 * (g + c) / len(seq) if len(seq) > 0 else 0

def mean_quality(qual):
    return sum(qual) / len(qual) if len(qual) > 0 else 0

data = []
for record in SeqIO.parse(input_fastq, "fastq"):
    seq_id = record.id
    seq = str(record.seq)
    qual = record.letter_annotations["phred_quality"]
    data.append({
        "Read_ID": seq_id,
        "Length": len(seq),
        "GC%": round(calc_gc(seq), 2),
        "Mean_Quality": round(mean_quality(qual), 2)
    })

df = pd.DataFrame(data)
df.to_csv(output_file, index=False)
print(f"✅ Metrics saved to {output_file}")
