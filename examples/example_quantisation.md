
# Quantisation Guide

Quantisation is a technique to reduce model size by lowering the precision of weights, making LLMs more memory-efficient.

## Why Quantise?

Quantisation is beneficial when deploying models on resource-constrained environments, as it reduces the memory footprint without significantly sacrificing accuracy.

---

## Steps for Quantising an LLM

### 1. Load and Prepare the Model
Load your model as usual.

```python
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("gpt-neo-125M")

2. Apply Quantisation
Use PyTorch’s dynamic quantisation for an 8-bit model.

import torch

quantized_model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)

3. Save the Quantised Model
Save the quantised model to a new directory.

quantized_model.save_pretrained("./quantized_model")

Testing the Quantised Model
Load and test the quantised model to ensure accuracy.

loaded_quantized_model = AutoModelForCausalLM.from_pretrained("./quantized_model")

Quantisation is complete! You now have a memory-efficient model suitable for deployment in constrained environments.
