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

$(".button").click(function() {
	console.log("testing a post");
    var input_string = "Test";
    $.ajax({
            type: "POST",
            data: {textfield : input_string},
            success: function(data) {
            	console.log("SUCCESS!!!!");
            },
            });
    return false;
    });
});
