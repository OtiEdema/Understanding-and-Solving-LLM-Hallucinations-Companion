import json
from transformers import BartForConditionalGeneration, BartTokenizer

# Load configuration
with open("config.json") as f:
    config = json.load(f)

# Load model and tokenizer
tokenizer = BartTokenizer.from_pretrained(config["model_name"])
model = BartForConditionalGeneration.from_pretrained(config["model_name"])

def generate_summary(text):
    inputs = tokenizer([text], return_tensors="pt")
    summary_ids = model.generate(inputs["input_ids"], max_length=config["max_length"], min_length=config["min_length"], temperature=config["temperature"])
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    print("Text Summarisation Tool. Type 'exit' to quit.")
    while True:
        user_input = input("Document: ")
        if user_input.lower() == "exit":
            break
        summary = generate_summary(user_input)
        print("Summary:", summary)
