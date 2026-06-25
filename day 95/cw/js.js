const p1 = document.getElementById('p1')
const p2 = document.getElementById('p2')
const p3 = document.getElementById('p3')
const p4 = document.getElementById('p4')

const b1 = document.getElementById('b1')
const b2 = document.getElementById('b2')
const b3 = document.getElementById('b3')
const b4 = document.getElementById('b4')


b1.addEventListener('click', () => {
    p1.innerText = "ტექსტი შეიცვალა"
})


b2.addEventListener('dblclick', () => {
    p2.style.backgroundColor = "yellow"
})


b3.addEventListener('mouseover', () => {
    p3.style.width = "400px"
})


b4.addEventListener('mouseout', () => {
    p4.innerText = ""
})