import json
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load configuration
with open("config.json") as f:
    config = json.load(f)

tokenizer = AutoTokenizer.from_pretrained(config["model_name"])
model = AutoModelForCausalLM.from_pretrained(config["model_name"])

def generate_response(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=config["max_length"], temperature=config["temperature"])
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def hand_off_to_human(query):
    return "This query requires human intervention."

if __name__ == "__main__":
    print("Customer Support Assistant. Type 'exit' to quit.")
    while True:
        query = input("Customer: ")
        if query.lower() == "exit":
            break
        response = generate_response(query)
        print("Assistant:", response)
