const server = "http://localhost:8000/";

document.getElementById("button-url").onclick = function () {
  // alert(localStorage["current_url"]);
  const parameters = {
    headers: {'Content-type': 'text/html'},
    body: {ur: localStorage["current_url"]},
    method: "POST"
  };
  fetch(server, parameters).then(data=>{return data.json()}).then(res=>{
    console.log(res);
  }).catch(error=>console.log(error));
}