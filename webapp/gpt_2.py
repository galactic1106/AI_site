import torch
from pytorch_pretrained_bert import GPT2Tokenizer, GPT2Model, GPT2LMHeadModel

import argparse
import logging
from tqdm import trange

import torch
import torch.nn.functional as F
import numpy as np

# Load pre-trained model tokenizer (vocabulary)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

model = GPT2LMHeadModel.from_pretrained("gpt2")

model.eval()
model.cuda()


def top_k_logits(logits, k):
    """
    Masks everything but the k top entries as -infinity (1e10).
    Used to mask logits such that e^-infinity -> 0 won't contribute to the
    sum of the denominator.
    """
    if k == 0:
        return logits
    else:
        values = torch.topk(logits, k)[0]
        batch_mins = values[:, -1].view(-1, 1).expand_as(logits)
        return torch.where(logits < batch_mins, torch.ones_like(logits) * -1e10, logits)


def sample_sequence(
    model,
    length,
    start_token=None,
    batch_size=None,
    context=None,
    temperature=1,
    top_k=0,
    device="cuda",
    sample=True,
):
    if start_token is None:
        assert context is not None, "Specify exactly one of start_token and context!"
        context = (
            torch.tensor(context, device=device, dtype=torch.long)
            .unsqueeze(0)
            .repeat(batch_size, 1)
        )
    else:
        assert context is None, "Specify exactly one of start_token and context!"
        context = torch.full(
            (batch_size, 1), start_token, device=device, dtype=torch.long
        )
    prev = context
    output = context
    past = None
    with torch.no_grad():
        for i in trange(length):
            logits, past = model(prev, past=past)
            logits = logits[:, -1, :] / temperature
            logits = top_k_logits(logits, k=top_k)
            log_probs = F.softmax(logits, dim=-1)
            if sample:
                prev = torch.multinomial(log_probs, num_samples=1)
            else:
                _, prev = torch.topk(log_probs, k=1, dim=-1)
            output = torch.cat((output, prev), dim=1)
    return output


def prompt_gpt_2(prompt):
    sequence_length = 100
    number_of_samples = 1

    context_tokens = []
    raw_text = prompt

    while not raw_text:
        print("Prompt should not be empty!")
        return ''

    context_tokens = tokenizer.encode(raw_text)
    generated = 0

    results=[]
    for _ in range(number_of_samples):
        out = sample_sequence(
            model=model, length=sequence_length, context=context_tokens, batch_size=512
        )
        out = out[:, len(context_tokens) :].tolist()
        for i in range(512):
            generated += 1
            text = tokenizer.decode(out[i])
            print("=" * 40 + " SAMPLE " + str(generated) + " " + "=" * 40)
            print(text)
            print("\n\n" + "=" * 80)
            results.append(text)

    return results[0]
