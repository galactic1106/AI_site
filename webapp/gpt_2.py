from aitextgen import aitextgen
from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU

def flag_gpt_2():

    file_name = "testoAI.txt"
    print(file_name)

    ai = aitextgen()

    tokenizer_file = "aitextgen.tokenizer.json"
    train_tokenizer(file_name)

    config = GPT2ConfigCPU()

    ai = aitextgen(tokenizer_file=tokenizer_file, config=config)
    data = TokenDataset(file_name, tokenizer_file=tokenizer_file, block_size=64)
    ai.train(data, batch_size=8, num_steps=30000, generate_every=3000, save_every=3000)
    return ai

def prompt_gpt_2(ai, prompt):
    return ai.generate(n=1, prompt=prompt,min_length=1000, max_length=2000)
