var search = function(position){
    console.log(position);
    var form = document.forms["search-form"];
    var longitude = document.createElement("input");
    input.type = "hidden";
    input.name = "longitude";
    input.value = position.coords.longitude;
    form.appendChild(longitude);
    var latitude = document.createElement("input");
    input.type = "hidden";
    input.name = "latitude";
    input.value = position.coords.latitude;
    form.appendChild(latitude);
};

var searchButton = function(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(search);
    } else {
	console.log("Geolocation not supported.");
    }
};

var searchB = document.getElementById("search-button");
searchB.addEventListener('click', searchButton);
