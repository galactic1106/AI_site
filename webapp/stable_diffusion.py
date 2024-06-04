import torch
from diffusers import StableDiffusionPipeline

from PIL import Image


def image_grid(imgs, rows, cols):
    assert len(imgs) == rows * cols

    w, h = imgs[0].size
    grid = Image.new("RGB", size=(cols * w, rows * h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i % cols * w, i // cols * h))
    return grid


def prompt_stable_diffusion(prompt):

    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16
    )

    pipe = pipe.to("cuda")

    num_images = 3

    all_images = []
    for i in range(num_images):
        images = pipe(prompt, num_inference_steps=100).images
        all_images.extend(images)
    grid = image_grid(all_images, rows=1, cols=3)
    return grid
