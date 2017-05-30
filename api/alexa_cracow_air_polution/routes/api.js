var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
  res.send({ 'test': 'value' });
});

router.get('/airpolution', function(req, res, next) {
  var collection = req.app.locals.db.collection('airpolution');

  collection
  .find()
  .toArray(function(err, items) {
    res.json(items[0]);
  });
});

module.exports = router