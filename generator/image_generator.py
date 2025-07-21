from diffusers import StableDiffusionPipeline
import torch

# Load Stable Diffusion
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("cuda")

def generate_image(prompt):
    return pipe(prompt).images[0]