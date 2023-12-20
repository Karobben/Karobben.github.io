---
toc: true
url: cdhit
covercopy: <a href="https://www.bioinformatics.org/cd-hit/cd-hit-user-guide">© Weizhong Li</a>
priority: 10000
date: 2023-12-13 15:21:40
description: "CD-HIT, a protein/nuclear"
excerpt: "CD-HIT was originally a protein clustering program. The main advantage of this program is its ultra-fast speed. It can be hundreds of times faster than other clustering programs, for example, BLASTCLUST. Therefore it can handle very large databases, like NR. The 1st version of this program, CD-HI, was published and released in 2001. The 2nd version, called CD-HIT, was published in 2002 with significant improvements. Since 2004, CD-HIT has been hosted at bioinformatics.org as an open source project. Current CD-HIT package can perform various jobs like clustering a protein database, clustering a DNA/RNA database, comparing two databases (protein or DNA/RNA), generating protein families, and many others.
"
tags: [Software, Cluster, NGS]
category: [Biology, Bioinformatics, Software, more]
cover: "https://www.bioinformatics.org/cd-hit/cd-hit-user-guide_files/image003.jpg"
thumbnail: "https://www.bioinformatics.org/cd-hit/cd-hit-user-guide_files/image003.jpg"
---



 

 
## CD-HIT

Documentation: [CD-HIT](https://www.bioinformatics.org/cd-hit/cd-hit-user-guide)

CD-HIT (Cluster Database at High Identity with Tolerance) is a widely used bioinformatics tool designed to cluster biological sequences (such as DNA, RNA, or proteins) to reduce sequence redundancy and improve the efficiency of other sequence analyses. It's particularly useful when dealing with large datasets, such as those frequently encountered in genomics and proteomics studies.

Here are some key features and uses of CD-HIT:

1. **Sequence Clustering**: CD-HIT efficiently clusters similar sequences together based on a user-defined similarity threshold. For example, if you set a threshold of 90%, the tool will group sequences that are 90% identical into the same cluster.

2. **Reduction of Redundancy**: By clustering similar sequences, CD-HIT helps in reducing redundancy in the dataset. This is particularly important when creating sequence databases or when analyzing large datasets where many sequences may be very similar or nearly identical.

3. **Speed and Efficiency**: CD-HIT is known for its speed and low memory usage, making it suitable for handling very large datasets that are common in modern high-throughput sequencing projects.

4. **Multiple Applications**: It's used in a variety of applications, such as creating non-redundant sequence databases, preparing datasets for further analyses (like phylogenetic studies), or in metagenomics for analyzing diversity and similarity of species.

5. **Customizable Parameters**: Users can customize several parameters, such as the identity threshold for clustering, the word size for initial comparisons, and memory usage, allowing for flexibility depending on the specific requirements of the data or the analysis.

6. **Output Files**: CD-HIT generates two main types of output files - one containing the clustered sequences and another (`.clstr` file) detailing the composition of each cluster.

CD-HIT is a command-line tool, which means it is run from a terminal or command prompt and offers great flexibility in scripting and automation within bioinformatics pipelines. The tool is an essential part of the toolkit for biologists and bioinformaticians dealing with large-scale sequence data.

## Example

```bash
cd-hit -i Trunked.fa -o cdhit/Trunked_$x.fa -c $x -M 32000 -d 0 -T 8 -n 5 -aL 0.8 -s 0.95  -uS 0.2  -sc 1 -sf 1
```

The command you've provided is for CD-HIT, a widely used bioinformatics tool for clustering and comparing protein or nucleotide sequences. CD-HIT helps to significantly reduce the redundancy of large datasets by clustering similar sequences together based on a specified sequence identity threshold. This is particularly useful in tasks like constructing databases or preparing datasets for other analyses where redundancy might be an issue.

Let's break down the components of your command:

- `cd-hit`: This invokes the CD-HIT program.

- `-i Trunked.fa`: The `-i` option specifies the input file. Here, the input file is `Trunked.fa`, which likely contains a collection of nucleotide or protein sequences in FASTA format.

- `-o cdhit/Trunked_$x.fa`: The `-o` option specifies the output file. This command will create an output file in the `cdhit` directory with a name based on the value of the variable `$x`. The `$x` seems to be a shell variable that would be replaced with its value when the command runs.

- `-c $x`: The `-c` option sets the sequence identity threshold. Sequences are clustered together if they are similar to each other above this threshold. The exact value is determined by the variable `$x`.

- `-M 32000`: This sets the maximum available memory (in MB). `32000` here means 32,000 MB, or 32 GB of RAM.

- `-d 0`: The `-d` option is for the description length to show in the `.clstr` output file. `0` means it will show the full sequence defline.

- `-T 8`: This specifies the number of threads to use. `8` means the program will run on 8 threads, enabling parallel computation for faster processing.

- `-n 5`: For protein sequences, this sets the word length for the initial match. `5` is typically used for thresholds between 0.7 and 0.8.

- `-aL 0.8`: This sets the alignment coverage for the longer sequence. `0.8` means 80% of the longer sequence must be covered in the alignment.

- `-s 0.95`: This sets the alignment coverage for the shorter sequence. `0.95` means 95% of the shorter sequence must be included in the alignment.

- `-uS 0.2`: This specifies the maximum unmatched percentage of the shorter sequence. `0.2` means up to 20% of the shorter sequence can be unmatched.

- `-sc 1`: This option, when set to `1`, sorts clusters by decreasing size.

- `-sf 1`: This option, when set to `1`, sorts fasta sequence by cluster size.

Each of these options tailors the behavior of CD-HIT to your specific requirements, influencing how sequences are clustered and how the output is formatted and organized. The use of shell variables (like `$x`) suggests that this command is part of a script where the value of `$x` is dynamically set, allowing for flexible application of the command with different parameters.

## Read the cd-hit Result as pandas dataframe

```python
import pandas as pd

# Initialize lists to store data
sequence_names = []
cluster_ids = []

# Open the .clstr file and parse it
with open('your_file.clstr', 'r') as file:
    current_cluster_id = None
    for line in file:
        if line.startswith('>Cluster '):
            current_cluster_id = line.split()[1]
        else:
            # Extracting sequence name
            parts = line.split()
            seq_name = parts[2].strip('>').split('...')[0]
            sequence_names.append(seq_name)
            cluster_ids.append(current_cluster_id)

# Create a DataFrame
df = pd.DataFrame({'Sequence Name': sequence_names, 'Cluster ID': cluster_ids})

# Display the DataFrame
print(df)
```

## Trouble Shooting

<pre>
Fatal Error:
Too low cluster threshold for the word length.
Increase the threshold or the tolerance, or decrease the word length.
Program halted !!
</pre>

The error message you're encountering, "Fatal Error: Too low cluster threshold for the word length. Increase the threshold or the tolerance, or decrease the word length. Program halted !!", indicates a conflict between the parameters you've set in CD-HIT, particularly relating to the sequence identity threshold and the word length.

In CD-HIT, the "word length" refers to the length of the initial exact match that the algorithm looks for when comparing sequences. The "cluster threshold" is the percentage similarity required for two sequences to be clustered together. When the cluster threshold is set too low relative to the word length, the program cannot effectively perform the initial sequence matching, leading to this error.

To resolve this issue, you can:

1. **Increase the Threshold**: Increase the sequence identity threshold (`-c` parameter). If it's currently very low, increasing it will make the clustering less stringent. For instance, if you have set `-c 0.6` (60% identity), try increasing it to 0.7 or higher.

2. **Decrease the Word Length**: Decrease the word length (`-n` parameter). A lower word length means the program will look for shorter exact matches in the initial step, which can be more tolerant of low similarity thresholds. However, be cautious, as too low a word length might make the process slower and less efficient.

3. **Adjust Tolerance**: If your dataset includes very diverse sequences and you need to maintain a low threshold, you might have to adjust other parameters to balance the sensitivity and specificity of the clustering.

Remember that the appropriate values for these parameters can vary depending on your specific dataset and the objectives of your analysis. It might require some experimentation to find the right balance for your needs.

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
