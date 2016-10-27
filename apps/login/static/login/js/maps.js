  function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 8,
      center: new google.maps.LatLng(47.548034, -121.983603)
    });
    var geocoder = new google.maps.Geocoder();

    document.getElementById('submit').addEventListener('click', function() {
      geocodeAddress(geocoder, map);
    });
    console.log('addMarkerToMap');
    addMarkerToMap(47.51730186993863, -122.37133436968786);
  }

  var map;
  var geocoder;
  var lat;
  var long;

  function geocodeAddress(geocoder, resultsMap) {
    var address = document.getElementById('address').value;
    geocoder.geocode({'address': address}, function(results, status) {
      if (status === 'OK') {
        resultsMap.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
          map: resultsMap,
          position: results[0].geometry.location
        });
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });
  }
  function showPosition(position) {
      lat = position.coords.latitude;
      long = position.coords.longitude;
      addMarkerToMap(lat, long);
      geocodeLatLong(geocoder, map);
  }

  function showError(error) {
      switch(error.code) {
          case error.PERMISSION_DENIED:
              document.getElementById("map").innerHTML = "User denied the request for Geolocation."
              break;
          case error.POSITION_UNAVAILABLE:
              document.getElementById("map").innerHTML = "Location information is unavailable."
              break;
          case error.TIMEOUT:
              document.getElementById("map").innerHTML = "The request to get user location timed out."
              break;
          case error.UNKNOWN_ERROR:
              document.getElementById("map").innerHTML = "An unknown error occurred."
              break;
      }
  }

  function addMarkerToMap(lat, long){
      var myLatLng = new google.maps.LatLng(lat, long);
      var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          animation: google.maps.Animation.DROP,
      });
  }
