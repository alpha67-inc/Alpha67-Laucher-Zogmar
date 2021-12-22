
function microsoft() {
    eel.startMicrosoft();
  }

function finish()
{
    window.location.href = "../hello.html";
}

async function mojangLogin(){
    eel.startMojangLogin()

}

eel.expose(getCred);
function getCred() {
    var userName = document.getElementById("username").value;
    var passWord = document.getElementById("password").value;
    const cred = [userName, passWord];
    return cred
}

eel.expose(invalid);
function invalid() {
    //document.getElementById('login-button').style.animation = "anim 2s 2s forward";
    document.getElementById("h1").style.color = "blue";
    alert("invalid cred")

}

