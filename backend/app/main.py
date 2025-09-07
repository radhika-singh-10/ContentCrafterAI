# ===============================
# File: backend/app/main.py
# ===============================
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uuid


# NOTE: make sure your project has these modules from your existing repo
# agentic_pipeline/autogen_content_pipeline.py
# tools/langchain_pipelines.py, tools/dalle_tool.py
# memory/memgpt_client.py, publisher/publisher.py
# If not, copy the versions we discussed earlier into the repo.
from agentic_pipeline.autogen_content_pipeline import Orchestrator


app = FastAPI(title="ContentCrafterAI Backend")


origins = [
"http://localhost:8501", # Streamlit
"http://127.0.0.1:8501",
"http://localhost:3000",
"http://127.0.0.1:3000",
]


app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)


orch = Orchestrator()


# Simple in-memory store for drafts
DRAFTS: Dict[str, Dict[str, Any]] = {}


class GenerateReq(BaseModel):
topic: str
audience: str


class PublishReq(BaseModel):
draft_id: str


@app.post("/api/generate")
def generate(req: GenerateReq):
try:
# Run writer + critic + designer only (no publish yet)
draft = orch.writer_agent(req.topic, req.audience)
orch.critic_agent({"text": draft["text"]})
image_url = orch.designer_agent(draft.get("image_brief", ""))
draft_id = str(uuid.uuid4())
DRAFTS[draft_id] = {
"topic": req.topic,
"audience": req.audience,
"draft": draft,
"image_url": image_url,
}
return {"draft_id": draft_id, "draft": draft, "image_url": image_url}
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/publish")
def publish(req: PublishReq):
return {"status": "ok"}
