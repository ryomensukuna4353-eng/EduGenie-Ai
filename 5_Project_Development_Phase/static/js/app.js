const task =
    document.getElementById("task");


const inputText =
    document.getElementById("inputText");


const submitBtn =
    document.getElementById("submitBtn");


const sampleBtn =
    document.getElementById("sampleBtn");


const statusBox =
    document.getElementById("status");


const resultCard =
    document.getElementById("resultCard");


const result =
    document.getElementById("result");


const copyBtn =
    document.getElementById("copyBtn");


const examples = {

    qa:
        "What is the difference between RAM and ROM?",

    explain:
        "Explain the Pythagoras theorem in simple language.",

    quiz:
        "Photosynthesis is the process by which green plants use sunlight, carbon dioxide, and water to produce glucose and oxygen. Chlorophyll absorbs light energy.",

    summarize:
        "Artificial intelligence is a field of computer science that develops systems able to perform tasks that normally require human intelligence, such as learning, reasoning, perception, and language understanding.",

    learn:
        "Python programming"

};


function escapeHtml(value) {

    return value
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

}


function endpointFor(value) {

    if (value === "learn") {

        return "/learn/recommendations";

    }

    return `/${value}`;

}


function renderQuiz(data) {

    if (data.error) {

        return `
            <div class="result-text">
                ${escapeHtml(data.error)}
            </div>
        `;

    }


    const questions =
        data.questions || [];


    return questions.map(
        (item, index) => {

            const options =
                item.options
                    .map(
                        option => `
                            <button
                                class="quiz-option"
                                data-answer="${escapeHtml(option)}"
                            >
                                ${escapeHtml(option)}
                            </button>
                        `
                    )
                    .join("");


            return `
                <article
                    class="quiz-question"
                    data-correct="${escapeHtml(item.correct_answer)}"
                >

                    <h3>
                        ${index + 1}.
                        ${escapeHtml(item.question)}
                    </h3>

                    <div class="quiz-options">

                        ${options}

                    </div>

                    <div
                        class="quiz-feedback"
                    ></div>

                </article>
            `;

        }
    ).join("");

}


function bindQuiz() {

    document
        .querySelectorAll(".quiz-question")
        .forEach(question => {

            const correct =
                question.dataset.correct;


            const feedback =
                question.querySelector(
                    ".quiz-feedback"
                );


            question
                .querySelectorAll(".quiz-option")
                .forEach(button => {

                    button.addEventListener(
                        "click",
                        () => {

                            const chosen =
                                button.dataset.answer;


                            question
                                .querySelectorAll(
                                    ".quiz-option"
                                )
                                .forEach(item => {

                                    item.disabled =
                                        true;

                                });


                            if (
                                chosen === correct
                            ) {

                                button.classList.add(
                                    "correct"
                                );


                                feedback.textContent =
                                    "Correct!";

                            }

                            else {

                                button.classList.add(
                                    "wrong"
                                );


                                feedback.textContent =
                                    `Not quite. Correct answer: ${correct}`;


                                question
                                    .querySelectorAll(
                                        ".quiz-option"
                                    )
                                    .forEach(item => {

                                        if (
                                            item.dataset.answer
                                            === correct
                                        ) {

                                            item.classList.add(
                                                "correct"
                                            );

                                        }

                                    });

                            }

                        }
                    );

                });

        });

}


async function submitTask() {

    const text =
        inputText.value.trim();


    if (!text) {

        statusBox.textContent =
            "Please enter a question, topic, or passage.";

        inputText.focus();

        return;

    }


    submitBtn.disabled =
        true;


    resultCard.classList.remove(
        "hidden"
    );


    statusBox.textContent =
        "EduGenie is thinking...";


    result.innerHTML =
        "";


    try {

        const response =
            await fetch(
                endpointFor(task.value),
                {

                    method:
                        "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({
                            text: text
                        })

                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            const detail =
                data.detail ||
                "The server rejected the request.";


            throw new Error(
                typeof detail === "string"
                    ? detail
                    : JSON.stringify(detail)
            );

        }


        if (task.value === "quiz") {

            result.innerHTML =
                renderQuiz(data);

            bindQuiz();

        }

        else {

            result.innerHTML = `
                <div class="result-text">
                    ${escapeHtml(
                        data.result ||
                        "No result returned."
                    )}
                </div>
            `;

        }


        statusBox.textContent =
            "Completed.";

    }

    catch (error) {

        result.innerHTML = `
            <div class="result-text">
                ${escapeHtml(
                    error.message
                )}
            </div>
        `;


        statusBox.textContent =
            "Request failed.";

    }

    finally {

        submitBtn.disabled =
            false;

    }

}


sampleBtn.addEventListener(
    "click",
    () => {

        inputText.value =
            examples[task.value];

        inputText.focus();

    }
);


task.addEventListener(
    "change",
    () => {

        inputText.placeholder =
            examples[task.value];

    }
);


submitBtn.addEventListener(
    "click",
    submitTask
);


copyBtn.addEventListener(
    "click",
    async () => {

        const text =
            result.innerText.trim();


        if (!text) {

            return;

        }


        try {

            await navigator.clipboard
                .writeText(text);


            statusBox.textContent =
                "Result copied.";

        }

        catch {

            statusBox.textContent =
                "Copy is not available in this browser.";

        }

    }
);