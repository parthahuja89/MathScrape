

chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
    var url = tabs[0].url;
    console.log("sending url to native app");
    porting.postMessage(url);
    alert(tabs[0].url); // return the url
  
});

//creates a json file with the url of the active tab
