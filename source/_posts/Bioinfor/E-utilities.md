---
title: "Entrez Direct: E-utilities on the UNIX Command Line"
description: "Entrez Direct: E-utilities on the UNIX Command Line"
url: esearch
date: 2020/07/28
toc: true
excerpt: "Entrez Direct: E-utilities on the UNIX Command Line"
tags: [Software, Bioinformatics]
category: [Biology, Bioinformatics, Software, more]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## Entrez Direct: E-utilities on the UNIX Command Line

## Install
```bash
cd ~
/bin/bash
perl -MNet::FTP -e \
    '$ftp = new Net::FTP("ftp.ncbi.nlm.nih.gov", Passive => 1);
    $ftp->login; $ftp->binary;
    $ftp->get("/entrez/entrezdirect/edirect.tar.gz");'
gunzip -c edirect.tar.gz | tar xf -
rm edirect.tar.gz
builtin exit
export PATH=$PATH:$HOME/edirect >& /dev/null || setenv PATH "${PATH}:$HOME/edirect"
./edirect/setup.sh
```

or, you can using **Bioconda**
```bash
conda install -c bioconda entrez-direct
```

## Cookbook
Origin: [NCBI-Hackathons (Archive)
](https://github.com/NCBI-Hackathons/EDirectCookbook)



### Best Practices for EDirect:

* Please keep to <50,000 expected hits (it simply won’t work)
* Please do not run from multiple processors on a compute farm
* Update to latest version

For more information and documentation on EDirect, please see:

* [Entrez Direct: E-utilities on the Unix Command Line](https://www.ncbi.nlm.nih.gov/books/NBK179288/)
* [Insiders Guide to Accessing NLM Data: EDirect Overview](https://dataguide.nlm.nih.gov/edirect/overview.html)

**All items below come with no explicit or implicit warranty.**

**All code is as-is and produced for the bioinformatics community, from the bioinformatics community.**

### EDirect Scripts

### 1. Protein

Description (optional):  
Written by: Peter Cooper
Confirmed by: Ben Busby
Databases: Taxonomy

```
efetch -db nuccore -id NZ_AZKP01000022.1 -seq_start 149413 -seq_stop 154038 -format gbc | xtract -insd CDS INSDInterval_from INSDInterval_to protein_id product
```
**<span style="Background:salmon">backs to:</span>**
```bash
NZ_AZKP01000022.1  1  480  WP_024797446.1  DEAD/DEAH box helicase
NZ_AZKP01000022.1  501  3626  WP_024797445.1  site-specific DNA-methyltransferase
NZ_AZKP01000022.1  3629  4626  WP_024797444.1  DEAD/DEAH box helicase family protein
```
### 2. taxids of taxonomy
Description (optional):  Note:  Options for parsing nodes.dmp from NCBI Taxonomy are cited in issue #25, intentionally left open
Written by: Scott McGinnis (11/17/2017)  
Confirmed by:  
Databases: Taxonomy

```
esearch -db taxonomy -query "vertebrata[orgn]" | efetch -db taxonomy -format docsum | xtract -pattern DocumentSummary -if Rank -equals family -element Id,Division,ScientificName,CommonName | more
```
**<span style="Background:salmon">backs to:</span>**
```bash

```
### 3. SRA from BioProject
Description: Given an SRA Run ID (e.g. SRR532256) that is a member of a BioProject that has additional runs, retrieve all the other run IDs. This is a variant of the BioProject call below.
Written by: Rob Edwards (1/11/2018)
Confirmed by:
Databases: SRA, BioProject

```
esearch -db sra -query "SRR532256" |  efetch -format docsum | xtract -pattern Runs -ACC @acc  -element "&ACC"
```
**<span style="Background:salmon">backs to SRA list:</span>**
```bash
SRR545469  SRR539813  SRR532971  SRR532256  SRR532204  SRR532200  SRR532194  SRR532250
```

#### 3.1 Get all SRA for a BioProject
Description (optional):  
Written by: Bob Sanders (3/22/2017)  
Confirmed by:  
Databases: SRA, BioProject

```
esearch -db bioproject -query "PRJNA356464" | elink -target sra | efetch -format docsum | \
xtract -pattern DocumentSummary -ACC @acc -block DocumentSummary -element "&ACC"
```
**<span style="Background:salmon">backs to SRA list:</span>**
```bash
SRA507436  SRX2439829  SRP095511  SRS1874418  SRR5125027
SRA507436  SRX2439828  SRP095511  SRS1874418  SRR5125026
SRA507436  SRX2439826  SRP095511  SRS1874418  SRR5125024
```
#### 3.2 Get latitiude and longitude for SRA Datasets (e.g. outbreaks and metagenomes)
Description (optional):  
Written by: BB, Mike D, Rob Edwards (4/12/2017)  
Confirmed by:  
Databases: SRA, BioSample

```
## make a ID list
echo "SRA507436SRX2439829SRP095511SRS1874418SRR5125027" |sed 's/SR/ SR/g'| tr " " '\n' | sed '/^$/d' > sra_ids.txt
## run
for i in $(cat sra_ids.txt); do ll=$(esearch -db sra -query $i | \
elink -target biosample | efetch -format docsum | \
xtract -pattern DocumentSummary -block Attribute -if Attribute@attribute_name -equals lat_lon -element Attribute); \
echo -e "$i\t$ll"; done
```
**<span style="Background:salmon">backs to:</span>**
```bash
SRA507436
SRX2439829
SRP095511
SRS1874418
SRR5125027
```
returns nothing - -

#### 3.3 SRA sizes
Description (optional): This retrieves the SRR id and the size in bp of the run from a file (`ids.txt`) of SRR IDs. You can also change `bases` to `size_MB`to get the size of the dataset in MB. _Question: Does the size in MB include the sequence identifiers (i.e. the size of the file) or just the sequences?_
Written by: Rob Edwards (7/6/2017)
Confirmed by:
Databases: SRA
```
## make a ID list
echo "SRA507436SRX2439829SRP095511SRS1874418SRR5125027" |sed 's/SR/ SR/g'| tr " " '\n' | sed '/^$/d' > ids.txt
## Run
epost -db sra -input ids.txt -format acc | esummary -format runinfo -mode xml | xtract -pattern Row -element Run,bases
```
**<span style="Background:salmon">backs to:</span>**
```bash
SRR5125024  36123158012
SRR5125026  44717689640
SRR5125027  26480446596
```

### 4 Gene
#### 4.1 Gene Aliases
Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: gene  
```
esearch -db gene -query "Liver cancer AND Homo sapiens" | \
efetch -format docsum | \
xtract -pattern DocumentSummary -element Name OtherAliases OtherDesignations
```

#### 4.2 Genomic.fa Download
Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by: Peter Cooper (NCBI) and Wayne Matten (NCBI) (12/29/2016, v6.00)   
Databases: assembly  
```
wget `esearch -db assembly -query "Leptospira alstonii[ORGN] AND latest[SB]" | \
efetch -format docsum | \
xtract -pattern DocumentSummary -element FtpPath_RefSeq | \
awk -F"/" '{print $0"/"$NF"_genomic.fna.gz"}'`
```

```
(For larger sets of data the above may fail as wget may not accept a very large number of arguments.
The command below should work for all.)

esearch -db assembly -query "Leptospira alstonii[ORGN] AND latest[SB]" | \
efetch -format docsum | \
xtract -pattern DocumentSummary -element FtpPath_RefSeq | \
awk -F"/" '{print $0"/"$NF"_genomic.fna.gz"}' | \
xargs wget
```

**<span style="Background:salmon">backs to:</span>**
```
--2020-05-18 17:45:54--  ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/569/445/GCF_001569445.1_ASM156944v1/GCF_001569445.1_ASM156944v1_genomic.fna.gz
  (try: 2) => ‘GCF_001569445.1_ASM156944v1_genomic.fna.gz’
Connecting to ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)|130.14.250.13|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD (1) /genomes/all/GCF/001/569/445/GCF_001569445.1_ASM156944v1 ... done.
==> SIZE GCF_001569445.1_ASM156944v1_genomic.fna.gz ... 1311014
==> PASV ... done.    ==> REST 870800 ... done.    
==> RETR GCF_001569445.1_ASM156944v1_genomic.fna.gz ... done.
Length: 1311014 (1.2M), 440214 (430K) remaining (unauthoritative)

GCF_001569445.1_ASM156944v1_genomic.fna.gz                 68%[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==>                                          ] 880.29K   404 B/s    eta 6m 49s
```


#### 4.3 organellar contigs from genbank

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: nuccore  

```
esearch -db nuccore -query "LKAM01" | efetch -format fasta
```

#### 4.4 Get protein sequences from nucleotide accessions

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: nuccore, protein  

```
cat accs_file | epost -db nuccore -format acc | \
elink -target protein | efetch -format fasta
```

#### 4.5 taxonomy (KPCOFG) for taxids

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: taxonomy  

```
efetch -db taxonomy -id 9606,1234,81726 -format xml | \
xtract -pattern Taxon -tab "," -first TaxId ScientificName \
-group Taxon -KING "(-)" -PHYL "(-)" -CLSS "(-)" -ORDR "(-)" -FMLY "(-)" -GNUS "(-)" \
-block "*/Taxon" -match "Rank:kingdom" -KING ScientificName \
-block "*/Taxon" -match "Rank:phylum" -PHYL ScientificName \
-block "*/Taxon" -match "Rank:class" -CLSS ScientificName \
-block "*/Taxon" -match "Rank:order" -ORDR ScientificName \
-block "*/Taxon" -match "Rank:family" -FMLY ScientificName \
-block "*/Taxon" -match "Rank:genus" -GNUS ScientificName \
-group Taxon -tab "," -element "&KING" "&PHYL" "&CLSS" "&ORDR" "&FMLY" "&GNUS"
```
**<span style="Background:salmon">backs to:</span>**
```bash
9606,Homo sapiens,Metazoa,Chordata,Mammalia,Primates,Hominidae,Homo
1234,Nitrospira,-,Nitrospirae,Nitrospira,Nitrospirales,Nitrospiraceae,-
81726,unidentified microorganism,-,-,-,-,-,-
```
### 5 Obtain UniProt IDs from gene symbols

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: gene, protein  

```
esearch -db gene -query "tp53[preferred symbol] AND human[organism]" | \
elink -target protein | \
esummary | \
xtract -pattern DocumentSummary -element Caption SourceDb | \
grep -E '^[OPQ][0-9][A-Z0-9]{3}[0-9]\|^[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}'
```

### 6. Taxon IDs from genome accession numbers

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: nuccore  

```
cat genome_accession.txt | \
epost -db nuccore -format acc | \
esummary | \
xtract -pattern DocumentSummary -element AccessionVersion TaxId
```

### 7. Convert article DOI to PMID

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by: Mike Davidson (NLM) (12/16/2016, v5.80)  
Databases: pubmed  

```
esearch -db pubmed -query "10.1111/j.1468-3083.2012.04708.x" | \
esummary | \
xtract -pattern DocumentSummary -block ArticleId -sep "\t" -tab "\n" -element IdType,Value | \
grep -E '^pubmed|doi'
```
**<span style="Background:salmon">backs to:</span>**
```bash
pubmed  23004926
doi  10.1111/j.1468-3083.2012.04708.x
```
### 8. Access organism specific meta-data from NCBI genome database

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: genome, bioproject  

```
esearch -db genome -query "22954[uid]" | \
elink -target bioproject | \
efetch -format xml | \
xtract -pattern DocumentSummary -element Salinity OxygenReq OptimumTemperature TemperatureRange Habitat
```

### 9. Get the status of records from PubMed search

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by: Mike Davidson (NLM) (12/16/2016, v5.80)  
Databases: pubmed  

```
esearch -db pubmed -query "pde3a AND 2016[dp]" | \
esummary | \
xtract -pattern DocumentSummary -element Id RecordStatus
```
**<span style="Background:salmon">backs to:</span>**
```bash
28959341  PubMed
28060719  PubMed - indexed for MEDLINE
27975297  PubMed - indexed for MEDLINE
27927168  PubMed - indexed for MEDLINE
27865066  PubMed - indexed for MEDLINE
27053290  PubMed - indexed for MEDLINE
27765510  PubMed - indexed for MEDLINE
27524442  PubMed - indexed for MEDLINE
27662514  PubMed - indexed for MEDLINE
27647936  PubMed - indexed for MEDLINE
27633875  PubMed - indexed for MEDLINE
27610941  PubMed - indexed for MEDLINE
27502037  PubMed - indexed for MEDLINE
27180831  PubMed - indexed for MEDLINE
28959563  PubMed
26934198  PubMed - indexed for MEDLINE
26926596  PubMed - indexed for MEDLINE
26656089  PubMed - indexed for MEDLINE
26628038  PubMed - indexed for MEDLINE
26460717  PubMed - indexed for MEDLINE
26374610  PubMed - indexed for MEDLINE
```
#### 9.1 Conduct a PubMed search and retrieve the results as a list of PMIDs

Description (optional):  
Written by: Mike Davidson (2/22/2017)  
Confirmed by: Mike Davidson (NLM) (2/22/2017, v6.30)  
Databases: pubmed  

```
esearch -db pubmed -query "seasonal affective disorder" | efetch -format uid
```
**<span style="Background:salmon">backs to:</span>**
```bash
32277035
32252583
32163458
32111489
32108162
...
```

### 10. Sort the hits by sequence length in nucleotide database

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: nuccore  

```
esearch -db nuccore -query "bacillus[orgn] AND biomol_rRNA[prop] AND 1500:1560[slen]" | \
esummary | \
xtract -pattern DocumentSummary -element Slen Extra | \
sort -rnk 1
```

### 11. Getting meta data from assembly

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: assembly  

```
esearch -db assembly -query "mammals[orgn] AND latest[filter]" | \
efetch -format docsum | \
xtract -pattern DocumentSummary -element Organism,SpeciesName,BioSampleAccn,LastMajorReleaseAccession \
-block Stat -if "@category" -equals chromosome_count -element Stat | \
grep -Pv "\t0$"
```

### 12. Fetch HSPs from a BLAST hit in FASTA                                              

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: nuccore  

```
blastn -db nr -query in.fna -remote -outfmt "6 sacc sstart send" | \
xargs -n 3 sh -c 'efetch -db nuccore -id "$0" -seq_start "$1" -seq_stop "$2" -format fasta'
```

### 13. Get all Gene Ontology IDs for a given protein accession

Description (optional):  
Written by: NCBI Folks (12/14/2016)  
Confirmed by:  
Databases: protien, biosystems  

```
epost -db protein -id BAD92651.1 -format acc | \
elink -target biosystems | \
efetch -format docsum | \
xtract -pattern externalid -element externalid | \
awk '{if ($0 ~ /GO/) print $0}'
```

### 14. Get the ten most frequently-occurring authors for a set of articles

Description (optional): Searches PubMed for the string "traumatic brain injury athletes", restricts results to those published in 2015 and 2016, retrieves the full XML records for each of the search results, extracts the last name and initials of every author on every record, sorts the authors by frequency of occurrence in the results set, and presents the top ten most frequently-occurring authors, along with the number of times that author appeared.  
Written by: Mike Davidson (NLM) (12/15/2016)  
Confirmed by: Mike Davidson (NLM) (12/16/2016)  
Databases: pubmed  

```
esearch -db pubmed -query "traumatic brain injury athletes" -datetype PDAT -mindate 2015 -maxdate 2016 | \
efetch -format xml | \
xtract -pattern Author -sep " " -element LastName,Initials | \
sort-uniq-count-rank | \
head -n 10
```

### 15. Get the ten funding agencies who are most active in funding articles on a particular topic

Description (optional): Searches PubMed for the string "diabetes AND pregnancy", restricts results to those published in 2014 through 2016, retrieves the full XML records for each of the search results, extracts the funding agencies for every  grant on every record, sorts the agencies by frequency of occurrence in the results set, and presents the top ten most frequently-occurring agencies, along with the number of times that agency appeared.  
Written by: Mike Davidson (2/17/2017)  
Confirmed by:  Mike Davidson (NLM) (v6.30, 2/17/2017)  
Databases: pubmed  

```
esearch -db pubmed -query "diabetes AND pregnancy" -datetype PDAT -mindate 2014 -maxdate 2016 | \
efetch -format xml | \
xtract -pattern Grant -element Agency | \
sort-uniq-count-rank | \
head -n 10
```

### 16. Look up the publication date for thousands of PMIDs (option one)

Description (optional):  Takes a file which contains a list of PMIDs (table_of_pubmed_ids) and uses `cat` to access the contents of the file, `epost` to post the PMIDs to the history server, `efetch` to retrieve the records and `xtract` to extract PMID and Publication Date.  
Written by: NCBI Folks (12/15/2016)  
Confirmed by:  Mike Davidson (NLM) (v6.30, 2/17/2017)  
Databases: pubmed  

```
cat table_of_pubmed_ids | \
epost -db pubmed | \
efetch -format xml | \
xtract -pattern PubmedArticle -element MedlineCitation/PMID \
-block PubDate -sep " " -element Year,Month MedlineDate
```

### 17. Look up the publication date for thousands of PMIDs (option two)

Description (optional): Takes a file which contains a list of PMIDs (table_of_pubmed_ids) and `epost -input` to access the contents of the file and post the PMIDs to the history server, `efetch` to retrieve the records and `xtract` to extract PMID and Publication Date.  
Written by: Mike Davidson (2/17/2017)  
Confirmed by:  Mike Davidson (NLM) (v6.30, 2/17/2017)  
Databases: pubmed  

```
epost -input table_of_pubmed_ids -db pubmed | \
efetch -format xml | \
xtract -pattern PubmedArticle -element MedlineCitation/PMID \
-block PubDate -sep " " -element Year,Month MedlineDate
```

### 18. Find the first author for a set of PubMed records

Description (optional): Outputs the PMID and first author's last name and initials for one or more PubMed records
Written by: Mike Davidson (2/17/2017)  
Confirmed by:  Mike Davidson (NLM) (v6.30, 2/17/2017)  
Databases: pubmed  

```
efetch -db pubmed -id 16940437 -format xml | \
xtract -pattern PubmedArticle -element MedlineCitation/PMID \
-block Author -position first -sep " " -element LastName,Initials
```

### 19. Find the first author and any other authors who contributed equally for a set of PubMed records

Description (optional): Outputs the PMID and first author's last name and initials for one or more PubMed records. If the record indicates equal contributors to the first author, the last name and initials for all equal contributors will also be output, separated by commas.  
Written by: Mike Davidson (10/27/2017)  
Confirmed by:  Mike Davidson (NLM) (v7.40, 10/27/2017)  
Databases: pubmed  

```
efetch -db pubmed -id 22358458,26877147 -format xml | \
xtract -pattern PubmedArticle -element MedlineCitation/PMID \
-block Author -position first -sep " " -tab ", " -element LastName,Initials -EQUAL Author@EqualContrib \
-block Author -if "+" -is-not 1 \
-and Author@EqualContrib -equals Y \
-and "&EQUAL" -equals Y \
-sep " " -tab ", " -element LastName,Initials
```

### 20 Download GEO Data from a BioProject Accession

Description (optional):  
Written by: NCBI Folks (12/16/2016)  
Confirmed by:  
Databases: gds  

```
esearch -db gds -query "PRJNA313294[ACCN]" | \
efetch -format docsum | \
xtract -pattern DocumentSummary -element FTPLink
```

### 21 Extract all MeSH Headings from a given PMID

Description (optional): Retrieves the PMID of a PubMed record, followed by a pipe-delimitted list of MeSH Descriptors for a PMID.  
Written by: Mike Davidson (10/02/2017)  
Confirmed by: Mike Davidson (NLM) (v7.30, 10/02/2017)  
Databases: pubmed  

```
efetch -db pubmed -id 24102982 -format xml | \
xtract -pattern PubmedArticle -tab "|" -element MedlineCitation/PMID \
-block MeshHeading -tab "|" -element DescriptorName
```


#### Extract all MeSH Headings and Subheadings from a given PMID
Description (optional): Retrieves the PMID of a PubMed record, followed by a pipe-delimitted list of MeSH Descriptors and Qualifiers for a PMID. Each Descriptor is followed by any attached qualifiers, separated by "/".  
Written by: Mike Davidson (10/02/2017)  
Confirmed by: Mike Davidson (NLM) (v7.30, 10/02/2017)  
Databases: pubmed  

```
efetch -db pubmed -id 24102982 -format xml | \
xtract -pattern PubmedArticle -tab "|" -element MedlineCitation/PMID \
-block MeshHeading -tab "|" -sep "/" -element DescriptorName,QualifierName
```

#### Search for articles by authors affiliated with a specific institution by matching two partial affiliation strings.

Description (optional): Searching PubMed for two affiliation strings ANDed together (e.g. "translational medicine\[AD] AND thomas jefferson\[AD]") will retrieve all records that have both strings listed somewhere in the record's Affiliation data, but does not require both strings be listed on the same author's affiliation. To generate a list of PMIDs where both strings are present in the same affiliation element, use the following script.  
Written by: Mike Davidson (4/2/2018)  
Confirmed by:  Mike Davidson (NLM) (v8.10, 4/2/2018)  
Databases: pubmed  

```
esearch -db pubmed -query "translational medicine[ad] AND thomas jefferson[ad]" | \
efetch -format xml | \
xtract -pattern PubmedArticle -PMID MedlineCitation/PMID \
-block Affiliation -if Affiliation -contains "translational medicine" -and Affiliation -contains "thomas jefferson" \
-tab "\n" -element "&PMID" | \
sort -n | uniq
```
#### Search for PMC articles citing a gived PubMed articler; retrieve title, source, ID

Description: Retrieve information about all PMC articles (wihich have free fulltext available) which cite a gived PubMed article
Written by: Lukas Wagner (08/16/2018)
Databases: pubmed, pmc

```
esearch -db pubmed -query 23618408 | elink -name pubmed_pmc_refs -target pmc | \
efetch -format docsum | \
xtract -pattern DocumentSummary -element Title -element Source -block ArticleId -if "IdType" -equals pmcid -element Value
```



## Xtract


Exp1: aquire infor inner a tag

```bash
esearch -db bioproject -query "PRJNA356464" | elink -target sra | efetch -format docsum | \
xtract -pattern DocumentSummary -ACC @acc -block DocumentSummary -element "&ACC"
```


<pre>
SRA507436	SRX2439829	SRP095511	SRS1874418	SRR5125027
SRA507436	SRX2439828	SRP095511	SRS1874418	SRR5125026
SRA507436	SRX2439827	SRP095511	SRS1874418	SRR5125025
SRA507436	SRX2439826	SRP095511	SRS1874418	SRR5125024
</pre>

Example of single `Runs`
```
<Runs>
    <Run acc="SRR5125024"
        total_spots="119613106"
        total_bases="36123158012"
        load_done="true"
        is_public="true"
        cluster_name="public"
        static_data_available="true"/>
</Runs>
```

As a result, we can aquire total spots with `@total_spots`
