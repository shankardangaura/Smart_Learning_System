from flask import Flask, request, jsonify
from flask_cors import CORS
import random, math

app = Flask(__name__)
CORS(app)

# ---------------- SHAPES ----------------
shape_data = {
    "circle": {
        "shape": "Circle",
        "formula": "π × r²",
        "description": "A circle is a round shape with all points equidistant from the center.",
        "example": "If radius = 7, area = π × 7 × 7"
    },
    "square": {
        "shape": "Square",
        "formula": "a²",
        "description": "A square has four equal sides.",
        "example": "If side = 5, area = 25"
    },
    "rectangle": {
        "shape": "Rectangle",
        "formula": "l × w",
        "description": "A rectangle has opposite sides equal.",
        "example": "If length = 6 and width = 4, area = 24"
    },
    "triangle": {
        "shape": "Triangle",
        "formula": "½ × b × h",
        "description": "A triangle has three sides.",
        "example": "If base = 10 and height = 4, area = 20"
    }
}

@app.route("/shapes")
def shapes():
    return jsonify(list(shape_data.keys()))

@app.route("/shapes/<name>")
def get_shape(name):
    return jsonify(shape_data[name])


# ---------------- QUIZ ----------------
@app.route("/quiz")
def quiz():
    questions = []

    for _ in range(120):
        shape = random.choice(["circle", "square", "rectangle", "triangle"])

        if shape == "circle":
            r = random.randint(2, 15)
            ans = round(math.pi * r * r, 2)
            q = {
                "shape": "Circle",
                "dimensions": {"radius": r},
                "answer": ans,
                "question": f"Find the area of a circle with radius {r}"
            }

        elif shape == "square":
            a = random.randint(2, 20)
            ans = a * a
            q = {
                "shape": "Square",
                "dimensions": {"side": a},
                "answer": ans,
                "question": f"Find the area of a square with side {a}"
            }

        elif shape == "rectangle":
            l = random.randint(5, 20)
            w = random.randint(5, 15)
            ans = l * w
            q = {
                "shape": "Rectangle",
                "dimensions": {"length": l, "width": w},
                "answer": ans,
                "question": f"Find the area of a rectangle {l} × {w}"
            }

        else:  # triangle
            b = random.randint(5, 20)
            h = random.randint(5, 20)
            ans = round(0.5 * b * h, 2)
            q = {
                "shape": "Triangle",
                "dimensions": {"base": b, "height": h},
                "answer": ans,
                "question": f"Find the area of a triangle with base {b} and height {h}"
            }

        questions.append(q)

    random.shuffle(questions)
    return jsonify(questions[:10])


# ---------------- SUBMIT QUIZ ----------------
@app.route("/quiz/submit", methods=["POST"])
def submit_quiz():
    data = request.json
    answers = data["answers"]
    questions = data["questions"]

    results = []
    score = 0

    for i, q in enumerate(questions):
        try:
            user_ans = float(answers[str(i)])
            correct_ans = float(q["answer"])
            is_correct = abs(user_ans - correct_ans) < 0.01
        except:
            user_ans = None
            correct_ans = q["answer"]
            is_correct = False

        if is_correct:
            score += 1

        results.append({
            "shape": q["shape"],
            "question": q["question"],
            "user_answer": user_ans,
            "correct_answer": correct_ans,
            "is_correct": is_correct
        })

    if score >= 8:
        feedback = "Excellent! You have mastered area calculations."
    elif score >= 5:
        feedback = "Good job! Keep practicing to improve further."
    else:
        feedback = "You need more practice. Review the Study section."

    return jsonify({
        "score": score,
        "feedback": feedback,
        "results": results
    })


if __name__ == "__main__":
    app.run(debug=True)
