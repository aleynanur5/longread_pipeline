import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

stats_file = sys.argv[1] if len(sys.argv) > 1 else "results/Metrics/read_metrics.csv"
out_dir = "results/Visualization"
os.makedirs(out_dir, exist_ok=True)

df = pd.read_csv(stats_file)

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

    plt.figure(figsize=(10,6))
    plt.scatter(range(len(df)), df[metric], s=5, alpha=0.6)
    plt.title(f"{label} Values (Dot Plot)")
    plt.xlabel("Read Index")
    plt.ylabel(label)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, f"{filename_safe}_DotPlot.png"))
    plt.close()

print(f"\n✅ All plots saved in {out_dir}/: Histogram, KDE, Dot Plot for each metric")
