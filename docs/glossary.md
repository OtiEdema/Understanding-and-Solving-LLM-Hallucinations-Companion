# Glossary of Key Terms in Large Language Models (LLMs)

This glossary covers essential terms and concepts in the realm of LLMs, transformers, and natural language processing.

### Attention Mechanism
The attention mechanism allows models to focus on relevant parts of the input sequence, assigning weights to each word or token. This enables the model to handle long sequences and capture context effectively, making it crucial in tasks like translation and summarisation.

### Bias
In the context of AI, bias refers to the tendency of a model to make predictions based on unfair or skewed representations, often due to imbalanced or unrepresentative training data. Mitigating bias is critical for ensuring ethical and fair AI applications.

### Decoder
In the transformer model architecture, the decoder is responsible for generating output sequences. For tasks like translation or text generation, the decoder takes encoded representations and turns them into human-readable text.

### Encoder
The encoder in a transformer model processes the input data by converting it into a dense representation that captures contextual relationships. For example, in a summarisation task, the encoder breaks down the input document into meaningful representations.

### Fine-Tuning
Fine-tuning is the process of training a pre-trained model on domain-specific data to improve its performance for specific tasks, such as generating legal summaries or handling medical FAQs. Fine-tuning typically uses a smaller, targeted dataset and fewer epochs than initial model training.

### Hallucination
Hallucination in LLMs refers to the generation of incorrect or fabricated information that seems plausible but is factually inaccurate. Hallucinations can be problematic in fields where accuracy is critical, such as healthcare and finance.

### LLM (Large Language Model)
Large Language Models are advanced neural network models with billions of parameters, trained on extensive text data to perform language-related tasks. Examples include OpenAI’s GPT series and Google’s BERT.

### Perplexity
Perplexity is an evaluation metric used in language modelling, measuring how confidently the model predicts the next word in a sequence. Lower perplexity indicates better performance.

### Prompt Engineering
Prompt engineering involves designing input prompts that guide LLMs to produce more accurate or relevant responses. This is especially useful in reducing model hallucinations and improving reliability.

### Quantisation
Quantisation reduces a model’s size by lowering the precision of its weights, often from 32-bit to 8-bit. This makes the model more memory-efficient and suitable for deployment in constrained environments, with minimal impact on accuracy.

### Transformer Model
A transformer is a deep learning model architecture that relies on self-attention mechanisms to process sequences of data. Transformers are foundational to LLMs and are known for handling long-range dependencies in text data.
