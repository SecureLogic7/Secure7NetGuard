# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Carregar o modelo e o tokenizador
model_path = "/home/neo/Mistral-7B-v0.1"  # Substitua pelo caminho real do seu modelo
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", torch_dtype=torch.float16)

# Função para gerar texto
def generate_text(prompt, max_length=50):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    outputs = model.generate(inputs.input_ids, max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Exemplo de uso para gerar código em JavaScript
prompt = "function greet(name) {\n return 'Hello, ' + name;\n}"
generated_text = generate_text(prompt)
print(generated_text)
