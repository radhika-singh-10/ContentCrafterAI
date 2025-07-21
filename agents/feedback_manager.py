import json
import os

class FeedbackManager:
    def __init__(self, feedback_file='feedback.json'):
        self.feedback_file = feedback_file
        if not os.path.exists(self.feedback_file):
            with open(self.feedback_file, 'w') as f:
                json.dump({}, f)

    def update_feedback(self, post_id, interactions):
        with open(self.feedback_file, 'r+') as f:
            data = json.load(f)
            data[post_id] = interactions
            f.seek(0)
            json.dump(data, f, indent=4)

    def get_feedback(self):
        with open(self.feedback_file, 'r') as f:
            return json.load(f)
