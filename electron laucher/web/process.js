eel.expose(js_random);
function js_random() {
    var select = document.getElementById('versiong');
    var value = select.options[select.selectedIndex].value;
    alert(value) // en
    return "value";
}

async function run() {
    // Synchronous call must be inside function marked 'async'

    // Get result returned synchronously by
    //  using 'await' and passing nothing in second brackets
    //        v                   v
    let n = await eel.test()();
    console.log('Got this from Python: ' + n);
    alert(n);  
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
