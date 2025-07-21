from agents.content_generator import ContentGenerator
from agents.feedback_manager import FeedbackManager
from agents.rag_retriever import RAGRetriever
from publisher.publisher import Publisher
from storage.aws_s3_manager import S3Manager

def main():
    # Initialize modules
    content_generator = ContentGenerator(openai_api_key="YOUR_OPENAI_API_KEY")
    feedback_manager = FeedbackManager()
    rag_retriever = RAGRetriever(documents=["AI trends 2025", "Tips for content marketing", "User engagement strategies"])
    publisher = Publisher()
    s3_manager = S3Manager(bucket_name='your-s3-bucket-name')

    # RAG enrichment
    enrichment = rag_retriever.retrieve("latest marketing strategies")[0]

    # Generate content
    text = content_generator.generate_text(f"Write a post about {enrichment}")
    image = content_generator.generate_image(f"Generate an image about {enrichment}")

    # Publish content
    post_id = publisher.publish(text, image)
    image_file = f"{post_id}.png"
    s3_manager.upload_file(image_file, f"posts/{image_file}")

    # Simulate feedback update
    feedback_manager.update_feedback(post_id, {"likes": 10, "shares": 2, "comments": 1})

if __name__ == "__main__":
    main()
