function initMap() {
	
	var myLatLng = {lat: 35.2271, lng: -80.8431};
	
	var maxZoomLevel = 11;
	
	var mapOptions = {
		zoom: 11,
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
		title: 'Statesville High School'
	});
	
	var trafficLayer = new google.maps.TrafficLayer();
	trafficLayer.setMap(map);
	
	var contentString = '<div id="content">'+
	'<h1>Statesville High School</h1>'+ 'This highschool was founded in blah blah blah..'
	'</div>';
	
	var infowindow = new google.maps.InfoWindow({
		content: contentString
	});
	
	marker.addListener('click', function() {
		infowindow.open(map, marker);
	});
	
	
	var polygonMask = new google.maps.Polygon({
		map:map,
		strokeColor: '#000000',
		strokeOpacity: 0.5,
		strokeWeight: 2,
		fillColor: '#CACACA',
		fillOpacity: 0.7,
		paths: [[new google.maps.LatLng(34.523924, -81.671790),
		new google.maps.LatLng(35.870576, -81.671790),
		new google.maps.LatLng(35.870576, -79.879645),
		new google.maps.LatLng(34.523924, -79.879645),
		new google.maps.LatLng(34.523924, -81.671790)],
		[new google.maps.LatLng(35.075527, -80.986404),
		new google.maps.LatLng(35.104602, -80.936794),
		new google.maps.LatLng(35.038149, -80.868645),
		new google.maps.LatLng(35.043630, -80.731144),
		new google.maps.LatLng(35.068221, -80.620422),
		new google.maps.LatLng(35.216734, -80.600853),
		new google.maps.LatLng(35.357696, -80.683594),
		new google.maps.LatLng(35.382612, -80.803413),
		new google.maps.LatLng(35.343695, -80.956879),
		new google.maps.LatLng(35.234122, -80.997734),
		new google.maps.LatLng(35.075527, -80.986404)]]});
	
	polygonMask.setMap(map);
	
	// Bounds for North America
    var strictBounds = new google.maps.LatLngBounds(
    	new google.maps.LatLng(35.2429, -81.0373), 
        new google.maps.LatLng(35.4088, -80.5795)
    );

    // Listen for the dragend event
    google.maps.event.addListener(map, 'dragend', function() {
    	if (strictBounds.contains(map.getCenter())) return;

    	// We're out of bounds - Move the map back within the bounds

    	var c = map.getCenter(),
        	x = c.lng(),
        	y = c.lat(),
            maxX = strictBounds.getNorthEast().lng(),
            maxY = strictBounds.getNorthEast().lat(),
            minX = strictBounds.getSouthWest().lng(),
            minY = strictBounds.getSouthWest().lat();

        if (x < minX) x = minX;
        if (x > maxX) x = maxX;
        if (y < minY) y = minY;
        if (y > maxY) y = maxY;

        map.setCenter(new google.maps.LatLng(y, x));
        
    });
	
	// Limit the zoom level
    google.maps.event.addListener(map, 'zoom_changed', function() {
    	if (map.getZoom() < maxZoomLevel) 
    		map.setZoom(maxZoomLevel);
    });
	
}

$( "#lat" ).val("35.2271");

$( "#long" ).val("80.8431");