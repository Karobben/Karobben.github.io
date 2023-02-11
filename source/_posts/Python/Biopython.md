---
title: "Biopython Introduction for Newbies"
ytitle: "Biopython 的入門使用"
description: "Biopython for newbies"
url: biopython2
date: 2020/01/22
toc: true
excerpt: "Biopython is a set of freely available tools for biological computation written in Python by an international team of developers."
tags: [Python, Biopython]
category: [Python, Bio]
cover: 'https://biopython.org/assets/images/biopython_logo_white.png'
thumbnail: 'https://biopython.org/assets/images/biopython_logo_white.png'
priority: 10000
---

## Biopython

<a name="C9IvS"></a>
## 1. Quick Start

```python
from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate

## echo a seq
my_string = "GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG"

##Revers complement
reverse_complement(my_string)

## { 'CTAACCAGCAGCACGACCACCCTTCCAACGACCCATAACAGC' }

##DNA to RNA
transcribe(my_string)

##--> { 'GCUGUUAUGGGUCGUUGGAAGGGUGGUCGUGCUGCUGGUUAG' }

##RNA to DNA
back_transcribe(my_string) --> { 'GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG' }

##DNA to protine
translate(my_string) --> { 'AVMGRWKGGRAAG*' }
```


<a name="mNuzg"></a>
## 2. Sequences

<a name="6mPRo"></a>
### 2.1 reading FASTA file<br />

```python
from Bio import SeqIO
Seq1='GSE44995_Reference_assembled_isotig_seq.fna'
for seq_record in SeqIO.parse(Seq1, "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record.seq))

## print by fasta formate
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
### 2.2 Seq run as string


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

## convert to str
my_seq = str(my_seq)
```


<br />
<a name="qfmb9"></a>
### 2.3 GC caculate
<br />
```python
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
GC(my_seq)

##Result
##46.875
```


<a name="lvo99"></a>
### 2.4 Slicing a sequence
<br />
```python
my_seq[4:12]

#####
the first, second and third codon positions of this DNA sequence:
#####
my_seq[0::3]  # Seq('GCTGTAGTAAG', IUPACUnambiguousDNA())
my_seq[1::3]  # Seq('AGGCATGCATC', IUPACUnambiguousDNA())
my_seq[2::3]  # Seq('TAGCTAAGAC', IUPACUnambiguousDNA())
```


<a name="WruAE"></a>
### 2.5 revers string
<br />
```python
my_seq = my_seq[::-1]
```


<a name="ijsZi"></a>
### 2.6 Changing Font case
<br />
```python
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
dna_seq = Seq("acgtACGT", generic_dna)
dna_seq.upper() --> {Seq('ACGTACGT', DNAAlphabet())}
dna_seq.lower() --> {Seq('acgtacgt', DNAAlphabet())}
```


<a name="RP0Ys"></a>
## 3 Bio-information

<a name="tqSMw"></a>
### 3.1 Revers Complement
<br />
```python
my_seq.reverse_complement()

Seq("ACGTCGTAGCTAC").complement() # standard example => output: Seq('TGCAGCATCGATG')
Seq("ACGTCGTAGCTAC").reverse_complement() # output => Seq('GTAGCTACGACGT')
```


<a name="o4Bl4"></a>
### 3.2 Translation

```python
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

Seq("UUU", IUPAC.unambiguous_rna).translate() # for RNA
Seq("TTT", IUPAC.unambiguous_dna).translate() # for DNA

```


<a name="28baJ"></a>
### 3.3 Translation Tables

```python
from Bio.Data import CodonTable

standard_table = CodonTable.unambiguous_dna_by_name['Standard']
mito_table = CodonTable.unambiguous_dna_by_name['Vertebrate Mitochondrial']

##same as:

standard_table = CodonTable.unambiguous_dna_by_id[1]
mito_table = CodonTable.unambiguous_dna_by_id[2]

mito_table.stop_codons  #--> { ['TAA', 'TAG', 'AGA', 'AGG'] }
mito_table.start_codons # --> { ['ATT', 'ATC', 'ATA', 'ATG', 'GTG'] }
mito_table.forward_table["ACG"] #--> { 'T' }

print(standard_table)
```

<pre>
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
</pre>

## 4. Alignment

### 1. Echo a test file

```bash
## run in bash
echo ">TRINITY_DN106095_c2_g1_i2
MSRIMKVFLFLAVMVCISEAQLHAQCLCPRVRSRISSMTDIREVQIYEATIFCDRMEIVVTNDSGLRYCLNPKLKAVQKLLTAMKPKTSTTARPTVHSSSTGSTNTARM
>TRINITY_DN92154_c0_g1_i1
DIHVRRRTLTRSKTLGRSTNVNKMKLCILLMLGTLLVLVYGMPPISRDYNTHCRCLQVESRIIPPNSLKSIKLVPEGPHCPDMEVIAGLSNGEKVCLNPRSSWVKKLVNFVLEKQQGGALPKNQGQ" > test.fa
```

### 2. Align

```python
## run in python
from Bio import pairwise2
from Bio.Seq import Seq
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo

seq1 = Seq("MSRIMKVFLFLAVMVCISEAQLHAQCLCPRVRSRISSMTDIREVQIYEATIFCDRMEIVVTNDSGLRYCLNPKLKAVQKLLTAMKPKTSTTARPTVHSSSTGSTNTARM")
seq2 = Seq("DIHVRRRTLTRSKTLGRSTNVNKMKLCILLMLGTLLVLVYGMPPISRDYNTHCRCLQVESRIIPPNSLKSIKLVPEGPHCPDMEVIAGLSNGEKVCLNPRSSWVKKLVNFVLEKQQGGALPKNQGQ")
alignments = pairwise2.align.globalxx(seq1, seq2)
test_alignments = pairwise2.align.localds(seq1, seq2, MatrixInfo.blosum62, -10, -1)

for alignment in alignments:
  print(format_alignment(*alignment))

for alignment in test_alignments:
  print(format_alignment(*alignment))
```

<pre>
SingleLetterAlphabet() alignment with 6 rows and 65 columns
MQNTPAERLPAIIEKAKSKHDINVWLLDRQGRDLLEQRVPAKVA...EGP B7RZ31_9GAMM/59-123
AKQRGIAGLEEWLHRLDHSEAIPIFLIDEAGKDLLEREVPADIT...KKP A0A0C3NPG9_9PROT/58-119
ARRHGQEYFQQWLERQPKKVKEQVFAVDQFGRELLGRPLPEDMA...KKP A0A143HL37_9GAMM/57-121
TRRHGPESFRFWLERQPVEARDRIYAIDRSGAEILDRPIPRGMA...NKP A0A0X3UC67_9GAMM/57-121
AINRNTQQLTQDLRAMPNWSLRFVYIVDRNNQDLLKRPLPPGIM...NRK B3PFT7_CELJU/62-126
AVNATEREFTERIRTLPHWARRNVFVLDSQGFEIFDRELPSPVA...NRT K4KEM7_SIMAS/61-125
</pre>


Quick Alignment

```python
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
alignments = pairwise2.align.globalxx("ACCGT", "ACG")
print(format_alignment(*alignments[0]))
```

<pre>
ACCGT
| ||
A-CG-
  Score=3
</pre>


## PDB file

Split the chain from PDF file


Cite: [David Cain](https://stackoverflow.com/questions/11685716/how-to-extract-chains-from-a-pdb-file)

```python
import os
from Bio import PDB

class ChainSplitter:
    def __init__(self, out_dir=None):
        """ Create parsing and writing objects, specify output directory. """
        self.parser = PDB.PDBParser()
        self.writer = PDB.PDBIO()
        if out_dir is None:
            out_dir = os.path.join(os.getcwd(), "chain_PDBs")
        self.out_dir = out_dir

    def make_pdb(self, pdb_path, chain_letters, overwrite=False, struct=None):
        """ Create a new PDB file containing only the specified chains.

        Returns the path to the created file.

        :param pdb_path: full path to the crystal structure
        :param chain_letters: iterable of chain characters (case insensitive)
        :param overwrite: write over the output file if it exists
        """
        chain_letters = [chain.upper() for chain in chain_letters]

        # Input/output files
        (pdb_dir, pdb_fn) = os.path.split(pdb_path)
        pdb_id = pdb_fn[3:7]
        out_name = "pdb%s_%s.ent" % (pdb_id, "".join(chain_letters))
        out_path = os.path.join(self.out_dir, out_name)
        print ("OUT PATH:",out_path)
        plural = "s" if (len(chain_letters) > 1) else ""  # for printing

        # Skip PDB generation if the file already exists
        if (not overwrite) and (os.path.isfile(out_path)):
            print("Chain%s %s of '%s' already extracted to '%s'." %
                    (plural, ", ".join(chain_letters), pdb_id, out_name))
            return out_path

        print("Extracting chain%s %s from %s..." % (plural,
                ", ".join(chain_letters), pdb_fn))

        # Get structure, write new file with only given chains
        if struct is None:
            struct = self.parser.get_structure(pdb_id, pdb_path)
        self.writer.set_structure(struct)
        self.writer.save(out_path, select=SelectChains(chain_letters))

        return out_path

class SelectChains(PDB.Select):
    """ Only accept the specified chains when saving. """
    def __init__(self, chain_letters):
        self.chain_letters = chain_letters

    def accept_chain(self, chain):
        return (chain.get_id() in self.chain_letters)

if __name__ == "__main__":
    """ Parses PDB id's desired chains, and creates new PDB structures. """
    import sys
    if not len(sys.argv) == 2:
        print( "Usage: $ python %s 'pdb.txt'" % __file__)
        sys.exit()

    pdb_textfn = sys.argv[1]

    pdbList = PDB.PDBList()
    splitter = ChainSplitter("")  # Change me.

    with open(pdb_textfn) as pdb_textfile:
        for line in pdb_textfile:
            pdb_id = line[:4].lower()
            chain = line[4]
            pdb_fn = pdbList.retrieve_pdb_file(pdb_id)
            splitter.make_pdb(pdb_fn, chain)
```


Another example:

This one works fine for me

![Carlos Rodrigues](https://stackoverflow.com/questions/11685716/how-to-extract-chains-from-a-pdb-file)

```python
from Bio.PDB import Select, PDBIO
from Bio.PDB.PDBParser import PDBParser
import sys

pdb_file = sys.argv[1]

class ChainSelect(Select):
   def __init__(self, chain):
       self.chain = chain
   def accept_chain(self, chain):
       if chain.get_id() == self.chain:
           return 1
       else:          
           return 0

chains = ['A','B','C']
p = PDBParser(PERMISSIVE=1)       
structure = p.get_structure(pdb_file, pdb_file)

for chain in chains:
   pdb_chain_file = 'pdb_file_chain_{}.pdb'.format(chain)                                 
   io_w_no_h = PDBIO()               
   io_w_no_h.set_structure(structure)
   io_w_no_h.save('{}'.format(pdb_chain_file), ChainSelect(chain))
```

### Extract fasta from PDB file


```python
import sys
from Bio import SeqIO

PDBFile = sys.argv[1]
with open(PDBFile, 'r') as pdb_file:
    for record in SeqIO.parse(pdb_file, 'pdb-atom'):
        print('>' + record.id)
        print(record.seq)
```



<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
