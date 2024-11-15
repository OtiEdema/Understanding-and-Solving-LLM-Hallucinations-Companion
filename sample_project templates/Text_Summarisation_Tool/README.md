# Text Summarisation Tool

This tool uses a pre-trained language model to summarise long-form documents, such as news articles or research papers.

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r ../../requirements.txt

Configure settings: Edit config.json to adjust model parameters like summary length.

Prepare data: Place your long documents in data/sample_texts.txt.

Fine-tune the model (optional): Run the fine_tune_model.py script if you want to fine-tune the model on specific summarisation data.

Run the summarisation tool: Start the tool with:

python summarisation.py

Usage
Input a document or text, and the tool will output a summary based on the configuration settings.



