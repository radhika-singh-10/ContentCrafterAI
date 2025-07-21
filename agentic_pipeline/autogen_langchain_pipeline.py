import autogen
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import openai

# Ensure OpenAI API key is set
openai.api_key = "YOUR_OPENAI_API_KEY"

# --- LangChain Pipeline Function ---
def langchain_content_generator(topic):
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    prompt = PromptTemplate.from_template("Write a social media post about {topic}")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(topic)

# --- Define AutoGen Agent Using LangChain ---
content_agent = autogen.AssistantAgent(
    name="ContentAgentWithLangChain",
    llm_config={"model": "gpt-4"},
    code_execution_config=False
)

# Register LangChain Task Inside Agent
@content_agent.register_for_llm()
def handle_message_with_langchain(message, sender):
    topic = message["content"]
    post = langchain_content_generator(topic)
    return post

# --- Define Planner Agent ---
planner_agent = autogen.AssistantAgent(
    name="ContentPlannerAgent",
    llm_config={"model": "gpt-4"},
    code_execution_config=False
)

# --- Define User Proxy Agent ---
user_proxy = autogen.UserProxyAgent(
    name="UserProxy",
    code_execution_config=False
)

# --- Conversation Orchestration ---
def task():
    # Planner decides a topic
    planner_agent.initiate_chat(
        recipient=content_agent,
        message="Plan today's post topic based on AI trends."
    )

    # Content Agent generates content using LangChain pipeline
    content_agent.initiate_chat(
        recipient=user_proxy,
        message="Here is the drafted post based on today's planned topic."
    )

# Start Pipeline
user_proxy.initiate_chat(
    recipient=planner_agent,
    message="Begin planning and content generation for today.",
    task=task
)
