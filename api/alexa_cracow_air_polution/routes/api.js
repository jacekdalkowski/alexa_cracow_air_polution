var express = require('express');
var alexaVerifier = require('alexa-verifier-middleware');
var router = express.Router();

//router.use(alexaVerifier);

router.post('/', function(req, res, next) {
  var collection = req.app.locals.db.collection('airpolution');

  collection
  .find()
  .toArray(function(err, items) {
    res.json(buildAlexaResponse(items[0]));
  });
});

function mapPolutionDataToQualityIndex(pollution_data){
  var pm10Level = pollution_data['pm_10']
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

function buildAlexaResponse(pollution_data){

  var pm10Level = pollution_data['pm_10'];
  var qualityIndex = mapPolutionDataToQualityIndex(pollution_data);

  var r = { 
  "version": "0.0.1", 
  "response": { 
    "outputSpeech": { 
      "type": "SSML", 
      "ssml": "<speak>" +
                "Air is <prosody volume='x-loud' pitch='x-low'>" + qualityIndex + "</prosody>. PM 10 level is " + pollution_data['pm_10'] + "." +
              "</speak>", 
    }
  },
  "shouldEndSession": true 
  };

  return r;
}

module.exports = router