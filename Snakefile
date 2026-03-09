rule all:
    input:
        "results/barcode77_fastqc.html",
        "results/barcode77_fastqc.zip",        
        "results/barcode77_stats.csv",
        "results/gc_distribution.png",
        "results/read_length_distribution.png",
        "results/mean_quality_distribution.png"

rule run_fastqc:
    input:
        "data/barcode77.fastq"
    output:
        html="results/barcode77_fastqc.html",
        zip="results/barcode77_fastqc.zip"
    shell:
        "export _JAVA_OPTIONS='-Xmx4G' && fastqc {input} -o results"

rule analyze_reads:
    input:
        "data/barcode77.fastq"
    output:
        "results/barcode77_stats.csv"
    shell:
        "python analyze_reads.py {input} {output}"

rule plot_results:
    input:
        "results/barcode77_stats.csv"
    output:
        "results/gc_distribution.png",
        "results/read_length_distribution.png",
        "results/mean_quality_distribution.png"
    shell:
        "python plot_reads.py"
