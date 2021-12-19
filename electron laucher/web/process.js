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