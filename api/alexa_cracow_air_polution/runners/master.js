module.exports = (function() {
    
    var cluster = require('cluster');

    function run(){
        var i = 0;
        for (i; i < 4; i++){
          cluster.fork();
        }
        //if the worker dies, restart it.
        cluster.on('exit', function(worker){
          console.log('Worker ' + worker.id + ' died..');
          cluster.fork();
        });
    }

    return {
        run: run
    };

})();