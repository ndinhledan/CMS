$(function () {

    function initMap() {

        var location = new google.maps.LatLng(1.344, 103.839);

        var mapCanvas = document.getElementById('map');
        var mapOptions = {
            center: location,
            zoom: 11,
            panControl: false,
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);

        //all different colour markers
        var markerImage1 = new Image();
        markerImage1.src = 'marker1.png';
        
        function test1(){
        addMarker({lat:1.265, lng:103.818});
        }

        function test2(){
        addMarker({lat:1.354, lng:103.941});
        }

        function test3(){
        addMarker({lat:1.344, lng:103.813});        
        }

        function test4(){
        addMarker({lat:1.338, lng:103.695});
        }

        function test5(){
            addMarker({lat:1.338, lng:103.695});
            addMarker({lat:1.344, lng:103.813});
            addMarker({lat:1.354, lng:103.941});
            addMarker({lat:1.265, lng:103.818});
        }

        function addMarker(lat_lng){
        var marker = new google.maps.Marker({
          position: lat_lng,
          map:map,
          icon: markerImage1
        });
        }


        function removeAllMarker(){
            for (var i = 0; i < markers.length; i++) {
          markers[i].setMap(map);
            };
        }

        

        



        //put filter

        var contentString = '<div class="info-window">' +
                '<h3>Info Window Content</h3>' +
                '<div class="info-content">' +
                '<p>Incident Type</p>' + 
                '</div>' +
                '</div>';

        var infowindow = new google.maps.InfoWindow({
            content: contentString,
            maxWidth: 400
        });

        marker.addListener('click', function () {
            infowindow.open(map, marker);
        });

        var styles = [{"featureType": "landscape", "stylers": [{"saturation": -100}, {"lightness": 65}, {"visibility": "on"}]}, {"featureType": "poi", "stylers": [{"saturation": -100}, {"lightness": 51}, {"visibility": "simplified"}]}, {"featureType": "road.highway", "stylers": [{"saturation": -100}, {"visibility": "simplified"}]}, {"featureType": "road.arterial", "stylers": [{"saturation": -100}, {"lightness": 30}, {"visibility": "on"}]}, {"featureType": "road.local", "stylers": [{"saturation": -100}, {"lightness": 40}, {"visibility": "on"}]}, {"featureType": "transit", "stylers": [{"saturation": -100}, {"visibility": "simplified"}]}, {"featureType": "administrative.province", "stylers": [{"visibility": "off"}]}, {"featureType": "water", "elementType": "labels", "stylers": [{"visibility": "on"}, {"lightness": -25}, {"saturation": -100}]}, {"featureType": "water", "elementType": "geometry", "stylers": [{"hue": "#ffff00"}, {"lightness": -25}, {"saturation": -97}]}];

        map.set('styles', styles);
    }
    google.maps.event.addDomListener(window, 'load', initMap);
});