---
toc: true
url: PLM
covercopy: © Karobben
priority: 10000
date: 2024-05-01 11:59:50
title: 'Pretrained Protein Language Model'
ytitle: 'Pretrained Protein Language Model'
description:'Pretrained Protein Language Model'
excerpt:'Pretrained Protein Language Model'
tags: []
category: []
cover: ""
thumbnail: ""
---

## Pretrained Protein Language Models

GitHub: [facebookresearch](https://github.com/facebookresearch/esm)
Paper: [Language models of protein sequences at the scale of evolution enable accurate structure prediction](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v1)

## EMS (Evolutionary Scale Modeling)

### Examples for using this more to embedding your sequences


```bash
# install it very quick
pip install esm
```

```python
import torch
import esm

# Load the pre-trained ESM model
model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
model.eval()  # Set the model to evaluation mode

# Get a batch converter to process input sequences
batch_converter = alphabet.get_batch_converter()
# Example input sequences
sequences = [
    ("seq1", "ACDEFGHIKLMNPQRSTVWY"),
    ("seq2", "QWERTYUIOPASDFGHPKL")
]

# Convert the sequences to the model's input format
batch_labels, batch_strs, batch_tokens = batch_converter(sequences)
with torch.no_grad():
    results = model(batch_tokens, repr_layers=[33])  # Choose which layers to represent
    embeddings = results["representations"][33]  # Access embeddings from the specified layer
print(embeddings.shape)  # Check the shape of the embeddings tensor

# Optionally, save embeddings for later use
torch.save(embeddings, "embeddings.pt")
```

<details><summary>why I want layer 33? how should I know which layer I should use?</summary>
The choice of layer 33 for embeddings in the ESM model by Meta AI is not arbitrary, but can depend on how different layers capture different levels of representation. Here's a guide on why a specific layer might be chosen and how you can decide which layer to use:

1. **Understanding Layer Representations:**

   - **Lower Layers:** In neural network models, lower layers tend to capture more basic features. For a protein model, these might relate to specific sequence motifs or short-range interactions.
   
   - **Middle Layers:** Middle layers often capture more complex patterns, like secondary structures or longer-range interactions.
   
   - **Higher Layers:** Higher layers generally capture more abstract and high-level features, such as overall structural motifs or global relationships within the protein sequence.

2. **ESM's Layer 33:**

   In ESM models, layer 33 is a common choice because it's one of the higher layers, and it tends to capture complex and abstract relationships within protein sequences. This makes it a suitable choice for embedding purposes, as it encapsulates a significant amount of semantic information.

3. **Selecting the Right Layer:**

   To determine the best layer for your needs, consider the following:

   - **Task-Specific Needs:** Depending on your application, you might require embeddings that reflect specific levels of detail.
       - For tasks like sequence similarity or clustering, higher layers might be appropriate, as they encapsulate global relationships.
       - For more granular tasks like motif identification or secondary structure prediction, middle or lower layers might be more suitable.
   
   - **Empirical Evaluation:** Try out different layers and evaluate how they perform on your specific tasks.
       - For example, you might measure clustering accuracy or other performance metrics to compare the effectiveness of different layers.
   
   - **Visual Inspection:** If feasible, consider using visualization techniques (e.g., PCA, t-SNE) to observe how embeddings from different layers group or separate, giving insights into the information they capture.

4. **Practical Tips:**

   - **Start with Higher Layers:** Initially, you can start with higher layers, such as layer 33, to get an overview of abstract relationships captured.
   
   - **Iterate and Refine:** Once you identify which layers work well, refine your selection by experimenting with layers in that vicinity.
   
   - **Combine Information:** If necessary, consider combining embeddings from multiple layers, or integrating them into a deeper model that learns to utilize multiple representations.

By following this approach, you can identify which layer of the ESM model provides embeddings that best suit your specific task or project.
</details>

### More other infor

#### Results Example

<pre>

</pre>


1. **Logits:**

   The `logits` in the `results` dictionary refer to the raw, unnormalized output values from the model. In the context of ESM and other transformer models:

   - **Token-Level Predictions:** Logits may represent predictions at each token (amino acid) level. For instance, they might indicate the model's confidence for predicting specific classes (e.g., amino acid types, functional properties) for each token in the input sequence.
   - **Further Processing:** These logits can be processed by applying functions such as softmax or sigmoid to convert them into probabilities, making them suitable for downstream tasks like classification or probabilistic analysis.

2. **Contacts:**

   The `contacts` in the `results` dictionary pertain to contact maps predicted by the model:

   - **Contact Maps:** These matrices indicate the likelihood of residue-residue contacts or interactions within the protein sequence. Contact maps are typically symmetric, where the entry (i, j) shows the probability of a contact or interaction between residues at positions i and j.
   - **Usage in Protein Folding:** Contact maps are useful in protein folding studies, structural biology, and modeling, as they provide insights into the protein's 3D structure based on residue interactions.

3. **Integrating Components:**

   Depending on your specific needs, you can integrate or use these components in various ways:

   - **Logits:** Convert logits to probabilities for tasks such as sequence classification or functional annotation.
   - **Contacts:** Use contact maps to guide structural modeling or analyze the protein's residue interactions.

4. **Visualization and Analysis:**

   If needed, you can also visualize these components:

   - **Contact Maps:** Display contact maps using heatmaps for a visual representation of residue interactions.
   - **Logits:** Plot logits or probability distributions for insights into the model's predictive confidence.

By understanding these components, you can leverage the full range of the ESM model's output, applying it effectively to protein analysis, structural biology, and beyond. If you need further assistance or clarification, feel free to ask!

#### Attention Matrix 

<pre>
torch.Size([12, 33, 20, 471, 471])
</pre>

The attention matrices from transformer-based models, including Meta AI's ESM model, have multiple dimensions because they capture relationships between various aspects of the input sequences. Let's break down the dimensions in `torch.Size([12, 33, 20, 471, 471])`:

1. **Batch Size (12):**
   The first dimension corresponds to the batch size, representing the number of input sequences fed into the model.

2. **Layers (33):**
   The second dimension corresponds to the number of layers in the model. The ESM model is a transformer-based model with multiple layers, each producing its own attention matrix.

3. **Heads (20):**
   The third dimension corresponds to the number of attention heads in each layer. In transformer models:
   - **Multi-Headed Attention:** Each layer consists of multiple attention heads (20 in this case), allowing for different aspects of the input sequence to be attended to in parallel.
   - **Parallel Processing:** Each head computes an attention matrix that represents relationships between tokens in the sequence, providing diverse and independent perspectives.

4. **Sequence Length (471):**
   The fourth and fifth dimensions correspond to the sequence length, representing the number of tokens (amino acids) in the input sequence. Since this model processes sequences of length 471:
   - **Attention Matrix:** Each attention matrix is a square matrix of size \(471 \times 471\), indicating the relationships between all pairs of tokens (residues) in the sequence.
   - **Token Pair Relationships:** The entry (i, j) in this matrix indicates how much token i attends to token j, which can represent relationships or interactions between residues.

### Summary of the Attention Matrix:

- **Multiple Heads:** Multi-headed attention provides various perspectives on relationships between tokens.
- **Square Matrices:** Each head's attention matrix represents relationships between all pairs of tokens, resulting in a \(471 \times 471\) matrix.
- **Layers and Parallelism:** With multiple layers and heads, the model captures diverse and nuanced relationships, making it useful for complex tasks like protein analysis.

If you need further clarification or assistance with managing or using these attention matrices, feel free to ask!

## AntiBERTy

GitHub: [jeffreyruffolo/AntiBERTy](https://github.com/jeffreyruffolo/AntiBERTy)
Publications: [Deciphering antibody affinity maturation with language models and weakly supervised learning](https://arxiv.org/abs/2112.07782)

It was an antibody-specific transformer language model pre-trained on 558M natural antibody sequences.

- Does it trained light chain/ heavy chain separately?
- Does it includes the antibody across species and cell types?


### Quick guide to achieving the embedding and attention results

```bash
# install
pip install antiberty
```

```python
from antiberty import AntiBERTyRunner

antiberty = AntiBERTyRunner()
sequences = [
    "EVQLVQSGPEVKKPGTSVKVSCKASGFTFMSSAVQWVRQARGQRLEWIGWIVIGSGNTNYAQKFQERVTITRDMSTSTAYMELSSLRSEDTAVYYCAAPYCSSISCNDGFDIWGQGTMVTVS",
    "DVVMTQTPFSLPVSLGDQASISCRSSQSLVHSNGNTYLHWYLQKPGQSPKLLIYKVSNRFSGVPDRFSGSGSGTDFTLKISRVEAEDLGVYFCSQSTHVPYTFGGGTKLEIK",
]
embeddings, attentions = antiberty.embed(sequences, return_attention=True)
```


---- 

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
