describe(...

  beforeEach(module('myApplication'))
         
  beforeEach(module(function($provide) {
    $provide.value('myDependency', myDependency);
  }));

  beforeEach(inject(function (...
