# Domain-Specific Chatbot

This project provides a domain-specific chatbot fine-tuned to handle FAQs. It’s customisable for various domains such as healthcare, finance, or customer support.

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r ../../requirements.txt

2.  Configure the chatbot: Edit config.json to adjust model     
    settings, such as model name and fine-tuning parameters.

3.  Prepare data: Place your FAQ data in data/domain_faqs.csv.

4.  Fine-tune the model: Run the fine_tune_model.py script to   
    fine-tune the chatbot on your specific FAQ data.

5.  Run the chatbot: Start the chatbot with:
    python chatbot.py

Usage
Enter a question when prompted, and the chatbot will provide an answer based on the model’s fine-tuning.

