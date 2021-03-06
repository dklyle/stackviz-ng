'use strict';

var directivesModule = require('./_index.js');

var d3 = require('d3');

/**
 * @ngInject
 */
function timeline() {
  var link = function(scope, el, attrs) {

    var init = function() {
      // TODO d3 init
    };

    var update = function() {
      // TODO d3 update
    };

    scope.$on('windowResize', function() {
      // TODO handle resize
    });
  };

  return {
    restrict: 'EA',
    scope: {
      'dataset': '='
    },
    link: link
  };
}

directivesModule.directive('timeline', timeline);
