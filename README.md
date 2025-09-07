# Directory Structure:

#### AgenticContentCreator/
```plaintext
├── agents/
│   ├── content_generator.py
│   ├── feedback_manager.py
│   └── rag_retriever.py
├── publisher/
│   └── publisher.py
├── storage/
│   └── aws_s3_manager.py
├── agentic_pipeline/
│   └── autogen_content_pipeline.py  
├── main.py
├── requirements.txt
```


# Agentic AI Content Generator using free LLM and Stable Diffusion.

In this project, I have built an Agentic AI-powered content creation ecosystem—essentially a self-improving system that automates generating, refining, and publishing social media content using multiple AI components. Here’s what’s happening step-by-step:

# Content Generation:

Microsoft Autogen + LangChain + LLMs + DALL·E + RAG:
These tools generate rich content (text + images). Autogen and LangChain coordinate different models (like LLMs for text, DALL·E for images) to create end-to-end posts.

# Content Publishing:

The system publishes this AI-generated content automatically across multiple social media platforms.

# Feedback Loop with MemGPT:

After publishing, MemGPT captures user interaction data (likes, comments, shares, engagement metrics).

This data is used to refine the content generation pipeline, effectively making your AI learn what content performs better and adapt future outputs.

# RAG (Retrieval-Augmented Generation):

You enrich content by pulling relevant, real-time information from external databases or APIs before generation, ensuring content is more contextually relevant or timely.

TensorFlow + AWS Deployment:

TensorFlow may be used for specific model serving or analytics tasks.

AWS handles deployment, scalability, and reliability, ensuring that your system can operate and scale in production environments.

In short, you’re automating the full content pipeline: generate → publish → analyze → refine, using multiple modern AI tools working together in an "agentic" (goal-driven, self-directed) manner.



- Content Generation: OpenAI LLM API + DALL·E API

- Feedback Loop: Simulated with MemGPT-like memory via local storage

- RAG Enrichment: Simple document retrieval using FAISS

- Publishing: Simulated (you can replace it with real API calls)

- Deployment: AWS S3 for storing content, Lambda trigger simulation



# Components:
- OpenAI GPT 5 Text Generation API
- DALLE 
- AUTOGEN
- LangChain
- MemGPT 
- AWS 


# Virtual Environment Creation
```bash
python -m venv .venv
```

# To Activate the Virtual Environment 
```bash
source .venv/bin/activate
```

# To Deactivate the Virtual Environment 
```bash
deactivate 
```

# Run Instructions:

```bash
pip freeze > requirements.txt
```

# Set Reddit API ACCESS TOKEN

- Go to https://www.reddit.com/settings/privacy, click on Third-party app authorizations under Advanced
- Under apps, click on 'create another app'
- Select script
- Add the following information - Name: AgenticAI Publisher, Type: Script, Redirect URI: http://localhost:8080
- Save Client ID and Secret


# Set Environmental Variables
```plaintext
Stores the environmental variables in the .env file in the same format.  
```


```bash
export OPENAI_API_KEY="your-openai-api-key"
```
```bash
export REDDIT_API_KEY = "your-reddit-api-key"
```

```bash
aws configure
```


# Run the simplified version

```bash 
python main.py
```

# Run AutoGen Multi-Agent Pipeline

```bash
cd agentic_pipeline
```
```bash
python autogen_content_pipeline.py
```
