const signIn = document.getElementById("signIn");
const email = document.getElementById("email");
const pass = document.getElementById("pass");
const anime = document.getElementById("reveal");

signIn.addEventListener("click", checkValidation);
email.addEventListener("keyup", rollBack);
pass.addEventListener("keyup", rollBack);

function rollBack() {

	if (anime.classList.contains("moved")) {
		
			anime.classList.toggle("moved");
		

	}
}
function checkValidation() {
	const result = document.getElementById("result");
	if (email.value === "admin@gmail.com" && pass.value === "admin") {
		result.innerHTML = "Login Succesfully";
		result.style.color="green";
		result.style.opacity="0.6";
	}
	else{
		result.innerHTML = "Invalid Data";
		result.style.color="red";
		result.style.opacity="0.6";
	}
	if(!anime.classList.contains("moved"))
	{
	anime.classList.toggle("moved"); 
}
}