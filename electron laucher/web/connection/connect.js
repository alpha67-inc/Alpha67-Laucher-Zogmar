
function hide()
{
    var nom = localStorage.nom;
    var x = document.getElementById("info");
    if (window.localStorage.getItem('invalid') == "okk") {
        x.style.display = "block";

    }
    else{
        x.style.display = "none";
    }

    var delayInMilliseconds = 1000; //1 second

    /*setTimeout(function() {
    alert("c'est bon");
    }, delayInMilliseconds);*/

}



function microsoft() {
    eel.startMicrosoft();
  }

  eel.expose(finish)
function finish()
{
    window.location.href = "../hello.html";
}

async function mojangLogin(){
    eel.startMojangLogin()

}

async function crackLogin(){
    alert("ok")
    eel.startCrackLogin()

}

eel.expose(getCred);
function getCred() {
    var userName = document.getElementById("username").value;
    var passWord = document.getElementById("password").value;
    const cred = [userName, passWord];
    return cred
}

eel.expose(getCredCrack);
function getCredCrack(){
    var userName = document.getElementById("usercrack").value;
    return userName;
}

eel.expose(invalid);
function invalid() {

    window.localStorage.setItem('invalid', 'okk');

    //document.getElementById('login-button').style.animation = "anim 2s 2s forward";
    var x = document.getElementById("info");
    x.style.display = "block";
    

}

$(document).ready(function(){
    $('.submit').click(function(e){
      // Code to check login
      // If fail
       $('.input').addClass('animated shake');
    });
})