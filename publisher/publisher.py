import uuid
import requests
import praw

class Publisher:
'''    
    def publish(self, text_content, image_content):
        post_id = str(uuid.uuid4())
        print(f"Publishing Post ID {post_id}...")
        print("Text Content:", text_content)
        image_content.save(f"{post_id}.png")
        print(f"Image saved as {post_id}.png")
        return post_id
'''
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
