# Phase 3 — Robustness Under Strong Paraphrasing

## Objective

The goal of Phase 3 was to evaluate how different text similarity metrics behave when sentences are **strongly paraphrased** using a language model.
Unlike Phase 2, which introduced small lexical modifications such as synonym replacement, Phase 3 focuses on **structural paraphrasing** where both wording and sentence structure may change while preserving meaning.

---

## Method

A pretrained **T5-based paraphrasing model** was used to generate rewritten versions of academic abstracts.

For each original text:

1. A paraphrased version of the sentence was generated.
2. Similarity between the original and paraphrased text was measured using three metrics:

   * Jaccard similarity
   * TF-IDF cosine similarity
   * Sentence embedding similarity
3. Results were aggregated across multiple abstracts.

---

## Results

The experiments showed the following behavior:

* **Jaccard similarity decreased significantly** due to reduced word overlap.
* **TF-IDF similarity decreased moderately**, as many important topic words remained similar.
* **Sentence embedding similarity remained high**, indicating strong semantic robustness.

These results demonstrate that lexical similarity metrics struggle when text structure changes significantly, while semantic representations remain effective at capturing meaning.

---

## Conclusion

Phase 3 confirms that **semantic similarity models are far more robust to paraphrasing than surface-level similarity metrics**.

While word-overlap methods quickly fail when wording changes, embedding-based models can still detect similarity when the underlying meaning of the text remains the same.

This highlights the importance of semantic representations in modern NLP systems for tasks such as:

* plagiarism detection
* semantic search
* document similarity analysis
