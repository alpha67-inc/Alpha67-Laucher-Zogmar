//var fs = require('electron').remote.require('fs');

var isLauch = false;

eel.expose(returnInfo);
function returnInfo(){
    var select = document.getElementById('motor');
    var value = select.options[select.selectedIndex].value;
    var e = document.getElementById("versiong");
    var strUser = e.options[e.selectedIndex].text;
    const info = [value, strUser]
    return info;
}

eel.expose(js_random);
function js_random() {
  return Math.random();
}

eel.expose(alertP);
function alertP(errorP) {
  alert("The python fonction of the laucher crash, with error ---> "+ errorP);
}


eel.expose(message);
function message(message) {
  alert(message);
  isLauch = false;
  window.location.reload();
}

function onload()
{
  var isLauch = false;
}

async function start()
{

  if (isLauch == false)
  {
    var login = await eel.getSelectVersion()();
    console.log(login);
  
    if (login != null)
    {
      await getPercentValue()
      await run()
  
      var an = document.getElementById("loader"); 
      var btn = document.getElementById("wrapper"); 
      var cont = document.getElementById("test"); 
      
      an.classList.toggle('show');
      cont.classList.toggle('show');
      btn.classList.toggle('hide').disabled = true;
  
      
    }
  }
  else 
  {
    alert("Minecraft is already lauch or being install !!")
  }

}

function settP() {
  eel.isUseS()
}


eel.expose(sett)
function sett()
{
    var consst = document.getElementById("main"); 
    var settp = document.getElementById("settp"); 
    var bod = document.getElementById("bod"); 
    
    consst.classList.toggle('hides');
    //settp.classList.toggle('show');
    bod.classList.toggle('settings');

    const myInterval = setInterval(myTimer, 300);

function myTimer() {
  const date = new Date();
  window.location.href = "test.html";
}

    

    

eel.expose(gameLauch);
function gameLauch()
{
  //alert("ok");
  var element = document.getElementById("progressBar");   

}


}

async function getPercentValue()
{ 
  var element = document.getElementById("progressBar");   
  var text = document.getElementById("re"); 
  var cont = document.getElementById("test"); 
  var width = 1;
  var identity = setInterval(scene, 30);
  var load = document.getElementById("loader"); 
  var btn = document.getElementById("wrapper"); 
  var count = 0;

  async function scene() {
    width = await eel.read()();
    width = width.toFixed(1);

    if (width >= 128) {
      clearInterval(identity);
      //alert("stop")
      //load.classList.toggle('hide');
      cont.classList.toggle('hide');
      //btn.classList.toggle('show').disabled = false;
      //window.location.reload();
      //alert("finish")
    } 

    else {
      cont.style.display = "block";
      element.style.width = width + '%'; 
      text.innerHTML = width + "%";

    
    }
  }
  }




async function run() {
  //var elem = document.getElementById("progressBar");
  //var width = eel.updateBar()
  //elem.style.width = width + "%";
  //elem.innerHTML = width  + "%";
    //window.open('https://github.com', '_blank', 'top=500,left=200,frame=false,nodeIntegration=no')
  isLauch = true;
  eel.StartMinecraft();

    

          /*(function(settings){
            var version = settings;
              })*/
}

async function connection() {

  eel.isUseC();

}

eel.expose(sett2)
function sett2()
{
  window.localStorage.removeItem('invalid');
  window.location.href = "connection/connection.html";
}


eel.expose
function updatePrgressBar(){
  var elem = document.getElementById("progressBar");

}



eel.sendVersions()(function(settings){
    var version = settings;
    var select = document.getElementById("versiong"); 
  
  
    
    // Optional: Clear all existing options first:
    select.innerHTML = "";

    // Populate list with options:
    for(var i = 0; i < version.length; i++) {
        var opt = version[i];
        select.innerHTML += "<option value=\"" + opt + "\">" + opt + "</option>";
    }
      });

eel.expose(noc);
function noc()
{
  alert("veuillez vous connecter, avant de lancer le jeu !");
}