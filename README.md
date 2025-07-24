# 🧠 Text Summarization using Transformers (Day 54 of #60DaysOfDevOps)

This project demonstrates **abstractive text summarization** using a pre-trained Transformer model from the Hugging Face library. We use the `distilbart-cnn-12-6` model to summarize long pieces of text into concise and meaningful summaries.

---

## 📌 What is Text Summarization?

Text summarization is an NLP task that shortens large bodies of text while preserving the core meaning. There are two main types:

- **Extractive**: Picks key sentences directly from the text.
- **Abstractive**: Generates a new version of the summary using natural language generation.

This project uses **abstractive summarization** with a transformer model.

---

## 🚀 Technologies Used

- Python 🐍
- HuggingFace Transformers 🤗
- PyTorch (via `transformers` backend)
- Pretrained Model: `distilbart-cnn-12-6`

---

## 🛠️ Installation
pip install transformers torch

## Run
python summerizer.py
