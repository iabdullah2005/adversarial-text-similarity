## Phase 2 — Robustness Under Lexical Perturbation

Phase 2 investigates how different text similarity metrics behave when academic text is modified while attempting to preserve its original meaning.

A perturbation pipeline was developed to generate modified versions of research abstracts. The transformations included **part-of-speech aware synonym replacement** and **sentence reordering**, which introduce lexical changes without intentionally altering the semantic content of the text.

Experiments were conducted on multiple abstracts from the dataset using several perturbation strengths (replacement ratios between 0.05 and 0.25). For each modified text, similarity with the original document was measured using three approaches:

* **Jaccard similarity** (surface n-gram overlap)
* **TF-IDF cosine similarity** (lexical similarity)
* **Sentence embedding similarity** (semantic similarity)

The results were aggregated across many abstracts to produce robustness curves showing how similarity scores change as perturbation increases.

### Key Observations

* **Jaccard similarity decreases rapidly** as lexical changes increase because it relies on exact phrase overlap.
* **TF-IDF similarity remains relatively stable**, indicating that moderate synonym replacement does not significantly affect weighted vocabulary representations.
* **Embedding similarity remains highly robust**, showing that semantic representations preserve meaning even when wording changes.

### Conclusion

The experiments demonstrate that **surface-level similarity metrics are much more sensitive to lexical perturbations**, while **semantic similarity methods remain stable when meaning is preserved**. This highlights the importance of semantic representations in systems designed to detect document similarity.
