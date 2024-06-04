from difflib import restore
from aitextgen import aitextgen
from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU
import os

os.environ['USER'] = 'Modified User'

def init_gpt_2():
    file_name = "./webapp/static/train_text/Answer.csv"
    ai = aitextgen()

    tokenizer_file = "aitextgen.tokenizer.json"
    train_tokenizer(file_name)

    config = GPT2ConfigCPU()

    ai = aitextgen(tokenizer_file=tokenizer_file, config=config)
    data = TokenDataset(file_name, tokenizer_file=tokenizer_file, block_size=64)
    ai.train(data, batch_size=8, num_steps=30000, generate_every=3000, save_every=3000)
    return ai


def prompt_gpt_2(ai, prompt):
    print('prompt:'+ prompt)
    response=ai.generate(n=1, prompt=input( ),min_length=1000, max_length=2000)
    print('response:'+ response)
    return response
