import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import numpy as np

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
    data = df[metric]

    plt.figure(figsize=(10,6))
    plt.hist(df[metric], bins=50, color="skyblue", edgecolor="black")

    median_val = data.median()
    min_val = data.min()
    max_val = data.max()

    plt.axvline(median_val, color='red', linestyle='--')
    plt.axvline(min_val, color='green', linestyle=':')
    plt.axvline(max_val, color='blue', linestyle=':')


    plt.text(median_val*1.01, plt.ylim()[1]*0.55, f'{median_val:.2f}', color='red', ha='left', va='center')
    plt.text(min_val*1.01, plt.ylim()[1]*0.50, f'{min_val:.2f}', color='green', ha='left', va='center')
    plt.text(max_val*1.01, plt.ylim()[1]*0.60, f'{max_val:.2f}', color='blue', ha='left', va='center')


    plt.title(f"{label} Distribution (Histogram)")
    plt.xlabel(label)
    plt.ylabel("Count")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, f"{filename_safe}_Histogram.png"))
    plt.close()

    plt.figure(figsize=(10,6))
    sns.kdeplot(df[metric], fill=True, color="orange")

    plt.axvline(median_val, color='red', linestyle='--')
    plt.axvline(min_val, color='green', linestyle=':')
    plt.axvline(max_val, color='blue', linestyle=':')

    plt.text(median_val*1.01, plt.ylim()[1]*0.55, f'{median_val:.2f}', color='red', ha='left', va='center')
    plt.text(min_val*1.01, plt.ylim()[1]*0.50, f'{min_val:.2f}', color='green', ha='left', va='center')
    plt.text(max_val*1.01, plt.ylim()[1]*0.60, f'{max_val:.2f}', color='blue', ha='left', va='center')


    plt.title(f"{label} Distribution (KDE)")
    plt.xlabel(label)
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, f"{filename_safe}_KDE.png"))
    plt.close()

if "Length" in df.columns:
    log_length = np.log10(df["Length"] + 1)
    plt.figure(figsize=(10,6))

    plt.hist(np.log10(df["Length"] + 1), bins=50, color="purple", edgecolor="black")

    median_val = np.median(log_length)
    min_val = np.min(log_length)
    max_val = np.max(log_length)

    plt.axvline(median_val, color='red', linestyle='--')
    plt.axvline(min_val, color='green', linestyle=':')
    plt.axvline(max_val, color='blue', linestyle=':')


    plt.text(median_val*1.01, plt.ylim()[1]*0.55, f'{median_val:.2f}', color='red', ha='left', va='center')
    plt.text(min_val*1.01, plt.ylim()[1]*0.50, f'{min_val:.2f}', color='green', ha='left', va='center')
    plt.text(max_val*1.01, plt.ylim()[1]*0.60, f'{max_val:.2f}', color='blue', ha='left', va='center')


    plt.title("Log Read Length Distribution")
    plt.xlabel("log10(Read Length)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "Length_LogHistogram.png"))
    plt.close()

print(f"\n✅ All plots saved in {out_dir}/: Histogram, KD, Log Read Length Distribution for each metric")
