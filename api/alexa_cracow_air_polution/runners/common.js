module.exports = (function() {
    
    var log4js = require('log4js');

    function setup(){

        log4js.configure({
            appenders: { 
                file: { 
                    type: 'dateFile', 
                    filename: 'logs/grido-web-identity.log', 
                    pattern: "--yyyy-MM-dd",
                    layout: {
                        type: 'pattern',
                        pattern: '[%d{ISO8601_WITH_TZ_OFFSET}] [%p] %c - %m' //  yyyy-MM-ddThh:mm:ss:SSSZ
                    }
                }
            },
            categories: { default: { appenders: ['file'], level: 'trace' } }
        });

    }

    return {
        setup: setup
    };

})();
            
            