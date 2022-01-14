//var fs = require('electron').remote.require('fs');

eel.expose(returnInfo);
function returnInfo(){
    var select = document.getElementById('motor');
    var value = select.options[select.selectedIndex].value;
    var e = document.getElementById("versiong");
    var strUser = e.options[e.selectedIndex].text;
    const info = [value, strUser]
    return info;
}

function first ()
{
  var cont = document.getElementById("test");
  x.style.display = "block";
}

eel.expose(js_random);
function js_random() {
  return Math.random();
}

async function start()
{
//alert("start");

  var login = await eel.getSelectVersion()();
  console.log(login);

  if (login != null)
  {
    await getPercentValue()
    await run()

    var cont = document.getElementById("loader"); 
    var btn = document.getElementById("wrapper"); 
    
    cont.classList.toggle('show');
    btn.classList.toggle('hide').disabled = true;

    
  }


}


async function sett()
{

    var consst = document.getElementById("main"); 
    var bod = document.getElementById("bod"); 
    
    consst.classList.toggle('hides');
    bod.classList.toggle('settings');




}

async function getPercentValue()
{ 
  var element = document.getElementById("progressBar");   
  var text = document.getElementById("re"); 
  var cont = document.getElementById("test"); 
  var width = 1;
  var identity = setInterval(scene, 100);
  var load = document.getElementById("loader"); 
  var btn = document.getElementById("wrapper"); 
  var count = 0;

  async function scene() {
    width = await eel.read()();
    width = width.toFixed(1);
    console.log(width);


    try {

      if (before == width) {
        count = count+1;
        console.log(count)
      }
      
      else {
        count = 0;
        console.log(count);
      }

    } 
    
    catch (error) {
      console.error(error);
    }



    if (width >= 100 || count == 100) {
      clearInterval(identity);
      cont.style.display = "none";
      load.classList.toggle('hide');
      btn.classList.toggle('show');

      load.classList.toggle('hide');
      btn.classList.toggle('show');
      alert("finish")
    } 

    else {
      cont.style.display = "block";
      element.style.width = width + '%'; 
      text.innerHTML = width + "%";

      var before = width;
    
    }
  }


  }




async function run() {
  //var elem = document.getElementById("progressBar");
  //var width = eel.updateBar()
  //elem.style.width = width + "%";
  //elem.innerHTML = width  + "%";
    //window.open('https://github.com', '_blank', 'top=500,left=200,frame=false,nodeIntegration=no')
  eel.StartMinecraft();

    

          /*(function(settings){
            var version = settings;
              })*/
}

async function connection() {
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