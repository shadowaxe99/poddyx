class Search:
    def __init__(self):
        self.feedback_data = []

    def add_feedback(self, feedback):
        self.feedback_data.append(feedback)

    def search_feedback(self, keyword):
        results = [feedback for feedback in self.feedback_data if keyword in feedback]
        return results
