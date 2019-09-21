const server = "http://localhost:8000/";

const userAction = async () => {
  const response = await fetch(server);
  localStorage["myJson"] = await response.json(); //extract JSON from the http response
  // do something with myJson
}

document.getElementById("button-url").onclick = function () {
  alert(localStorage["current_url"]);
}