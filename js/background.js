var Dark = function()
{
    document.getElementsByClassName("dark_stylesheet_link")[0].href="css/dark.css";


};

var Light = function()
{
    document.getElementsByClassName("dark_stylesheet_link")[0].href="";

};
var DarkStylesheetRequestCompleted = function () {
    // console.log(httpRequest.readyState);
    // console.log(XMLHttpRequest.DONE);
    console.log("Request completed");
};

var LoadStylesheet = function() {
    var httpRequest;
    httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange =  DarkStylesheetRequestCompleted;
    httpRequest.open('GET', 'css/dark.css');
    httpRequest.send();


};

// LoadStylesheet();
