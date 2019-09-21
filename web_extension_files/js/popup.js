//  // If you prefer external files.
//  chrome.tabs.executeScript(null, {
//      "file": "bg_red.js"
//  })
// }

document.getElementById("button-url").onclick = function () {
  alert(localStorage["current_url"]);
}