#!/usr/bin/python3

import http.server
from http.server import BaseHTTPRequestHandler
import socketserver
import requests
import json



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):


    def do_GET(self):

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                    }

            self.wfile.write(json.dumps(data).encode("utf-8"))


        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                    "version": "1.0",
                    "description": "A simple API buit with http.server"
                    }

            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
            


PORT = 8000
Handler = SimpleHTTPRequestHandler
 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
     print("serving at port", PORT)
     httpd.serve_forever()
