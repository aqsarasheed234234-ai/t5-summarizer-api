# T5 Summarization API (FastAPI)

A FastAPI application for text summarization using a fine-tuned T5 transformer model.

✨ Built with T5 Transformer  
⚡ Powered by FastAPI  
🧠 Uses Hugging Face Transformers  
📁 Custom trained model integration 
---

# 📌 Features

- Fast and lightweight API using FastAPI
- Fine-tuned T5 model for text summarization
- Simple REST API endpoint
- Easy testing using Swagger UI
- CPU/GPU support (Torch)
- Clean and modular project structure

---

# 📡 API Endpoints

| Method | Endpoint      | Description              |
|--------|--------------|--------------------------|
| GET    | /            | Check API status        |
| POST   | /summarize   | Generate text summary   |
| GET    | /docs        | Swagger API testing UI  |

---
⚙️ Run Locally
# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

📁 Project Structure
.
├── app.py                  # FastAPI application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── model/
    ├── config.json
    ├── model.safetensors
    ├── tokenizer_config.json
    ├── special_tokens_map.json
    └── spiece.model

    🧠 Model Information

This project uses a fine-tuned T5 transformer model for text summarization.

Model Type: T5 (Text-to-Text Transfer Transformer)
Task: Abstractive Text Summarization
Framework: Hugging Face Transformers + PyTorch

    🧠 Training Notebook

Want to see how this model was trained?
You can explore and run the notebook for free on Kaggle:

📄 T5 Summarization Model
Kaggle Notebook
https://www.kaggle.com/code/aqsa234/t5-with-summarization/notebook

🤝 Learning Purpose
This project is designed to help you explore and practice modern AI development. You can modify the code, try new ideas, and build your own improvements on top of it. It is structured in a way that makes it easier to understand how NLP models, T5 transformers, FastAPI, and deployment workflows work together in real applications.
