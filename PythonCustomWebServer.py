#	Python Custom Web Server 
#	[ Following Tutorial on: https://pythonbasics.org/webserver/ ]
#	Author: Nikos-Nikitas
#	GitHub: nikosnikitas


#	importing request handler and server from python's built-in server
from http.server import BaseHTTPRequestHandler, HTTPServer
#	importing time to use time functions
import time

#	declaring host and port of our server
host = "localhost"
port = 5000

#	making the server class that responds, sends headers 
#	and creates a starting welcome page
#	self.path returns the path entered in the url
class TheServer(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header("content-type","text/html")
		self.end_headers()
		self.wfile.write(bytes("<html><head><title>My Web Server</title></head>","utf-8"))
		self.wfile.write(bytes("<p>Request: %s </p>" % self.path, "utf-8"))
		self.wfile.write(bytes("<body>","utf-8"))
		self.wfile.write(bytes("<p><strong>My Web Server</strong></p>","utf-8"))
		self.wfile.write(bytes("</body></html>","utf-8"))

#	creating, initializing and running the server when program starts
if __name__ == "__main__":
	
	myServer = HTTPServer((host,port),TheServer)
	print("Server initialized at: [ http://%s:%s ]" % (host, port))
	
	#	serving but interrupting when control/command + c keys are pressed
	#	causing the program to stop
	try:
		myServer.serve_forever()
		
	except KeyboardInterrupt:
		pass
		print("KeyboardInterrupt. Stopping...")
		
	myServer.server_close()
	print("Server has stopped.")
