const lien = document.getElementById("aideLien")
const p = document.getElementById("aide")
console.log("ok")
lien.addEventListener("click",function (){
	p.classList.toggle("cache");
})