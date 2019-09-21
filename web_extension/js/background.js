// localStorage["current_url"] is preset to https://www.facebook.com/legal/terms/update
localStorage["current_url"] = "https://www.facebook.com/legal/terms/update";

chrome.tabs.onActivated.addListener(function(activeInfo) {
  chrome.tabs.get(activeInfo.tabId, function(tab) {
    localStorage["current_url"] = tab.url;
    console.log(tab.url);
  });
  chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab){
    if(tabId == activeInfo.tabId){
      chrome.tabs.get(activeInfo.tabId, function(tab) {
        localStorage["current_url"] = tab.url;
        console.log(tab.url);
      });
    }
  });
});