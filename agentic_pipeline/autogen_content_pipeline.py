import autogen
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize the Assistant Agent (e.g., content generator)
content_agent = autogen.AssistantAgent(
    name="ContentCreatorAgent",
    llm_config={"model": "gpt-4"},
)

# Initialize the Planner Agent (e.g., decides topics and goals)
planner_agent = autogen.AssistantAgent(
    name="ContentPlannerAgent",
    llm_config={"model": "gpt-4"},
)

# Define the User Proxy (triggers and manages tasks)
user_proxy = autogen.UserProxyAgent(
    name="UserProxy",
    code_execution_config=False  # Disable arbitrary code execution for safety
)

# Define the conversation flow
def task():
    # Planner decides a topic
    planner_agent.initiate_chat(
        recipient=content_agent,
        message="Plan today's post topic based on AI trends."
    )

    # Content Agent creates content based on planner's decision
    content_agent.initiate_chat(
        recipient=user_proxy,
        message="Here is the drafted post based on today's planned topic."
    )

# Run the task
user_proxy.initiate_chat(
    recipient=planner_agent,
    message="Begin planning and content generation for today.",
    task=task
)







'''
import autogen
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize the Assistant Agent (e.g., content generator)
content_agent = autogen.AssistantAgent(
    name="ContentCreatorAgent",
    llm_config={"model": "gpt-4"},
)

# Initialize the Planner Agent (e.g., decides topics and goals)
planner_agent = autogen.AssistantAgent(
    name="ContentPlannerAgent",
    llm_config={"model": "gpt-4"},
)

# Define the User Proxy (triggers and manages tasks)
user_proxy = autogen.UserProxyAgent(
    name="UserProxy",
    code_execution_config=False  # Disable arbitrary code execution for safety
)

# Define the conversation flow
def task():
    # Planner decides a topic
    planner_agent.initiate_chat(
        recipient=content_agent,
        message="Plan today's post topic based on AI trends."
    )

    # Content Agent creates content based on planner's decision
    content_agent.initiate_chat(
        recipient=user_proxy,
        message="Here is the drafted post based on today's planned topic."
    )

# Run the task
user_proxy.initiate_chat(
    recipient=planner_agent,
    message="Begin planning and content generation for today.",
    task=task
)
'''
