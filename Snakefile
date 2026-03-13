rule all:
    input:
        "results/NanoPlot-report.html",
        "results/NanoStats.txt",
        "results/Metrics/read_metrics.csv",
        "results/Visualization/Length_Histogram.png",
        "results/Visualization/Length_KDE.png",
        "results/Visualization/Length_LogHistogram.png",
        "results/Visualization/Mean_Quality_Histogram.png",
        "results/Visualization/Mean_Quality_KDE.png",
        "results/Visualization/GCp_Histogram.png",
        "results/Visualization/GCp_KDE.png"

rule nanoplot:
    input:
        "data/barcode77.fastq"
    output:
        html="results/NanoPlot-report.html", 
        stats="results/NanoStats.txt",
        detail_dir=directory("results/NanoPlot_details")
    shell:
        """
        mkdir -p {output.detail_dir}
        NanoPlot -t 1 --fastq {input} -o {output.detail_dir} --plots kde dot
        mv {output.detail_dir}/NanoPlot-report.html {output.html}
        mv {output.detail_dir}/NanoStats.txt {output.stats}
       
        """

rule calculate_metrics:
    input:
        "data/barcode77.fastq"
    output:
        "results/Metrics/read_metrics.csv"
    shell:
        "python calculate_metrics.py {input} {output}"

rule visualize_metrics:
    input:
        "results/Metrics/read_metrics.csv"
    output:
        expand("results/Visualization/{metric}_{plot}.png", metric=["Length","Mean_Quality","GCp"], plot=["Histogram","KDE"]) + ["results/Visualization/Length_LogHistogram.png"]
    shell:
        "python visualize_reads.py {input}"
