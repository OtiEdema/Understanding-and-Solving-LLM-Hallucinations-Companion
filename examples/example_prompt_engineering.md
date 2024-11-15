# Prompt Engineering Guide

This guide covers essential techniques in prompt engineering, enabling more accurate responses from LLMs by refining input prompts.

## Why Prompt Engineering?

Prompt engineering is a critical tool for guiding LLMs to produce desired outputs, especially important in applications where hallucinations must be minimised. By carefully crafting prompts, we can make model responses more reliable.

---

## Techniques

### 1. Be Specific and Clear
When crafting prompts, specificity is key. Avoid vague terms that could lead to ambiguous answers.

**Example**:
- **General Prompt**: "Tell me about renewable energy."
- **Specific Prompt**: "Explain how solar panels generate electricity and why they are considered renewable energy."

### 2. Provide Context
Adding context can help the model understand the purpose of the prompt.

**Example**:
- **Without Context**: "Describe neural networks."
- **With Context**: "In the context of deep learning, describe neural networks and their role in image classification."

### 3. Use Examples in Prompts
Provide examples in your prompt to guide the LLM on the format or style of the response.

**Example**:
```plaintext
"Here’s how a summary is structured: 'The main character embarks on an adventure...' Now, summarise this story in the same format."

Example Applications
Customer Support
"Answer this customer query as a customer support agent: 'How can I reset my password?'"

Research Assistance
"Summarise the key findings of this research paper in two sentences."

Use these techniques to improve the clarity and accuracy of model responses.


