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
	 console.log("test");
	 $.ajax({
           type: "POST",
           headers: {"Content-Type": "application/json"},
           url: "http://localhost:5000/test",
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
