# Customer Support Assistant

An assistant designed for handling customer support queries by answering FAQs and escalating complex questions.

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r ../../requirements.txt

2.  Configure settings: Edit config.json to customise response parameters.

3.  Prepare data: Place customer support FAQs in data/customer_support_faq.csv.

4.  Fine-tune the model (optional): Run fine_tune_model.py if you wish to fine-tune the assistant for your domain.

5.  Run the assistant: Start the assistant with:
 python assistant.py

 Usage
Enter a query, and the assistant will provide an answer or indicate if it requires human intervention.
