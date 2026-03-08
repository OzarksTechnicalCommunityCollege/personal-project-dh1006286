//Base Url of the website
const siteUrl = '//127.0.0.1:8000/'
// Url of the css
const styleUrl = siteUrl + 'static/css/study.css'

const set = document.getElementById('cards');
console.log("hello")
function gameLaunch() {


    if (set) {
        const cardsArray = JSON.parse(set.textContent);
        console.log(cardsArray);
        console.log("e")
    } else {
        console.log("error");
    }
}

gameLaunch();



//html
// var body = document.getElementsByTagName('body')[0]
// boxHtml = '
//     <
// '