
## ✨ t5-summarizer-api

This project provides a fine-tuned T5 Transformer model for automatic text summarization using a FastAPI backend.

---

## 🤖 Model Details

- **Model Type:** T5 (Text-to-Text Transfer Transformer)
- **Task:** Text Summarization
- **Framework:** Hugging Face Transformers
- **Backend:** FastAPI

---

## ✨ Features

- 📄 Accurate text summarization using T5 model  
- ⚡ Fast and lightweight API  
- 🔐 Secure API key authentication  
- 🐳 Docker-ready deployment  
- 📡 RESTful API integration  
- 📘 Auto-generated API docs at `/docs`

---

## 📡 API Endpoints

| Method | Endpoint      | Description           |
|--------|--------------|-----------------------|
| POST   | /summarize   | Summarize input text  |
| POST   | /generate    | Generate text         |
| GET    | /docs        | API documentation     |

---

## ⚙️ Run Locally

```

# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

```
---

## 📁 Project Structure


```
.
├── main.py # FastAPI application
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files
├── README.md # Project documentation
└── models/
├── config.json
├── model.safetensors
├── tokenizer_config.json
├── special_tokens_map.json
└── spiece.model
```
---


## 🧠 Training Notebook


- 📄 **T5 Summarization Notebook**
https://www.kaggle.com/code/aqsa234/t5-with-summarization

---


## 🤝 Contributing


This project is designed for easy exploration. Feel free to fork it, modify it, and experiment freely. There’s no need to start from scratch — the structure is already in place to help you learn efficiently.

