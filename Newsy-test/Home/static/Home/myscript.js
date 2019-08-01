function search(){
	var searchBox = document.getElementById("searchBox");
	var data = searchBox.value;
	if(data !=""){
	window.open('https://www.google.co.in/search?q='+data, '_blank');
	searchBox.value = "";
	}
	else{
		alert("Enter something to search");
	}
}