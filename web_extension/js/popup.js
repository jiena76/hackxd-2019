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
    document.getElementById("button-url").classList.add("hidden");
    document.getElementById("loader").classList.remove("hidden");
    setTimeout(() => {
      document.getElementById("loader").classList.add("hidden");
      document.getElementById("desc").classList.remove("hidden");
    }, 3000);
  }).catch(error=>console.log(error));
}
