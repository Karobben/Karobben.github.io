---
url: biopython
---

# Biopython


<a name="C9IvS"></a>
# 1. Quick Start

```python
from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate

# echo a seq 
my_string = GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG

#Revers complement 
reverse_complement(my_string) 

# { 'CTAACCAGCAGCACGACCACCCTTCCAACGACCCATAACAGC' }

#DNA to RNA
transcribe(my_string) 

#--> { 'GCUGUUAUGGGUCGUUGGAAGGGUGGUCGUGCUGCUGGUUAG' }

#RNA to DNA
back_transcribe(my_string) --> { 'GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG' }

#DNA to protine
translate(my_string) --> { 'AVMGRWKGGRAAG*' }
```


<a name="mNuzg"></a>
# 2. Sequences

<a name="6mPRo"></a>
## 2.1 reading FASTA file<br />

```python
from Bio import SeqIO
Seq1='GSE44995_Reference_assembled_isotig_seq.fna'
for seq_record in SeqIO.parse(Seq1, "fasta")
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record.seq))

# print by fasta formate
Seq10=''
for seq_record in SeqIO.parse(Seq1, "fasta"):
  if len(seq_record.seq) < 100:
    Seq10 += ">"+str(seq_record.id)+"\n"
    Seq10 += str(seq_record.seq)+"\n"
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record.seq))
```


<a name="ZwldO"></a>
## 2.2 Seq run as string


```python
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq = Seq("GATCG", IUPAC.unambiguous_dna)
for index, letter in enumerate(my_seq):
  print("%i %s" % (index, letter))

'''
print result
0 G
1 A
2 T
3 C
4 G
'''

print(my_seq[0]) #/ print(my_seq[-1])
Seq("AAAA").count("AA")
len(my_seq)

# convert to str
my_seq = str(my_seq)
```


<br />
<a name="qfmb9"></a>
## 2.3 GC caculate
<br />
```python
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
GC(my_seq)

#Result
#46.875
```


<a name="lvo99"></a>
## 2.4 Slicing a sequence
<br />
```python
my_seq[4:12]

####
the first, second and third codon positions of this DNA sequence:
####
my_seq[0::3]  # Seq('GCTGTAGTAAG', IUPACUnambiguousDNA())
my_seq[1::3]  # Seq('AGGCATGCATC', IUPACUnambiguousDNA())
my_seq[2::3]  # Seq('TAGCTAAGAC', IUPACUnambiguousDNA())
```


<a name="WruAE"></a>
## 2.5 revers string
<br />
```python
my_seq = my_seq[::-1]
```


<a name="ijsZi"></a>
## 2.6 Changing Font case
<br />
```python
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
dna_seq = Seq("acgtACGT", generic_dna)
dna_seq.upper() --> {Seq('ACGTACGT', DNAAlphabet())}
dna_seq.lower() --> {Seq('acgtacgt', DNAAlphabet())}
```


<a name="RP0Ys"></a>
# 3 Bio-information

<a name="tqSMw"></a>
## 3.1 Revers Complement
<br />
```python
my_seq.reverse_complement()

Seq("ACGTCGTAGCTAC").complement() # standard example => output: Seq('TGCAGCATCGATG')
Seq("ACGTCGTAGCTAC").reverse_complement() # output => Seq('GTAGCTACGACGT')
```


<a name="o4Bl4"></a>
## 3.2 Translation

```python
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

Seq("UUU", IUPAC.unambiguous_rna).translate() # for RNA
Seq("TTT", IUPAC.unambiguous_dna).translate() # for DNA

```


<a name="28baJ"></a>
## 3.3 Translation Tables

```python
from Bio.Data import CodonTable

standard_table = CodonTable.unambiguous_dna_by_name['Standard']
mito_table = CodonTable.unambiguous_dna_by_name['Vertebrate Mitochondrial']

#same as:

standard_table = CodonTable.unambiguous_dna_by_id[1]
mito_table = CodonTable.unambiguous_dna_by_id[2]

mito_table.stop_codons  #--> { ['TAA', 'TAG', 'AGA', 'AGG'] }
mito_table.start_codons # --> { ['ATT', 'ATC', 'ATA', 'ATG', 'GTG'] }
mito_table.forward_table["ACG"] #--> { 'T' }

print(standard_table)
'''
  |  T      |  C      |  A      |  G      |
--+---------+---------+---------+---------+--
T | TTT F   | TCT S   | TAT Y   | TGT C   | T
T | TTC F   | TCC S   | TAC Y   | TGC C   | C
T | TTA L   | TCA S   | TAA Stop| TGA Stop| A
T | TTG L(s)| TCG S   | TAG Stop| TGG W   | G
--+---------+---------+---------+---------+--
C | CTT L   | CCT P   | CAT H   | CGT R   | T
C | CTC L   | CCC P   | CAC H   | CGC R   | C
C | CTA L   | CCA P   | CAA Q   | CGA R   | A
C | CTG L(s)| CCG P   | CAG Q   | CGG R   | G
--+---------+---------+---------+---------+--
A | ATT I   | ACT T   | AAT N   | AGT S   | T
A | ATC I   | ACC T   | AAC N   | AGC S   | C
A | ATA I   | ACA T   | AAA K   | AGA R   | A
A | ATG M(s)| ACG T   | AAG K   | AGG R   | G
--+---------+---------+---------+---------+--
G | GTT V   | GCT A   | GAT D   | GGT G   | T
G | GTC V   | GCC A   | GAC D   | GGC G   | C
G | GTA V   | GCA A   | GAA E   | GGA G   | A
G | GTG V   | GCG A   | GAG E   | GGG G   | G
--+---------+---------+---------+---------+--

'''

```

