# FASTQ Files Quality Control Report

**Dear Professor Kılıç,**

The quality control analysis of the provided FASTQ files has been completed. In
this study, the following metrics were calculated for each read and visualized:

1. Read length  
2. GC content  
3. Read quality  
4. Length vs. Quality  
5. Yield / total base count  
6. Longest reads and their quality scores  

## Visualization

- **NanoPlot HTML reports:** Provided detailed and interactive visualizations of
  read lengths, quality, and cumulative yield.  
- **Python script-generated plots:** Histograms and density (KDE) plots were
  created for GC content, read lengths, and quality scores, showing median,
  minimum, and maximum values.  
- Some metrics were also saved as CSV and TXT files, offering both interactive
  and static visualization options.  

## Key Findings

1. **GC content:** Evaluated using a histogram. The dataset has an average GC
   content of 53.53%, with most reads concentrated in the mid-GC range. This
   helps achieve more balanced genomic coverage in Nanopore sequencing and
   improves the reliability of downstream analyses (Delahaye & Nicolas, 2021;
   Browne et al., 2020).  

2. **Read length:** Assessed via histogram, KDE, and scatter plots. The average
   read length is 1,038 bp, median length 547 bp, and N50 is 1,761 bp,
   indicating the dataset mostly contains short-to-medium reads. Some ultra-long
   reads (up to ≈686 kb) create a noticeable long-tail distribution (Goodwin
   et al., 2016; Oxford Nanopore Technologies, 2025).  

3. **Read quality:** Evaluated using scatter plots and KDE. The average quality
   score is 8.9, with ~48.6% of reads above Q10. Reads above Q15 constitute
   only 8.5%, and reads above Q20 are very few. This indicates a relatively
   high error rate, suggesting that quality filtering or error correction steps
   may be needed before downstream analyses.  

4. **Length vs. quality relationship:** Scatter plot and KDE analyses show that
   short and medium reads generally maintain average quality, while some
   ultra-long reads have lower quality values. Careful consideration of ultra-
   long reads is needed for downstream analyses.  

5. **Longest reads and quality scores:** Scatter plots and tables reveal that
   the longest read is 686 kb with a low quality score (Q3.7). Other long reads
   show medium-quality values, indicating some reads must be cautiously
   evaluated due to low quality (Libuit et al., 2022; Wick et al., 2019; OH SFS
   Handbook, 2021).  

6. **Yield / total base count:** Cumulative yield and bar plots indicate a total
   dataset of ≈84 Mb across 81,011 reads. Cumulative yield plots show a steady
   increase in data production. Considering quality distributions, the dataset
   may be limited for analyses requiring high accuracy.  

## Conclusion and Recommendations

The dataset mainly consists of short-to-medium reads with low-to-moderate
quality. Therefore, it is insufficient for analyses requiring long or ultra-
long reads, such as high-contiguity de novo assembly, gap closure, telomere/
tandem repeat analysis, or MHC/segmental duplication resolution.  

Small-scale DNA/RNA methylation and modification analyses are possible, but the
low proportion of high-quality reads (8.5% Q15+) limits reliability (Logsdon et
al., 2020).  

On the other hand, the dataset is suitable for short-read error correction,
low-genome coverage assembly, reference-based alignment, and SNP/indel calling.
Applying careful filtering in these analyses can yield reliable results
(Schröder et al., 2009; Yu & Sun, 2013; Kosugi & Terao, 2024).  

**Sincerely,**  
Aleynanur DOĞAN ATALAY  
Massive Bioinformatics  

## References

1. Goodwin, S., McPherson, J. D., & McCombie, W. R. (2016). Coming of age: ten
   years of next-generation sequencing technologies. Nature reviews.
   Genetics, 17(6), 333–351.  

2. Oxford Nanopore Technologies. (n.d.). Short, long, or ultra long: which read
   length is right for you? Nanopore Know How. Retrieved March 18, 2025, from
   https://nanoporetech.com/es/blog/short-long-or-ultra-long-which-read-length-
   is-right-for-you?utm_source=chatgpt.com  

3. Logsdon, G. A., Vollger, M. R., & Eichler, E. E. (2020). Long-read human
   genome sequencing and its applications. Nature reviews. Genetics, 21(10),
   597–614.  

4. Kosugi, S., & Terao, C. (2024). Comparative evaluation of SNVs, indels, and
   structural variations detected with short- and long-read sequencing data.
   Human genome variation, 11(1), 18.  

5. Yu, X., & Sun, S. (2013). Comparing a few SNP calling algorithms using
   low-coverage sequencing data. BMC bioinformatics, 14, 274.  

6. Schröder, J., Schröder, H., Puglisi, S. J., Sinha, R., & Schmidt, B. (2009).
   SHREC: a short-read error correction method. Bioinformatics (Oxford,
   England), 25(17), 2157–2163.  

7. Libuit, K. G., Lunn, S., Carleton, H., Khan, W., Kanwar, S., van Heusden, P.,
   Amrosio, F., Lemmer, D., Mboowa, G., Macori, G., & Southgate, J. (2022, June
   23). Quality Control Solutions for SARS CoV 2 Genomic Analysis. Public
   Health Alliance for Genomic Epidemiology. Retrieved from
   https://pha4ge.org/resource/guidance/qc_solutions_for_sars_cov_2_genomic_analysis/  

8. OH SFS Handbook (Release v0.0.1, Sep 10, 2021). Nanopore basecalling and
   trimming — Oxford Nanopore read quality typical range and filtering
   guideline. Retrieved from https://oh-sfs-handbook.readthedocs.io/_/downloads/en/latest/pdf/  

9. Wick, R. R., Judd, L. M., & Holt, K. E. (2019). Performance of neural network
   basecalling tools for Oxford Nanopore sequencing. Genome biology, 20(1), 129.
   https://doi.org/10.1186/s13059-019-1727-y  

10. Browne, P. D., Nielsen, T. K., Kot, W., Aggerholm, A., Gilbert, M. T. P.,
    Puetz, L., Rasmussen, M., Zervas, A., & Hansen, L. H. (2020). GC bias affects
    genomic and metagenomic reconstructions, underrepresenting GC-poor organisms.
    GigaScience, 9(2), giaa008.  

11. Delahaye, C., & Nicolas, J. (2021). Sequencing DNA with nanopores: Troubles
    and biases. PloS one, 16(10), e0257521.
