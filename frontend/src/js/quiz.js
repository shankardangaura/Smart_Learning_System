const quizData = [
    {
        question: "What is the area of a rectangle with a length of 5 and a width of 3?",
        a: "15",
        b: "8",
        c: "18",
        d: "20",
        correct: "a"
    },
    {
        question: "What is the area of a triangle with a base of 4 and a height of 5?",
        a: "10",
        b: "12",
        c: "15",
        d: "20",
        correct: "a"
    },
    {
        question: "What is the area of a circle with a radius of 3? (Use π ≈ 3.14)",
        a: "28.26",
        b: "31.42",
        c: "9.42",
        d: "18.84",
        correct: "a"
    },
    {
        question: "What is the area of a square with a side length of 4?",
        a: "12",
        b: "16",
        c: "20",
        d: "24",
        correct: "b"
    }
];

const quizContainer = document.getElementById('quiz');
const resultContainer = document.getElementById('result');
const submitButton = document.getElementById('submit');

function loadQuiz() {
    quizData.forEach((currentQuiz, index) => {
        const questionElement = document.createElement('div');
        questionElement.classList.add('question');
        questionElement.innerHTML = `
            <h2>${currentQuiz.question}</h2>
            <label>
                <input type="radio" name="question${index}" value="a">
                ${currentQuiz.a}
            </label>
            <label>
                <input type="radio" name="question${index}" value="b">
                ${currentQuiz.b}
            </label>
            <label>
                <input type="radio" name="question${index}" value="c">
                ${currentQuiz.c}
            </label>
            <label>
                <input type="radio" name="question${index}" value="d">
                ${currentQuiz.d}
            </label>
        `;
        quizContainer.appendChild(questionElement);
    });
}

function calculateScore() {
    let score = 0;
    quizData.forEach((currentQuiz, index) => {
        const answer = document.querySelector(`input[name="question${index}"]:checked`);
        if (answer && answer.value === currentQuiz.correct) {
            score++;
        }
    });
    return score;
}

submitButton.addEventListener('click', () => {
    const score = calculateScore();
    resultContainer.innerHTML = `You scored ${score} out of ${quizData.length}`;
});

loadQuiz();