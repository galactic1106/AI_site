import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def prompt_gpt_2(prompt):
    # Load pre-trained model and tokenizer
    model_name = "gpt2"  # You can choose from 'gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl'
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Set the model to evaluation mode
    model.eval()

    # Tokenize the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate text
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)

    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print('-'*40+'\nprompt: '+prompt)
    print('response: '+generated_text+'\n'+'-'*40)
    return generated_text
