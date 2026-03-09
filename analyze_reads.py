import gzip
import csv
import sys

def phred33_to_q(char):
    """Phred+33 karakterini kalite skoruna çevirir"""
    return ord(char) - 33

def analyze_fastq(fastq_file, output_file):
    results = []

    # Eğer gz dosya ise gzip ile aç, değilse normal aç
    if fastq_file.endswith('.gz'):
        fh = gzip.open(fastq_file, 'rt')
    else:
        fh = open(fastq_file, 'r')

    while True:
        header = fh.readline().strip()
        if not header:
            break
        seq = fh.readline().strip()
        plus = fh.readline().strip()
        qual = fh.readline().strip()

        read_len = len(seq)
        gc_count = seq.count('G') + seq.count('C')
        gc_percent = (gc_count / read_len) * 100 if read_len > 0 else 0
        mean_qual = sum(phred33_to_q(c) for c in qual) / read_len if read_len > 0 else 0

        results.append([header, read_len, round(gc_percent, 2), round(mean_qual, 2)])

    fh.close()

    # CSV’ye yaz
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Read_ID', 'Length', 'GC%', 'Mean_Quality'])
        writer.writerows(results)

    print(f"{len(results)} reads analyzed. Results saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python analyze_reads.py <input.fastq> <output.csv>")
        sys.exit(1)

    fastq_file = sys.argv[1]
    output_file = sys.argv[2]
    analyze_fastq(fastq_file, output_file)
