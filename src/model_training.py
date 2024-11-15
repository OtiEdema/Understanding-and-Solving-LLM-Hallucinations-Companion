from transformers import Trainer, TrainingArguments, AutoModelForCausalLM, AutoTokenizer

def train_model(data_path, model_name="gpt-neo-125M"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    data = preprocess_text_data(data_path)
    inputs = tokenizer(list(data['text']), return_tensors="pt", padding=True, truncation=True)

    training_args = TrainingArguments(output_dir="./results", num_train_epochs=3, per_device_train_batch_size=2)
    trainer = Trainer(model=model, args=training_args, train_dataset=inputs)
    trainer.train()
