import torch  # allows Tensor computation with strong GPU acceleration
from transformers import pipeline  # fast way to use pre-trained models for inference


# define helper function
def get_completion_dolly(input):
    system = f"""
  You are an expert Physicist.
  You are good at explaining Physics concepts in simple words.
  Help as much as you can.
  """
    prompt = f"#### System: {system}\n#### User: \n{input}\n\n#### Response from Dolly-v2-3b:"
    print(prompt)
    dolly_response = dolly_pipeline(prompt, max_new_tokens=500)
    return dolly_response[0]["generated_text"]


if __name__ == "__main__":
    dolly_pipeline = dolly_pipeline = pipeline(
        model="databricks/dolly-v2-3b",
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
    )

    while True:
        # let's prompt
        prompt = input("prompt:>")
        # prompt = "Why is the Sky blue?"
        print(get_completion_dolly(prompt))
