from browser import document, alert

def hello(ev):
  alert("Hello !")

document["button0"].bind("click", hello)