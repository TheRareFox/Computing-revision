// Image switcher code

var myImage = document.querySelector('img');

myImage.onclick = function() {
  var name = localStorage.getItem('name');
  if (name === "Alex" || name === "alex"){
    var images = ['pic1.jpeg','pic5.jpeg','pic6.jpeg','pic9.jpeg','pic1.jpeg'];
      }
  else {
      var images = ['pic1.jpeg','pic2.jpeg','pic3.jpeg','pic4.jpeg','pic5.jpeg','pic6.jpeg','pic7.jpeg','pic8.jpeg','pic9.jpeg','pic10.jpeg','pic11.jpeg','pic12.jpeg','pic13.jpeg','pic1.jpeg'];
    }
    var mySrc = myImage.getAttribute('src');
    if(mySrc === images[-1]) {
        myImage.setAttribute ('src',images[0]);
    }
    else {
      var index = images.indexOf(mySrc);
      myImage.setAttribute ('src',images[index+1]);
    }
  }
// Personalized welcome message code

var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName() {
  var myName = prompt('Please enter your name.');
  localStorage.setItem('name', myName);
  myHeading.innerHTML = 'Welcome to the 5C34 sleeping gallery, ' + myName;
}

if(!localStorage.getItem('name')) {
  setUserName();
} else {
  var storedName = localStorage.getItem('name');
  myHeading.innerHTML = 'Welcome to the 5C34 sleeping gallery, ' + storedName;
}

myButton.onclick = function() {
  setUserName();
}
