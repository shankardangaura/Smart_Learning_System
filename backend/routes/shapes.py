from flask import Blueprint, jsonify, request
from models.knowledge_base import KnowledgeBase
import os
import traceback

shapes_bp = Blueprint('shapes', __name__)

# OWL file path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWL_PATH = os.path.join(BASE_DIR, "ontology", "shapes.owl")

# Initialize KnowledgeBase
try:
    knowledge_base = KnowledgeBase(OWL_PATH)
except Exception as e:
    print(f"Error loading knowledge base: {e}")
    knowledge_base = None

# Store current quiz answers
current_quiz_answers = {}

# Shape metadata
SHAPE_DATA = {
    "circle": {
        "description": "A circle is a geometric shape where all points are equidistant from the center.",
        "example": "Example: A circle with radius 5 has area = π × 5² ≈ 78.54",
        "formula": "π × r²"
    },
    "square": {
        "description": "A square is a regular quadrilateral with all sides equal and all angles 90 degrees.",
        "example": "Example: A square with side 5 has area = 5² = 25",
        "formula": "s²"
    },
    "rectangle": {
        "description": "A rectangle is a quadrilateral with opposite sides equal and all angles 90 degrees.",
        "example": "Example: A rectangle with length 5 and width 3 has area = 5 × 3 = 15",
        "formula": "length × width"
    },
    "triangle": {
        "description": "A triangle is a polygon with three sides and three angles.",
        "example": "Example: A triangle with base 5 and height 4 has area = (5 × 4) / 2 = 10",
        "formula": "(base × height) / 2"
    }
}

# ---------------- Routes -----------------

@shapes_bp.route('/shapes', methods=['GET'])
def get_shapes():
    try:
        shapes = knowledge_base.list_shapes()
        print(f"Shapes retrieved: {shapes}")
        return jsonify(shapes)
    except Exception as e:
        print(f"Error in get_shapes: {e}")
        traceback.print_exc()
        # Return default shapes if knowledge base fails
        return jsonify(list(SHAPE_DATA.keys()))

@shapes_bp.route('/shapes/<name>', methods=['GET'])
def get_shape_formula(name):
    try:
        print(f"Fetching shape: {name}")
        
        # Normalize name to lowercase
        name_lower = name.lower()
        
        # Try to get formula from knowledge base first
        formula = None
        try:
            formula = knowledge_base.get_formula(name_lower)
        except Exception as kb_error:
            print(f"Knowledge base error for {name}: {kb_error}")
            # Fall back to SHAPE_DATA
            formula = SHAPE_DATA.get(name_lower, {}).get("formula")
        
        if not formula:
            print(f"Formula not found for {name}")
            return jsonify({"error": f"Shape '{name}' not found"}), 404
        
        # Get metadata from SHAPE_DATA
        metadata = SHAPE_DATA.get(name_lower, {})
        
        response = {
            "shape": name.capitalize(),
            "formula": formula,
            "description": metadata.get("description", f"{name.capitalize()} is a geometric shape."),
            "example": metadata.get("example", "Example calculation using the formula above.")
        }
        
        print(f"Returning shape data: {response}")
        return jsonify(response)
        
    except Exception as e:
        print(f"Error in get_shape_formula for {name}: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@shapes_bp.route('/quiz', methods=['GET'])
def get_quiz():
    try:
        global current_quiz_answers
        questions = knowledge_base.generate_quiz_questions(10)
        current_quiz_answers = {i: q["answer"] for i, q in enumerate(questions)}
        quiz_for_frontend = [{"shape": q["shape"], "dimensions": q["dimensions"]} for q in questions]
        return jsonify(quiz_for_frontend)
    except Exception as e:
        print(f"Error in get_quiz: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@shapes_bp.route('/quiz/submit', methods=['POST'])
def submit_quiz():
    try:
        global current_quiz_answers
        data = request.json
        score = 0

        for idx, user_answer in data.items():
            correct = current_quiz_answers.get(int(idx))
            if correct is not None and abs(float(user_answer) - correct) < 0.01:
                score += 1

        if score <= 3:
            feedback = "Needs practice"
        elif score <= 7:
            feedback = "Good, but can improve"
        else:
            feedback = "Excellent!"

        return jsonify({"score": score, "feedback": feedback})
    except Exception as e:
        print(f"Error in submit_quiz: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@shapes_bp.route('/debug/shapes', methods=['GET'])
def debug_shapes():
    """Debug endpoint to check what shapes are available"""
    try:
        shapes = knowledge_base.list_shapes()
        return jsonify({
            "shapes_available": shapes,
            "shape_data_keys": list(SHAPE_DATA.keys()),
            "status": "success"
        })
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "failed",
            "fallback_shapes": list(SHAPE_DATA.keys())
        }), 500