# FASTQ Files Quality Control Report

**Dear Professor Kılıç,**

The quality control analysis of the provided FASTQ files has been completed. The
following metrics were calculated for each read and visualized:

1. Read length  
2. GC content  
3. Read quality  
4. Length vs. Quality  
5. Yield / total base count  
6. Longest reads and their quality scores  

## Visualization

- **NanoPlot HTML reports:** Detailed and interactive visualizations of read
  lengths, quality, and cumulative yield.  
- **Python script-generated plots:** Histograms and KDE plots of GC content,
  read lengths, and quality scores showing median, minimum, and maximum values.  
- Some metrics were also saved as CSV and TXT files, offering both interactive
  and static visualization options.  

## Key Findings

1. **GC content:** Average 53.53%, most reads in mid-GC range, providing more
   balanced coverage (Delahaye & Nicolas, 2021; Browne et al., 2020).  

2. **Read length:** Average 1,038 bp, median 547 bp, N50 1,761 bp; mostly
   short-to-medium reads, with some ultra-long reads (~686 kb) forming a
   long-tail distribution (Goodwin et al., 2016; Oxford Nanopore Technologies,
   2025).  

3. **Read quality:** Average score 8.9; ~48.6% of reads > Q10, 8.5% > Q15. Low
   Q20 counts indicate higher error rate; filtering or error correction needed
   before downstream analyses.  

4. **Length vs. quality:** Short/medium reads maintain quality, ultra-long reads
   sometimes have lower quality, requiring careful consideration.  

5. **Longest reads:** Max read 686 kb, quality Q3.7; other long reads medium
   quality (Libuit et al., 2022; Wick et al., 2019; OH SFS Handbook, 2021).  

6. **Yield / total bases:** Total ≈84 Mb across 81,011 reads. Cumulative yield
   plots show steady increase; quality distribution may limit high-accuracy
   analyses.  

## Conclusion and Recommendations

Dataset contains short-to-medium reads with low-to-moderate quality. Insufficient
for ultra-long read analyses (de novo assembly, gap closure, telomere/tandem
repeat, MHC/segmental duplication).  

Small-scale DNA/RNA methylation/modification analyses possible, but low high-
quality read proportion (8.5% Q15+) limits reliability (Logsdon et al., 2020).  

Suitable for short-read error correction, low-coverage assembly, reference-
based alignment, and SNP/indel calling, with careful filtering to ensure
reliability (Schröder et al., 2009; Yu & Sun, 2013; Kosugi & Terao, 2024).  

**Sincerely,**  
Aleynanur DOĞAN ATALAY  
Massive Bioinformatics
