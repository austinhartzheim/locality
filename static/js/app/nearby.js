var app = angular.module('nearbyApp', []);
app.controller('NearbyController', function($scope, $http) {
    $scope.nearbyNodes =[
	{"tags": {"name": "Things"}}
    ];

    $scope.updateListings = function() {
	$http.get('/api/find_nearby/' + $scope.lat.toString() + '%2C' +
		  $scope.lng.toString() + '/').success(
		      function(data) {
			  $scope.nearbyNodes = data['nearby_nodes'];
		      });
    };

});
	