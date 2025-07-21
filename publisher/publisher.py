import uuid

class Publisher:
    def publish(self, text_content, image_content):
        post_id = str(uuid.uuid4())
        print(f"Publishing Post ID {post_id}...")
        print("Text Content:", text_content)
        image_content.save(f"{post_id}.png")
        print(f"Image saved as {post_id}.png")
        return post_id
