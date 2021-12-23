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


async function run() {
    //window.open('https://github.com', '_blank', 'top=500,left=200,frame=false,nodeIntegration=no')
    eel.StartMinecraft()

          /*(function(settings){
            var version = settings;
              })*/
}

async function connection() {
  window.localStorage.removeItem('invalid');
  window.location.href = "connection/connection.html";
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
