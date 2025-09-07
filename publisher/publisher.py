from typing import Dict, Any
import textwrap

def format_for_platform(platform: str, text: str, hashtags: list[str], cta: str) -> Dict[str, Any]:
    if platform == "twitter":
        body = textwrap.shorten(text, width=270, placeholder="…")
        tag_str = " ".join(f"#{h}" for h in hashtags[:4])
        return {"platform":"twitter", "text": f"{body}\n{tag_str}\n{cta}".strip()}
    elif platform == "instagram":
        tag_str = " ".join(f"#{h}" for h in hashtags[:8])
        return {"platform":"instagram", "text": f"{text}\n\n{tag_str}\n{cta}".strip()}
    else: 
        tag_str = " ".join(f"#{h}" for h in hashtags[:8])
        return {"platform":"linkedin", "text": f"{text}\n\n{tag_str}\n{cta}".strip()}

def simulate_publish(payload: Dict[str, Any], image_url: str | None) -> Dict[str, Any]:
    """
    Stub for LinkedIn/Twitter/Instagram SDK posts.
    Returns a dummy post_id and fake metrics.
    """
    post_id = f"{payload['platform']}_post_{abs(hash(payload['text'])) % 10_000_000}"
    metrics = {"ctr": 0.042, "likes": 57, "comments": 6, "saves": 11}
    return {"post_id": post_id, "metrics": metrics, "image_url": image_url, "payload": payload}


'''

import uuid
import requests
import praw

class Publisher:
   
    def publish(self, text_content, image_content):
        post_id = str(uuid.uuid4())
        print(f"Publishing Post ID {post_id}...")
        print("Text Content:", text_content)
        image_content.save(f"{post_id}.png")
        print(f"Image saved as {post_id}.png")
        return post_id

    def publish_to_reddit(title, content, subreddit_name, reddit_config):
    reddit = praw.Reddit(
        client_id=reddit_config['client_id'],
        client_secret=reddit_config['client_secret'],
        user_agent=reddit_config['user_agent'],
        username=reddit_config['username'],
        password=reddit_config['password']
    )

    subreddit = reddit.subreddit(subreddit_name)
    post = subreddit.submit(title=title, selftext=content)
    print(f"Reddit post published: https://www.reddit.com{post.permalink}")
'''
