import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load model from current directory
tokenizer = AutoTokenizer.from_pretrained(".")
model = AutoModelForSequenceClassification.from_pretrained(".")

labels = ["World", "Sports", "Business", "Sci/Tech"]

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    prediction = torch.argmax(outputs.logits, dim=1).item()
    return labels[prediction]

interface = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text",
    title="News Topic Classifier (BERT)"
)

interface.launch()
