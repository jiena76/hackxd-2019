# from . import text_processing

from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
  def _set_handlers(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    self._set_headers()
    self.wfile.write("Hello String!")

  # def do_POST(self):
  #   # 1. How long was the message?
  #   length = int(self.headers.get('Content-length', 0))

  #   # 2. Read the correct amount of data from the request.
  #   data = self.rfile.read(length).decode()

  #   # 3. Extract the "message" field from the request data.
  #   # message = parse_qs(data)["message"][0]

  #   # Send the "message" field back as the response.
  #   self._set_headers()
  #   self.wfile.write("Hello String!")
  #   # self.wfile.write(message.encode())

  def do_POST(self):
    # Doesn't do anything with posted data
    self._set_headers()
    self.wfile.write("<html><body><h1>POST!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler, port=8000):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print("The server begins----\t" + str(port))
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass
  httpd.server_close()
  print("The server ends------\t" + str(port))

if __name__ == "__main__":
  from sys import argv

  if len(argv) == 2:
      run(port=int(argv[1]))
  else:
      run()