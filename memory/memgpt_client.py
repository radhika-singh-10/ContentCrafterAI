import json, os, time
from typing import List, Dict, Any
from config.settings import MEMGPT_STORE_PATH

class MemGPTClient:
    """
    Lightweight stand-in: stores lessons (topic, audience, features, engagement)
    and retrieves top-scoring summaries as 'lessons' to condition prompts.
    Replace with real MemGPT API if you use it.
    """
    def __init__(self, path: str = MEMGPT_STORE_PATH):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({"entries": []}, f)

    def _read(self) -> Dict[str, Any]:
        with open(self.path, "r") as f:
            return json.load(f)

    def _write(self, data: Dict[str, Any]):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def write_lesson(self, topic: str, audience: str, features: Dict[str, Any], engagement: Dict[str, float]):
        data = self._read()
        data["entries"].append({
            "ts": time.time(),
            "topic": topic,
            "audience": audience,
            "features": features,
            "engagement": engagement,
            "score": self._score(engagement)
        })
        self._write(data)

    def retrieve_lessons(self, topic: str, audience: str, k: int = 3) -> str:
        data = self._read()
        entries = data.get("entries", [])
        # naive similarity: same topic/audience + top by score
        filtered = [
            e for e in entries
            if e["topic"] == topic or e["audience"] == audience
        ]
        filtered.sort(key=lambda x: x.get("score", 0), reverse=True)
        return "; ".join(
            f"Lesson(ts={int(e['ts'])}): features={e['features']} -> engagement={e['engagement']}"
            for e in filtered[:k]
        )

    @staticmethod
    def _score(engagement: Dict[str, float]) -> float:
        # simple weighted CTR + saves + comments
        return (
            2.5 * engagement.get("ctr", 0.0) +
            1.5 * engagement.get("saves", 0.0) +
            1.0 * engagement.get("comments", 0.0) +
            0.5 * engagement.get("likes", 0.0)
        )
