import json
import os

def load_qa(path):
    project_root = os.path.dirname(os.path.dirname(__file__))  # backend/.. = project root
    abs_path = os.path.join(project_root, path)

    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"QA file not found at {abs_path}")

    with open(abs_path, "r", encoding="utf-8") as file:
        return json.load(file)

def find_answer(question, qa_list):
    question = question.lower()
    for item in qa_list:
        if item["question"].lower() in question:
            return item["answer"]
    return "Sorry, I don't have an answer for that."
