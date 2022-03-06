
function main()
{
  document.getElementById("settingsGameWidth").setAttribute('value','test');

  eel.javaEx("GRX")(n => GRX(n));
  eel.javaEx("GRY")(n => GRY(n));
  eel.javaEx("RAMMIN")(n => RAMMIN(n));
  eel.javaEx("RAMMAX")(n => RAMMAX(n));
  eel.javaEx("JAVA")(n => java(n));

}

function GRX(n)
{
  document.getElementById("settingsGameWidth").setAttribute('value',n);
}

function GRY(n)
{
  document.getElementById("settingsGameHeight").setAttribute('value',n);
}

function RAMMIN(n)
{
  document.getElementById("settingsrammin").setAttribute('value',n);
}

function RAMMAX(n)
{
  document.getElementById("settingsrammax").setAttribute('value',n);
}

function java(n)
{
  document.getElementById("javain").setAttribute('value',n);
}


function save()
{
  var x = document.getElementById("settingsGameWidth").value;
  var y = document.getElementById("settingsGameHeight").value;
  var min = document.getElementById("settingsrammin").value;
  var max = document.getElementById("settingsrammax").value;
  var java = document.getElementById("javain").value;

  eel.saveSettings(x,y,min,max,java)();

  window.location.href = "hello.html";

}