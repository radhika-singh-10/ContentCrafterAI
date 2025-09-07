from typing import Optional
from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_IMAGE_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_image(image_brief: str, size: str = "1024x1024") -> Optional[str]:
    """
    Returns a URL (or base64) for the generated image.
    """
    if not image_brief:
        return None
    resp = client.images.generate(
        model=OPENAI_IMAGE_MODEL,
        prompt=image_brief,
        size=size,
        n=1,
    )
    # url variant
    return resp.data[0].url
