document.addEventListener("DOMContentLoaded", function() {
    const shapeInfo = document.getElementById("shape-info");
    const quizButton = document.getElementById("quiz-button");
    const feedbackButton = document.getElementById("feedback-button");

    // Load shape information
    function loadShapeInfo() {
        fetch('/api/shapes')
            .then(response => response.json())
            .then(data => {
                shapeInfo.innerHTML = '';
                data.shapes.forEach(shape => {
                    const shapeElement = document.createElement("div");
                    shapeElement.className = "shape";
                    shapeElement.innerHTML = `<h3>${shape.name}</h3><p>${shape.description}</p>`;
                    shapeInfo.appendChild(shapeElement);
                });
            })
            .catch(error => console.error('Error loading shape information:', error));
    }

    // Redirect to quiz page
    quizButton.addEventListener("click", function() {
        window.location.href = "pages/quiz.html";
    });

    // Redirect to feedback page
    feedbackButton.addEventListener("click", function() {
        window.location.href = "pages/feedback.html";
    });

    // Initialize the application
    loadShapeInfo();
});