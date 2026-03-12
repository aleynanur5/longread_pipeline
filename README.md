# Long Read Bioinformatics Pipeline
A reproducible mini bioinformatics pipeline for analyzing long-read sequencing data using Snakemake and Python.

## Pipeline Overview
This pipeline performs basic analysis of long-read sequencing data and generates quality metrics and visualizations to help researchers evaluate sequencing results before downstream analysis.

### Main steps of the pipeline:
1. Read input FASTQ sequencing data
2. Generate Quality Metrics & Statistics using NanoPlot → Produces HTML and TXT outputs
3. Calculate Additional Metrics using calculate_metrics.py → Produces CSV outputs 
4. Generate Custom Visualizations using visualize_reads.py → PNG plots 
5. Save all results in organized output directories → Store all outputs in results/ 

### Pipeline Workflow
```
Raw Sequencing Data (FASTQ)
↓
Quality Metrics & Statistics (NanoPlot)
↓
Additional Metrics (calculate_metrics.py)
↓
Results Folder
```

This workflow analyzes long-read sequencing data and generates statistics and visualizations to help evaluate sequencing quality before further downstream analysis.

## Repository Structure

```
longread_pipeline/
│
├── README.md
├── Snakefile
├── calculate_metrics.py
├── data
│   ├── Case Study_ Gıda Güvenliği Krizi_ Bozulmuş Ürün.zip
│   └── barcode77.fastq
├── environment.yml
├── results
│   ├── Metrics
│   │   └── read_metrics.csv
│   ├── NanoPlot-report.html
│   ├── NanoPlot_details
│   │   ├── LengthvsQualityScatterPlot_dot.html
│   │   ├── LengthvsQualityScatterPlot_kde.html
│   │   ├── NanoPlot_20260312_1104.log
│   │   ├── Non_weightedHistogramReadlength.html
│   │   ├── Non_weightedLogTransformed_HistogramReadlength.html
│   │   ├── WeightedHistogramReadlength.html
│   │   ├── WeightedLogTransformed_HistogramReadlength.html
│   │   └── Yield_By_Length.html
│   ├── NanoStats.txt
│   └── Visualization
│       ├── GCp_DotPlot.png
│       ├── GCp_Histogram.png
│       ├── GCp_KDE.png
│       ├── Length_DotPlot.png
│       ├── Length_Histogram.png
│       ├── Length_KDE.png
│       ├── Mean_Quality_DotPlot.png
│       ├── Mean_Quality_Histogram.png
│       └── Mean_Quality_KDE.png
└── visualize_reads.py
```
## Required Folders 
- `data/` → Place your FASTQ files here.  
- `results/` → This folder will be automatically created by the pipeline for output files.
  
## Requirements
Make sure the following tools are installed:
-	Git
-	Git LFS
-	Conda (Miniconda or Anaconda)

## Installation
1. Clone the repository
   ```
   git clone https://github.com/aleynanur5/longread_pipeline.git
   cd longread_pipeline
   ```
2. Install the Conda environment
   ```
   conda env create -f environment.yml
   conda activate longread_env
   ```
3. Initialize Git LFS (for large files)
   ```
   git lfs install
   ```

## Running the Pipeline
Execute the workflow using Snakemake:
```
snakemake --cores 1
```
This will execute the full workflow defined in the Snakefile and generate results in the results/ directory.

## Input Data
The pipeline expects long-read sequencing data in FASTQ format.
Example input location:
data/example.fastq
Large sequencing FASTQ files are tracked using Git LFS.

## Output
After running the pipeline, the results will be stored in the results/ directory.
Outputs include:
- Quality metrics (`.html` or `.txt`)
- Additional Metrics (`.csv`)
- Visualization plots (`.png`)

## Reproducibility
The pipeline uses:
- Snakemake for workflow management
- Conda environment for dependency management
- Git LFS for handling large sequencing FASTQ files

This project uses a Conda environment defined by an environment.yml file to provide reproducible analysis.
To recreate the environment:
- conda env create -f environment.yml
- conda activate longread_env

## Author
Aleynanur DOĞAN ATALAY
Bioinformatics Internship Project
