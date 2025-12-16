from flask import Blueprint, request, jsonify

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    score = data.get('score')
    comments = data.get('comments')

    # Process the feedback (store it, analyze it, etc.)
    # For now, we'll just return a success message
    response = {
        'message': 'Feedback submitted successfully!',
        'score': score,
        'comments': comments
    }
    return jsonify(response), 200

@feedback_bp.route('/get_feedback/<int:student_id>', methods=['GET'])
def get_feedback(student_id):
    # Here you would typically retrieve feedback from a database
    # For demonstration, we'll return a mock response
    mock_feedback = {
        'student_id': student_id,
        'feedback': 'Great job! Keep practicing your area calculations.'
    }
    return jsonify(mock_feedback), 200