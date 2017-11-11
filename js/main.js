google.maps.event.addDomListener(window, 'load', init);

function init() {
	//var mapCanvas = document.getElementById('map');
	
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
	
	var marker = new google.maps.Marker({
		position: myLatLng,
		map: map,
		title: 'Predictive Auto Incident Map'
	});
	
	var trafficLayer = new google.maps.TrafficLayer();
	trafficLayer.setMap(map);
	
	var contentString = '<div id="content">'+
	'<h1>Predictive Auto Incident Map</h1>'+
	'</div>';
	
	var infowindow = new google.maps.InfoWindow({
		content: contentString
	});
	
	marker.addListener('click', function() {
		infowindow.open(map, marker);
	});
}