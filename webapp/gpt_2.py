import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def prompt_gpt_2(prompt):
    print("-"*40+" GPT-2 "+"-"*40)
    # Load pre-trained model and tokenizer
    model_name = "microsoft/DialoGPT-medium"  # You can also use 'DialoGPT-small' or 'DialoGPT-large'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Set the model to evaluation mode
    model.eval()

    # Tokenize the input prompt
    input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")

    # Generate a response
    with torch.no_grad():
        output_ids = model.generate(
            input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id
        )

    # Decode the generated response
    response = tokenizer.decode(
        output_ids[:, input_ids.shape[-1] :][0], skip_special_tokens=True
    )
    print("-" * 40 + "\nprompt: " + prompt)
    print("response: " + response + "\n" + "-" * 40)
    return response
