const server = "http://localhost:8000/";

document.getElementById("button-url").onclick = function () {
  const body = {
    url: localStorage["current_url"],
  };
  // alert(body.url);
  const parameters = {
    headers: {'Content-type': 'application/json'},
    body: JSON.stringify(body),
    method: "POST"
  };
  fetch(server, parameters).then(data=>{return data.json()}).then(res=>{
    print(res.json["url"])
  }).catch(error=>console.log(error));
}
