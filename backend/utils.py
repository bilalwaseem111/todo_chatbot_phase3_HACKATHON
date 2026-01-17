import json
import os

def load_qa(path):
    # Convert relative path to absolute path
    abs_path = os.path.join(os.path.dirname(__file__), "..", path)
    with open(abs_path, "r", encoding="utf-8") as file:
        return json.load(file)

def find_answer(question, qa_list):
    question = question.lower()
    for item in qa_list:
        if item["question"].lower() in question:
            return item["answer"]
    return "Sorry, I don't have an answer for that."
