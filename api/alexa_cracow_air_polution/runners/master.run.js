var cluster = require('cluster');
var commonSetup = require('./common');

commonSetup.setup();
if (cluster.isMaster) {
  var master = require('./master');
  master.run();
}else{
  var worker = require('./worker');
  worker.run();
}
