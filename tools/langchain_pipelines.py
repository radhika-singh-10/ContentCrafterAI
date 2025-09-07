from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel
from config.settings import OPENAI_API_KEY, OPENAI_TEXT_MODEL, DEFAULT_TEMPERATURE

class PostDraft(BaseModel):
    platform: str
    text: str
    hashtags: list[str]
    image_brief: str
    cta: str

def build_writer_chain():
    llm = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model=OPENAI_TEXT_MODEL,
        temperature=DEFAULT_TEMPERATURE,
    )
    prompt = PromptTemplate(
        template=(
            "You are a brand-safe content writer.\n"
            "Brand rules:\n{brand_rules}\n\n"
            "Topic: {topic}\nAudience: {audience}\n"
            "Historical insights (from MemGPT): {lessons}\n\n"
            "Produce a JSON with keys [platform, text, hashtags, image_brief, cta]. "
            "Platform should be one of [linkedin, twitter, instagram]. "
            "Text must fit the chosen platform. Hashtags as a small list. "
            "Keep it on-brand and safe."
        ),
        input_variables=["brand_rules", "topic", "audience", "lessons"],
    )
    chain = prompt | llm | StrOutputParser()
    return chain

def build_refiner_chain():
    llm = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model=OPENAI_TEXT_MODEL,
        temperature=0.4,
    )
    prompt = PromptTemplate(
        template=(
            "Refine the following post JSON for clarity, brevity, and brand tone.\n"
            "Brand rules:\n{brand_rules}\n\n"
            "POST_JSON:\n{post_json}\n\n"
            "Return improved JSON only."
        ),
        input_variables=["brand_rules", "post_json"],
    )
    chain = prompt | llm | StrOutputParser()
    return chain

def parse_post_json(raw: str) -> PostDraft:
    import json
    data = json.loads(raw)
    return PostDraft(
        platform=data.get("platform", "linkedin"),
        text=data["text"],
        hashtags=data.get("hashtags", [])[:10],
        image_brief=data.get("image_brief", ""),
        cta=data.get("cta", "")
    )
