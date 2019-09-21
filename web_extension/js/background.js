chrome.tabs.onActivated.addListener(function(activeInfo) {
  chrome.tabs.get(activeInfo.tabId, function(tab) {
    localStorage["current_url"] = tab.url;
    console.log(tab.url);
  });
});