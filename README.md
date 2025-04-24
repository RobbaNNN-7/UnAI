# 🎓 University Information Retrieval Bot

An AI-powered chatbot assistant built to help students get accurate, document-backed information about **universities in Pakistan**. It leverages semantic search and LLMs to answer queries related to admissions, programs, faculty, campus life, and more — based on real university documents.
---

## ✅ Features

- 📄 PDF-based document ingestion and embedding
- 🔍 Semantic search using ChromaDB + HuggingFace embeddings
- 💬 LLM-based responses with grounded context
- 🧠 Metadata-aware document retrieval
- 🇵🇰 Built specifically for Pakistani universities and students

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **ChromaDB**
- **HuggingFace Embeddings**
- **PyPDFLoader**

---

## 🚀 How It Works

1. **Document Parsing**: University PDFs are loaded from the `Books/` directory. Metadata is stored in JSON files under `metadata/`.
2. **Vectorization**: Documents are embedded and stored in **ChromaDB** with metadata.
3. **Query Pipeline**:
   - User submits a query (e.g., "What is QAU's fee structure?")
   - System retrieves top matching documents
   - The context is passed to an LLM
   - A response is generated based on the actual content

---

## 🧪 Example Query

```bash
> Who is the rector of NUST?

> 🛠️ Currently supports:
> - National University of Sciences and Technology (NUST)
> - Lahore University of Management Sciences (LUMS)
> - Quaid-i-Azam University (QAU)

More universities will be added soon.
