import json
import pandas as pd
from transformers import BartForConditionalGeneration, BartTokenizer, Trainer, TrainingArguments
import torch

# Load configuration
with open("config.json") as f:
    config = json.load(f)

# Load data
data = pd.read_csv("data/sample_texts.csv")

tokenizer = BartTokenizer.from_pretrained(config["model_name"])
model = BartForConditionalGeneration.from_pretrained(config["model_name"])

# Prepare dataset
inputs = tokenizer(list(data['document']), return_tensors="pt", padding=True, truncation=True)
outputs = tokenizer(list(data['summary']), return_tensors="pt", padding=True, truncation=True)
dataset = torch.utils.data.TensorDataset(inputs["input_ids"], outputs["input_ids"])

# Fine-tune model
training_args = TrainingArguments(output_dir="./results", num_train_epochs=3)
trainer = Trainer(model=model, args=training_args, train_dataset=dataset)
trainer.train()
model.save_pretrained("./fine_tuned_model")
