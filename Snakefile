rule all:
    input:
        "results/NanoPlot-report.html",        
        "results/NanoStats.txt",       
        "results/barcode77_stats.csv"

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
rule analyze_reads:
    input:
        "data/barcode77.fastq"
    output:
        "results/barcode77_stats.csv"
    shell:
        "python analyze_reads.py {input} {output}"

