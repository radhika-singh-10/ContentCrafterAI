from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
import torch

# Load model
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.2",
    torch_dtype=torch.float16,
    device_map="auto"
)
text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=512, temperature=0.7)
llm = HuggingFacePipeline(pipeline=text_generator)

# Prompt
template = PromptTemplate.from_template("""You are a social media content creator. Generate a short, engaging post about: {topic}""")

def generate_text(topic):
    prompt = template.format(topic=topic)
    return llm(prompt)