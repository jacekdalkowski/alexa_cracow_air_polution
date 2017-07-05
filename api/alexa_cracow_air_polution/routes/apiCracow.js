var express = require('express');
var alexaVerifier = require('alexa-verifier-middleware');
var bodyParser = require('body-parser');
var router = express.Router();

//router.use(alexaVerifier);
router.use(bodyParser.json());
router.use(bodyParser.urlencoded({ extended: false }));

var intentToHandler = new Map();
intentToHandler.set('GetAirQuality', handleGetAirQualityRequest);
intentToHandler.set('GetWeatherForecast', handleGetWeatherForecastRequest);

function handleGetAirQualityRequest(req, res, next) {
  var collection = req.app.locals.db.collection('airpolution');

  collection.aggregate([
      { $match: {'app': { $eq: 'cracow' }}},
      { $project : { 
        'air' : 1 } }])
  .toArray(function(err, items) {
    res.json(buildGetAirQualityResponse(items[0]));
  });
}

function handleGetWeatherForecastRequest(req, res, next) {
  var collection = req.app.locals.db.collection('airpolution');

  collection.aggregate([
      { $match: {'app': { $eq: 'cracow' }}},
      { $unwind : '$weather.list' },  
      { $match : {'weather.list.dt' : { $gte: 1499520000 } } },  
      { $project : { 
        'weather.dt' : '$weather.list.dt',  
        'weather.temp' : '$weather.list.main.temp', 
        'weather.descriptions' : '$weather.list.weather.description' } }])
    .toArray(function(err, items) {
      res.json(buildGetWeatherForecastResponse(items[0]));
    });

  /*
  collection
  .find()
  .toArray(function(err, items) {
    res.json(buildAlexaResponse(items[0]));
  });
  */
}

router.post('/', function(req, res, next) {
  var intentName = req.body.request.intent.name;
  if(intentToHandler.has(intentName)){
    intentToHandler.get(intentName)(req, res, next);
  }else{
    res.status(404).send('Not found');
  }
});

function mapPolutionDataToQualityIndex(airData){
  var pm10Level = airData.air.pm_10;
  if(pm10Level < 25){
    return "good";
  }else if(pm10Level < 50){
    return "moderate";
  }else if(pm10Level < 75){
    return "unhealthy";
  }else if(pm10Level < 100){
    return "very unhealthy";
  }else{
    return "hazardous";
  }
}

function buildGetAirQualityResponse(airData){

  var pm10Level = airData.air.pm_10;
  var qualityIndex = mapPolutionDataToQualityIndex(airData);

  var r = { 
  "version": "0.0.1", 
  "response": { 
    "outputSpeech": { 
      "type": "SSML", 
      "ssml": "<speak>" +
                "Air is <prosody volume='x-loud' pitch='x-low'>" + qualityIndex + "</prosody>. PM 10 level is " + pm10Level + "." +
              "</speak>", 
    }
  },
  "shouldEndSession": true 
  };

  return r;
}

function buildGetWeatherForecastResponse(weatherData){

  var description = weatherData.weather.descriptions[0];
  var temperature = weatherData.weather.temp;

  var r = { 
  "version": "0.0.1", 
  "response": { 
    "outputSpeech": { 
      "type": "SSML", 
      "ssml": "<speak>" +
                "It will be " + description + ". Temperature will be " + temperature + "." +
              "</speak>", 
    }
  },
  "shouldEndSession": true 
  };

  return r;
}

module.exports = router