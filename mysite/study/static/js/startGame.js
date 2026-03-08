// retrieve python card object in json format and parse it
const serializeSetData = document.getElementById('cards');
const SetData = JSON.parse(serializeSetData.textContent);


// wait tell user answer correctly access next card
function loadCard(i) {
    if (i >= SetData.length) {
        question.textContent = "You win!";
        return;
    }
    question.textContent = SetData[i].question;
    option1.textContent = SetData[i].false_answer_1;
    option2.textContent = SetData[i].false_answer_2;
    option3.textContent = SetData[i].false_answer_3;
    option4.textContent = SetData[i].answer;
}

function gameLaunch() {

    if (serializeSetData) {
        let currentIndex = 0;
        question = document.getElementById("questionText")
        option1 = document.getElementById("option1Container");
        option2 = document.getElementById("option2Container");
        option3 = document.getElementById("option3Container");
        option4 = document.getElementById("option4Container");

        //move to next card when user click option 4 (while improve!!!)
        option4.addEventListener("click", function () {
            currentIndex++;
            loadCard(currentIndex);
        });

        loadCard(currentIndex);

    }
    else {
        console.log("Serialization Error");
    }
}

gameLaunch();



