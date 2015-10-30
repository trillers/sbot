var webdriver = require('selenium-webdriver');
var source = {
    'WebDriver': ['get'],
    'WebElement': ['sendKeys', 'click']
};

require('./proxy/shareIO')(webdriver, source, {shareIO: true});
var clientType = process.argv[1];
module.exports = function createDriver(){
    var driver = new webdriver.Builder()
        .withCapabilities(webdriver.Capabilities.chrome())
        .setControlFlow(new webdriver.promise.ControlFlow())
        .build();
    return driver;
};
