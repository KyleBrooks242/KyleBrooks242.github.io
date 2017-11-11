function initMap() {
	
	var myLatLng = {lat: 35.919576, lng: -79.053618};
	
	var mapOptions = {
		zoom: 50,
		center: myLatLng,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		zoomControl: true,
		zoomControlOptions: {
			position: google.maps.ControlPosition.RIGHT_BOTTOM
		},
		mapTypeControl: true,
		mapTypeControlOptions: {
			style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
			position: google.maps.ControlPosition.RIGHT_TOP
		},
		scaleControl: true,
		streetViewControl: true,
		streetViewControlOptions: {
			position: google.maps.ControlPosition.RIGHT_BOTTOM
		},
		rotateControl: false
	}
	
	var map = new google.maps.Map(document.getElementById('map'), mapOptions);
}

$('#testButton').click(function(){
<<<<<<< HEAD
		$.ajax({
			url: 'http://127.0.0.1:5000/predictIncident',
			data: {"username":"username","password":"password"},
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
=======
	 console.log("test");
	 $.ajax({
           type: "GET",
           headers: {"Content-Type": "application/json"},
           url: "/kylebrooks242.github.io/test2/",
           data: JSON.stringify({"key": "value"}),
           success: function(response) {
               console.log(response);
           },
           error: function(response, error) {
               console.log(response);
               console.log(error);
           }
       });
});
>>>>>>> branch 'master' of https://github.com/KyleBrooks242/KyleBrooks242.github.io.git
