const server = "http://localhost:8000/";

document.getElementById("button-url").onclick = function () {
  // alert(localStorage["current_url"]);
  const body = {
    url: localStorage["current_url"],
  };
  const parameters = {
    headers: {'Content-type': 'application/json'},
    body: JSON.stringify(body),
    method: "POST"
  };
  fetch(server, parameters).then(data=>{return data.json()}).then(res=>{
    console.log(res);
  }).catch(error=>console.log(error));
}
