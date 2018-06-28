(function(){
 'use strict';
 angular.module('one.demo',[]).controller('Onecontroller',['$scope','$http',Onecontroller]);

 function Onecontroller($scope,$http){
         $scope.add=function (list,title) {
           var card={
             list:list.id,
             title: title
           };
           $http.post("one/cards/",card).then(function(response){
            list.cards.push(response.data);
         },

            function() {
              alert("errror occured")
            });

         };

         $scope.data=[];
         $http.get("one/lists/").then(function(response)
       {
         $scope.data=response.data ;
       });


 }


}());
