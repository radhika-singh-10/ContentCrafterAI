from langchain.agents import initialize_agent, Tool, AgentType
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFacePipeline
from generator.text_generator import generate_text
from generator.image_generator import generate_image

# Define Text Generation Tool
def text_generation_tool(input_topic):
    return generate_text(input_topic)

# Define Image Generation Tool
def image_generation_tool(input_topic):
    image = generate_image(input_topic)
    image_path = "generated_agent_image.png"
    image.save(image_path)
    return f"Image saved at {image_path}"

# Setup Tools for Agent
llm_pipeline = HuggingFacePipeline.from_model_id("mistralai/Mistral-7B-Instruct-v0.2")

tools = [
    Tool(
        name="ContentGenerator",
        func=text_generation_tool,
        description="Generates engaging text content for social media posts."
    ),
    Tool(
        name="ImageGenerator",
        func=image_generation_tool,
        description="Generates an illustrative image for the post."
    )
]

# Initialize LangChain Agent
agent = initialize_agent(
    tools=tools,
    llm=llm_pipeline,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Orchestrator Function
def orchestrate_content_generation(topic):
    task = f"Generate text and image content about: {topic}"
    return agent.run(task)
