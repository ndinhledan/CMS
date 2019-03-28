var markerType = {
    "incidents": [],
    "weather": [],
    "psi": []
};

var map;

$(function () {

    function initMap() {

        var location = new google.maps.LatLng(1.35735, 103.821);

        var mapCanvas = document.getElementById('map');
        var mapOptions = {
            center: location,
            zoom: 11,
            panControl: false,
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }

        map = new google.maps.Map(mapCanvas, mapOptions);

        //var markerImage = new Image();
        //markerImage.src = 'marker.png';

        loadMarkers();
        //var styles = [{"featureType": "landscape", "stylers": [{"saturation": -100}, {"lightness": 65}, {"visibility": "on"}]}, {"featureType": "poi", "stylers": [{"saturation": -100}, {"lightness": 51}, {"visibility": "simplified"}]}, {"featureType": "road.highway", "stylers": [{"saturation": -100}, {"visibility": "simplified"}]}, {"featureType": "road.arterial", "stylers": [{"saturation": -100}, {"lightness": 30}, {"visibility": "on"}]}, {"featureType": "road.local", "stylers": [{"saturation": -100}, {"lightness": 40}, {"visibility": "on"}]}, {"featureType": "transit", "stylers": [{"saturation": -100}, {"visibility": "simplified"}]}, {"featureType": "administrative.province", "stylers": [{"visibility": "off"}]}, {"featureType": "water", "elementType": "labels", "stylers": [{"visibility": "on"}, {"lightness": -25}, {"saturation": -100}]}, {"featureType": "water", "elementType": "geometry", "stylers": [{"hue": "#ffff00"}, {"lightness": -25}, {"saturation": -97}]}];

        //map.set('styles', styles);
    }

    google.maps.event.addDomListener(window, 'load', initMap);

    setInterval(function () {
        window.location.reload(true);
    }, 5 * 60 * 1000);

    function loadMarkers() {
        for (var i = 0; i < locations.length; i++) {
            addMarker(locations[i]);
        }

        addInfoWindow({ lat: 1.46981, lng: 103.817 }, "psi", "PSI: ", psi_north, 40, 0);//north
        addInfoWindow({ lat: 1.35735, lng: 103.695 }, "psi", "PSI: ", psi_west, -150, 50);//west
        addInfoWindow({ lat: 1.35735, lng: 103.821 }, "psi", "PSI: ", psi_central, 0, 50);//central
        addInfoWindow({ lat: 1.35735, lng: 103.941 }, "psi", "PSI: ", psi_east, 180, 50);//east
        addInfoWindow({ lat: 1.24082, lng: 103.828 }, "psi", "PSI: ", psi_south, 50, 85);//south
        addInfoWindow({ lat: 1.46981, lng: 103.817 }, "weather", "Weather: ", weather_north, -50, 0);//north
        addInfoWindow({ lat: 1.35735, lng: 103.695 }, "weather", "Weather: ", weather_west, -150, 0);//west
        addInfoWindow({ lat: 1.35735, lng: 103.821 }, "weather", "Weather: ", weather_central, 0, 10);//central
        addInfoWindow({ lat: 1.35735, lng: 103.941 }, "weather", "Weather: ", weather_east, 180, 0);//east
        addInfoWindow({ lat: 1.24082, lng: 103.828 }, "weather", "Weather: ", weather_south, -50, 85);//south
    }

    function addInfoWindow(lat_lng, type, displayString, region, width, height) {
        var contentString = '<div class="info-window">' +
            '<p>' + displayString + region + '</p>' +
            '</div>';
        var infowindow = new google.maps.InfoWindow({
            position: lat_lng,
            content: contentString,
            maxWidth: 160,
            pixelOffset: new google.maps.Size(width, height),
            opened: true
        });
        infowindow.open(map);
        markerType[type].push(infowindow);
    }

    function addMarker(lat_lng) {
        var marker = new google.maps.Marker({
            position: lat_lng,
            map: map,
            type: "incidents",
        });
        markerType["incidents"].push(marker);
    }
});

function toggleGroup(type) {
    if (type == "incidents") {
        toggleMarkers(type);
    }
    else {
        toggleWindows(type);
    }
}

function toggleMarkers(type){
    for (var i = 0; i < markerType[type].length; i++) {
        var marker = markerType[type][i];
        if (!marker.getVisible()) {
            marker.setVisible(true);
        } else {
            marker.setVisible(false);
        }
    }
}

function toggleWindows(type){
    for (var i = 0; i < markerType[type].length; i++) {
        var infowindow = markerType[type][i];
        if (infowindow.opened) {
            var windownew = new google.maps.InfoWindow({
                position: infowindow.position,
                content: infowindow.content,
                maxWidth: 160,
                pixelOffset: infowindow.pixelOffset,
                opened: false
            });
            infowindow.close();
            markerType[type][i] = windownew;
        } else {
            infowindow.open(map);
            infowindow.opened = true;
        }
    }
}