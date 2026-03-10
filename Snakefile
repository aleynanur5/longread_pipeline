rule all:
    input:
        "results/barcode77_fastqc.html",
        "results/barcode77_fastqc.zip",        
        "results/NanoPlot-report.html",        
        "results/NanoStats.txt",       
        "results/barcode77_stats.csv"

rule run_fastqc:
    input:
        "data/barcode77.fastq"
    output:
        html="results/barcode77_fastqc.html",
        zip="results/barcode77_fastqc.zip"
    shell:
        "export _JAVA_OPTIONS='-Xmx4G' && fastqc {input} -o results"

rule nanoplot:
    input:
        "data/barcode77.fastq"
    output:
          html="results/NanoPlot-report.html",
          stats="results/NanoStats.txt"
    shell:
          "NanoPlot -t 1 --fastq {input} -o results --plots kde dot"
       
rule analyze_reads:
    input:
        "data/barcode77.fastq"
    output:
        "results/barcode77_stats.csv"
    shell:
        "python analyze_reads.py {input} {output}"

