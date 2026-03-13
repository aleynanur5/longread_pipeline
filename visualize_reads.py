import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

stats_file = sys.argv[1] if len(sys.argv) > 1 else "results/Metrics/read_metrics.csv"
out_dir = "results/Visualization"
os.makedirs(out_dir, exist_ok=True)

df = pd.read_csv(stats_file)

df = df[df['Read_ID'] != 'ALL']

metrics = {
    "Length": "Read Length (bp)",
    "Mean_Quality": "Mean Quality",
    "GC%": "GC Content (%)"
}

for metric, label in metrics.items():
    if metric not in df.columns:
        print(f"\n⚠ {metric} column not found in {stats_file}, skipping.")
        continue

    print(f"\n=== {label} Statistics ===")
    print(f"Count: {len(df[metric])}")
    print(f"Mean: {df[metric].mean():.2f}")
    print(f"Median: {df[metric].median():.2f}")
    print(f"Min: {df[metric].min()}")
    print(f"Max: {df[metric].max()}")

for metric, label in metrics.items():
    if metric not in df.columns:
        continue


    filename_safe = metric.replace("%", "p")

    plt.figure(figsize=(10,6))
    plt.hist(df[metric], bins=50, color="skyblue", edgecolor="black")
    plt.title(f"{label} Distribution (Histogram)")
    plt.xlabel(label)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, f"{filename_safe}_Histogram.png"))
    plt.close()

    plt.figure(figsize=(10,6))
    sns.kdeplot(df[metric], fill=True, color="orange")
    plt.title(f"{label} Distribution (KDE)")
    plt.xlabel(label)
    plt.ylabel("Density")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, f"{filename_safe}_KDE.png"))
    plt.close()

if "Length" in df.columns:
    import numpy as np
    plt.figure(figsize=(10,6))
    plt.hist(np.log10(df["Length"] + 1), bins=50, color="purple", edgecolor="black")
    plt.title("Log Read Length Distribution")
    plt.xlabel("log10(Read Length)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "Length_LogHistogram.png"))
    plt.close()

print(f"\n✅ All plots saved in {out_dir}/: Histogram, KD, Log Read Length Distribution for each metric")
