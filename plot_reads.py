import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('results/barcode77_stats.csv')

print("Summary statistics:")
print(df.describe())

sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
sns.histplot(df['GC%'], bins=50, kde=True, color='skyblue')
plt.title('GC% Distribution')
plt.xlabel('GC%')
plt.ylabel('Count')
plt.savefig('results/gc_distribution.png')
plt.close()

plt.figure(figsize=(8,5))
sns.histplot(df['Length'], bins=100, kde=True, color='salmon')
plt.title('Read Length Distribution')
plt.xlabel('Read Length')
plt.ylabel('Count')
plt.savefig('results/read_length_distribution.png')
plt.close()

plt.figure(figsize=(8,5))
sns.histplot(df['Mean_Quality'], bins=50, kde=True, color='lightgreen')
plt.title('Mean Read Quality Distribution')
plt.xlabel('Mean Quality Score')
plt.ylabel('Count')
plt.savefig('results/mean_quality_distribution.png')
plt.close()

print("Plots saved in results/ folder.")
