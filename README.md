## Overview
The Smart Tutoring App is an interactive web application designed to help students learn how to calculate the area of various geometric shapes. The application features educational content, quizzes to test knowledge, and feedback based on quiz performance. 

## Project Structure
The project is divided into two main parts: the frontend and the backend.

### Frontend
- **src/index.html**: The main entry point for the web application.
- **src/css/styles.css**: Contains the main styles for the application.
- **src/css/responsive.css**: Ensures the webpage is fully responsive.
- **src/js/main.js**: Handles core functionality and user interactions.
- **src/js/quiz.js**: Manages quiz functionality, including question display and score tracking.
- **src/js/utils.js**: Contains utility functions for calculations and helpers.
- **src/pages/shapes.html**: Provides information on different shapes and area calculations.
- **src/pages/quiz.html**: Presents the quiz to students.
- **src/pages/feedback.html**: Displays feedback based on quiz performance.

### Backend
- **app.py**: Main entry point for the backend application using Flask.
- **requirements.txt**: Lists Python dependencies required for the backend.
- **routes/shapes.py**: Contains routes related to shape information and area calculations.
- **routes/quiz.py**: Manages quiz-related routes and submissions.
- **routes/feedback.py**: Handles feedback processing based on student performance.
- **ontology/shapes.owl**: OWL file defining the ontology for different shapes.
- **models/knowledge_base.py**: Logic for interacting with the ontology and reasoning.
- **config.py**: Configuration settings for the backend application.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd shape-learning-app
   ```

2. **Frontend Setup**:
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Start the frontend server:
     ```
     npm start
     ```

3. **Backend Setup**:
   - Navigate to the `backend` directory.
   - Create a virtual environment:
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the backend server:
     ```
     python app.py
     ```

## Usage
- Access the application through your web browser at `http://localhost:3000` for the frontend and `http://localhost:5000` for the backend API.
- Explore different shapes, take quizzes, and receive feedback based on your performance.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.
