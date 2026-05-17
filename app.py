from fastapi import FastAPI
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# FastAPI App
app = FastAPI(
    title="T5 Text Summarization API",
    description="A FastAPI application for generating concise summaries using a fine-tuned T5 transformer model.",
    version="1.0.0"
)

# Device (GPU or CPU)
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# Model Path
MODEL_PATH = "./model"

# Load Tokenizer
tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)

# Load Model
model = T5ForConditionalGeneration.from_pretrained(
    MODEL_PATH,
    ignore_mismatched_sizes=True
).to(device)

# Request Body
class TextRequest(BaseModel):
    text: str
    max_length: int = 20

# Home Endpoint
@app.get("/")
def home():
    return {
        "message": "T5 Summarization API is running successfully!"
    }

# Summarization Endpoint
@app.post("/summarize")
def summarize(request: TextRequest):

    input_text = "summarize: " + request.text

    inputs = tokenizer.encode(
        input_text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    ).to(device)

    summary_ids = model.generate(
        inputs,
        max_length=120,
        min_length=30,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )

    return {
        "summary": summary
    }