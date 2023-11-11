let rand1 = Math.floor(Math.random()*6)+1
let rand2 = Math.floor(Math.random()*6)+1

let randomPNG = `images/dice${rand1}.png`;
let randomPNG1 = `images/dice${rand2}.png`;

let image1 = document.querySelectorAll("img")[0];
image1.setAttribute("src", randomPNG)

let image2 = document.querySelectorAll("img")[1];
image2.setAttribute("src", randomPNG1)

let content = document.querySelector("h1");
if (rand1 > rand2){

    content.innerHTML = ` ⛳Player 1 is winner `
}
else if(rand2 > rand1 ){
    content.innerHTML = `Player 2 is winner⛳`
}
else{
    content.innerHTML = `⛳Draw⛳ `
}
