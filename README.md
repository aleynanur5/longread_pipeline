# Long Read Bioinformatics Pipeline
A reproducible mini bioinformatics pipeline for analyzing long-read sequencing data using Snakemake and Python.

## Pipeline Overview
This pipeline performs basic analysis of long-read sequencing data and generates quality metrics and visualizations to help researchers evaluate sequencing results before downstream analysis.

### Main steps of the pipeline:
1. Read input FASTQ sequencing data
2. Analyze read statistics (analyze_reads) → Compute read statistics (CSV)
3. Generate plots and QC reports using NanoPlot → Visualize statistics (HTML + TXT outputs)
4. Save results in an organized output directory → Store all outputs in results/ folder (HTML and CSV outputs)

### Pipeline Workflow
```
Raw Sequencing Data (FASTQ)
↓
Read Analysis (analyze_reads.py)
↓
Quality Metrics & Statistics (NanoPlot)   
↓
Results Folder
```

This workflow analyzes long-read sequencing data and generates statistics and visualizations to help evaluate sequencing quality before further downstream analysis.

## Repository Structure

```
longread_pipeline/
├── README.md                         # Project documentation
├── Snakefile                         # Snakemake workflow definition
├── analyze_reads.py                  # Script for analyzing sequencing reads
├── data/
│   ├── example.zip                   # Example data (if needed)
│   └── example.fastq                 # Example FASTQ file
├── environment.yml                   # Conda environment file for reproducibility
└── results/
    ├── NanoPlot-report.html          # NanoPlot quality report
    ├── NanoStats.txt                 # NanoPlot statistics
    ├── example_stats.csv             # Read statistics
    └── NanoPlot_details/             # All detailed plots
        ├── LengthvsQualityScatterPlot_dot.html
        ├── LengthvsQualityScatterPlot_kde.html
        ├── Non_weightedHistogramReadlength.html
        ├── Non_weightedLogTransformed_HistogramReadlength.html
        ├── WeightedHistogramReadlength.html
        ├── WeightedLogTransformed_HistogramReadlength.html
        ├── Yield_By_Length.html
        └── NanoPlot log file
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
3. Install the Conda environment
   ```
   conda env create -f environment.yml
   conda activate longread_env
   ```
5. Initialize Git LFS (for large files)
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
- Read statistics (`.csv`)
- Quality metrics (`.html` or `.txt`)
- Visualization plots (`.html` inside NanoPlot_details/)

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
