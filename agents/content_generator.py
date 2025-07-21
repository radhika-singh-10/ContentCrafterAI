import openai
import torch
from PIL import Image
import requests
from io import BytesIO

class ContentGenerator:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def generate_text(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

    def generate_image(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        image = Image.open(BytesIO(requests.get(image_url).content))
        return image
