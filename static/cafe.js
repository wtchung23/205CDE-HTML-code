mobileMode();
loginError();
loginMode();

function mobileMode(){
	var w = window.innerWidth;
	var h = window.innerHeight;
	var i;
	var TopPge = document.getElementById("topPage");
	var BottomPge = document.getElementById("bottomPage");
	var removeDd = 	document.getElementsByClassName("removeDowndrop")
	if(w<768){
		for(i=0;i<removeDd.length;i++){
		removeDd[i].removeAttribute("onmouseover");
		}
	}
	else{
		for(i=0;i<removeDd.length;i++){
		removeDd[i].setAttribute("onmouseover","openDList()");
		}
	}
	if(w<1079){
		TopPge.style.padding = "0px";
		BottomPge.style.padding = "50px 20px 0px 20px";
	}
	else{
		TopPge.style.padding = "0px "+w*(200/1680)+"px";
		BottomPge.style.padding = "50px "+w*(200/1680)+"px "+"0px "+w*(200/1680)+"px";
		//slideShow[0].style.padding = "0px "+w*0.09+"px";
	}
	/*
	document.getElementById("demo").innerHTML = "Width: " + w + "<br>Height: " + h;
	*/
}
//function for dropdown
function openDList(){
	document.getElementsByClassName("dropdown-menu")[0].style.display = 'block'
}
function closeDList(){
	document.getElementsByClassName("dropdown-menu")[0].style.display = 'none'
}
function loginMode(){
	var username = document.getElementById("username");
	var loginBtn = document.getElementById("loginBtn");
	if(username.textContent == ""){
		//document.getElementById("demo").innerHTML = 'null';
		if(loginBtn.hasAttribute("data-toggle")){}
		else{
			loginBtn.setAttribute("data-toggle","modal");
			loginBtn.removeAttribute("onclick");
			loginBtn.innerHTML = "Login";
			username.style.display = 'none';
		}
	}
	else{
		loginBtn.removeAttribute("data-toggle");
		loginBtn.setAttribute("onclick","signoutMode()");
		loginBtn.innerHTML = "Sign out";
		username.style.display = '';
	}
}
function signoutMode(){
	window.open("http://localhost:5000/signout","_self")
}
//When login error
function loginError(){
	var error = document.getElementById("errorMessage").textContent;
	var modal = document.getElementById("205Modal");
	var close = document.getElementsByClassName("close")[0];
	var div = document.createElement("DIV");
	if(error=='false'){
		document.getElementById("errorMessage").innerHTML = 'Username or Password are incorrect';
		modal.style.display = "block";
		modal.setAttribute("class","modal fade in");
		div.setAttribute("class","modal-backdrop fade in");
		document.body.appendChild(div);
		close.setAttribute("onclick","closeModal()")
		
	}
}
function closeModal(){
	var modal = document.getElementById("205Modal");
	var div = document.getElementsByClassName("modal-backdrop fade in")[0];
	var close = document.getElementsByClassName("close")[0];
	modal.style.display = "none";
	modal.setAttribute("class","modal fade");
	div.setAttribute("class","");
	close.removeAttribute("onclick")
	document.getElementById("errorMessage").innerHTML = '';
}
