var one   = document.querySelector('#one')
var two   = document.querySelector('#two')
var three = document.querySelector('#three')

one.addEventListener('mouseover', function(){

one.textContent = "Mouseover currently happening"
one.style.color = "blue"

})

one.addEventListener('mouseout',function(){
  one.textContent = "Hover Over Me"
  one.style.color = 'black'

})

two.addEventListener('click', function(){
  two.textContent = "Clicked"
  two.style.color = 'blue'
})

three.addEventListener('dblclick',function(){
  three.textContent = "Double Clicked"
  three.style.color = 'red'
})
