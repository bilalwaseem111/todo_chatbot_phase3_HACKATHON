import json

def load_qa(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def find_answer(user_input, qa_list):
    user_input = user_input.lower()
    for item in qa_list:
        if item["question"] in user_input:
            return item["answer"]
    return "Sorry, I don't understand that yet."
