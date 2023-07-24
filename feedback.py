class Feedback:
    def __init__(self):
        self.feedback_list = []

    def providing_feedback(self, feedback):
    # Add your logic here
    self.feedback_list.append(feedback)
    # Add your logic here
    return 'Feedback provided successfully.'
    # Add your logic here
    # Add your logic here
    self.feedback_list.append(feedback)
        # Add your logic here
        # Add your logic here
    return 'Feedback provided successfully.'
        # Add your logic here
        # Add your logic here
        self.feedback_list.append(feedback)
        return 'Feedback provided successfully.'

    def tagging_feedback(self, feedback, tag):
        for item in self.feedback_list:
            if item == feedback:
                item['tag'] = tag
        return 'Feedback tagged successfully.'

    def searching_feedback(self, keyword):
        search_results = [item for item in self.feedback_list if keyword in item['feedback']]
        return search_results
