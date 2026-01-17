from utils import load_qa, find_answer

QA_PATH = "../data/qa.json"

class TodoChatBot:
    def __init__(self):
        self.qa_list = load_qa(QA_PATH)

    def get_response(self, user_message):
        return find_answer(user_message, self.qa_list)
