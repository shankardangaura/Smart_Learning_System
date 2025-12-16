from flask import Blueprint, request, jsonify
import random

quiz_bp = Blueprint('quiz', __name__)

# Sample quiz questions
questions = [
    {
        "question": "What is the area of a rectangle with length 5 and width 3?",
        "options": [15, 8, 20, 18],
        "answer": 15
    },
    {
        "question": "What is the area of a circle with radius 7? (Use π ≈ 3.14)",
        "options": [153.86, 140.0, 154.0, 160.0],
        "answer": 153.86
    },
    {
        "question": "What is the area of a triangle with base 4 and height 5?",
        "options": [10, 12, 15, 20],
        "answer": 10
    }
]

@quiz_bp.route('/quiz/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

@quiz_bp.route('/quiz/submit', methods=['POST'])
def submit_quiz():
    data = request.json
    score = 0
    for question, user_answer in zip(questions, data['answers']):
        if question['answer'] == user_answer:
            score += 1
    return jsonify({"score": score, "total": len(questions)})