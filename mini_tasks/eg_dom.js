var header  = document.querySelector("body");
header.style.backgroundColor  = "#f88028"

// '#ff8028'

function RandomColor(){
  var combination = "0123456789ABCDEF"
  var color       = "#"
  for (var i = 0; i<6; i++){
    color += combination[Math.floor(Math.random()*16)]
  }
  // eg: 45.2 floor 45
  // 45.2 ceil 46
  return color
}

function change(){
  var Bcolor = RandomColor()
  header.style.backgroundColor = Bcolor
}

setInterval("change()",600)
