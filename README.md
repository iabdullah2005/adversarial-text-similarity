# Adversarial Robustness of Text Similarity Systems

This project explores how robust common **text similarity methods** are when academic text is modified while attempting to preserve its original meaning.

Many real-world systems—such as **plagiarism detection tools, document retrieval systems, and semantic search engines**—rely on similarity metrics like **TF-IDF**, **n-gram overlap**, or **semantic embeddings**.
The goal of this project is to experimentally evaluate how these systems behave when text undergoes controlled lexical perturbations.

---

# Project Goals

The primary objective of this project is to understand how different similarity metrics respond to changes in text wording and structure.

Key questions addressed include:

* How sensitive are similarity systems to lexical modifications?
* Which similarity metrics are most robust to paraphrasing?
* How much textual modification can occur while preserving semantic meaning?

---

# Implemented Similarity Methods

The project evaluates three commonly used similarity approaches.

### 1. Jaccard Similarity

Measures overlap between documents using **n-grams**.
This metric captures **surface-level similarity** and is highly sensitive to wording changes.

### 2. TF-IDF Cosine Similarity

Represents documents as **TF-IDF vectors** and computes similarity using cosine distance.
This method captures **lexical similarity** and is more robust than simple n-gram overlap.

### 3. Sentence Embedding Similarity

Uses **sentence embeddings** to represent the semantic meaning of text and compares documents using cosine similarity.
This approach focuses on **semantic similarity rather than exact word matching**.

---

# Phase 1 — Baseline Similarity System

Phase 1 implemented and validated the three similarity models:

* Jaccard similarity
* TF-IDF cosine similarity
* Sentence embedding similarity

Baseline experiments confirmed expected behavior:

* Identical texts produce similarity scores close to **1.0**
* Unrelated texts produce **low similarity scores**

This phase established a reliable framework for measuring document similarity.

---

# Phase 2 — Robustness Under Lexical Perturbation

Phase 2 examines how similarity metrics behave when text is modified while preserving its meaning.

A perturbation pipeline was implemented to generate modified versions of academic abstracts using:

* **POS-aware synonym replacement**
* **Sentence reordering**

These transformations introduce lexical variation while attempting to keep the semantic content intact.

Experiments were conducted across multiple abstracts with varying perturbation strengths.

---


# Key Observations

Experimental results reveal several important trends:

* **Jaccard similarity decreases rapidly** when wording changes, reflecting its sensitivity to surface-level variations.
* **TF-IDF similarity remains relatively stable** under moderate synonym replacement.
* **Sentence embedding similarity remains highly robust**, indicating that semantic representations effectively preserve meaning.

These findings highlight the difference between **surface-level similarity metrics** and **semantic similarity models**.

---

# Phase 3 — Robustness Under Strong Paraphrasing

Phase 3 extends the robustness analysis by introducing **strong paraphrasing transformations** generated using a pretrained language model.
Unlike Phase 2, where lexical changes were created through synonym replacement and sentence reordering, Phase 3 focuses on **structural and semantic paraphrasing** that significantly alters wording and sentence structure while preserving meaning.

To generate paraphrased text, a pretrained **T5-based paraphrasing model** was used. The model rewrites sentences by introducing new vocabulary, modifying grammatical structure, and reorganizing sentence patterns while maintaining the original semantic intent.

Example transformation:

Original sentence

> The model predicts accurate results for complex tasks.

Paraphrased sentence

> The system produces precise outcomes even for challenging problems.

Although the wording and structure differ considerably, the semantic meaning remains similar.

---

## Experimental Procedure

For each abstract in the dataset:

1. The original text was selected.
2. A paraphrased version was generated using the pretrained paraphrasing model.
3. Similarity between the original and paraphrased texts was measured using the three similarity methods developed in earlier phases:

   * **Jaccard similarity**
   * **TF-IDF cosine similarity**
   * **Sentence embedding similarity**

These experiments were repeated across multiple abstracts to obtain average similarity values.

---

## Key Observations

The experiments revealed a clear pattern:

* **Jaccard similarity decreased significantly**, reflecting its reliance on exact word overlap.
* **TF-IDF similarity decreased moderately**, as many important topic words remained similar despite structural changes.
* **Sentence embedding similarity remained high**, indicating that semantic representations effectively capture the underlying meaning of the text.

---

## Conclusion

The results confirm that **surface-level similarity metrics struggle with strong paraphrasing**, while **semantic embedding models remain highly robust** when the meaning of the text is preserved.

This demonstrates the importance of semantic representations in modern NLP systems designed for document comparison, semantic search, and paraphrase detection.

Phase 3 therefore highlights the limitations of traditional lexical similarity metrics and reinforces the role of **semantic similarity models in robust text comparison systems**.


# Repository Structure

```
data/           Processed dataset samples
notebooks/      Experimental notebooks
src/            Similarity model implementations
results/        Experiment outputs and plots
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Sentence Transformers
* Matplotlib

---

# Future Work

Planned extensions of this project include:

* Structural paraphrasing experiments
* Evaluation on larger datasets
* Development of hybrid similarity detection models
* Analysis of adversarial paraphrasing techniques

---

# Research Motivation

Understanding the robustness of similarity systems is critical for applications such as:

* plagiarism detection
* document retrieval
* academic integrity systems
* semantic search engines

This project investigates how these systems respond to controlled textual modifications and evaluates their resilience to adversarial perturbations.

---



# License

This project is released under the **MIT License**.
