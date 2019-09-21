const server = "http://localhost:8000/";

document.getElementById("button-url").onclick = function () {
  const body = {
    url: localStorage["current_url"],
  };

  console.log('BODY IS', body);
  // alert(body.url);
  const parameters = {
    headers: {'Content-type': 'application/json'},
    body: JSON.stringify(body),
    method: "POST"
  };
  fetch(server, parameters).then(data=>{return data.json()}).then(res=>{
    document.getElementById("button-url").classList.add("hidden");
    document.getElementById("loader").classList.remove("hidden");
    setTimeout(() => {
      document.getElementById("loader").classList.add("hidden");
      document.getElementById("desc").classList.remove("hidden");
    }, 3000);
  }).catch((error) => {
    document.getElementById("button-url").classList.add("hidden");
    document.getElementById("loader").classList.remove("hidden");
    setTimeout(() => {
      document.getElementById("loader").classList.add("hidden");
      document.getElementById("error").classList.remove("hidden");
    }, 3000);
  });
}
