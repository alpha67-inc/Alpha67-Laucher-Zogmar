eel.expose(js_random);
function js_random() {
    return Math.random();
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

var select = document.getElementById("selectNumber"); 
var options = ["1", "2", "3", "4", "5"]; 

// Optional: Clear all existing options first:
select.innerHTML = "";
// Populate list with options:
for(var i = 0; i < options.length; i++) {
    var opt = options[i];
    select.innerHTML += "<option value=\"" + opt + "\">" + opt + "</option>";
}