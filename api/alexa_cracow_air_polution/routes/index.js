var express = require('express');
var router = express.Router();
var Db = require('../db/db.js');

/* GET home page. */
router.get('/', function(req, res, next) {
  var collection = req.app.locals.db.collection('airpolution'),
    db = new Db(collection),
    viewModel = {};

  db.getStatus('cracow',
    function onSuccess(status){
      viewModel.status = status;
      onDataFetched();
    },
    function onError(){
      res.render('index', { title: 'Express' });
    });

  db.getAirQuality('cracow',
    function onSuccess(air){
      viewModel.air = air;
      onDataFetched();
    },
    function onError(){
      res.render('index', { title: 'Express' });
    });
  
  function onDataFetched(){
    if(viewModel.air && viewModel.status){
      res.render('index', viewModel);
    }
  }

});

module.exports = router;
