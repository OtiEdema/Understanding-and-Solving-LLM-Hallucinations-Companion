# Fine-Tuning Guide

Fine-tuning allows us to tailor a pre-trained model to a specific domain, increasing its accuracy for specialised tasks.

## Why Fine-Tune?

Fine-tuning adjusts a pre-trained model’s weights based on new data, improving performance on specific tasks. This is especially useful for applications requiring domain-specific knowledge.

---

## Steps for Fine-Tuning an LLM

### 1. Prepare Your Data
Your data should be relevant to the domain and task. Save data in a CSV file with columns for input prompts and target responses.

**Example Data**:
```csv
prompt,response
"What is the minimum balance requirement?", "The minimum balance is $500."
"How do I apply for a loan?", "You can apply by visiting our website and filling out the loan form."

2. Load and Tokenise Data
Use transformers to load your dataset and tokenise it.

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt-neo-125M")
inputs = tokenizer(list(data['prompt']), return_tensors="pt", padding=True, truncation=True)
outputs = tokenizer(list(data['response']), return_tensors="pt", padding=True, truncation=True)

3. Set Up and Train the Model
Set up training arguments and train the model on your dataset.

from transformers import Trainer, TrainingArguments, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("gpt-neo-125M")
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=2,
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

trainer.train()

Testing the Fine-Tuned Model
Once fine-tuning is complete, test your model by inputting relevant prompts to check the responses.