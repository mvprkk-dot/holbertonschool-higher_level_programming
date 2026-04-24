""" http.server example """
import http.server
import json

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    """ Custom request handler """
    def do_GET(self):
        """ Handle GET requests """
        if self.path == '/data':
            # Sample dataset
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            # Set the response code and headers
            self.send_response(200)  # HTTP status code 200 (OK)
            self.send_header('Content-Type', 'application/json')  # Set content type to JSON
            self.end_headers()  # End headers
            # Write the JSON data as a response
            self.wfile.write(json.dumps(sample_data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')  # Example response    # Convert dict to JSON and encode to bytes
        elif self.path == '/info':
            # Info endpoint
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info_data).encode('utf-8'))
        elif self.path == '/':
            # Handle the root path
            self.send_response(200)  # HTTP status code 200 (OK)
            self.send_header('Content-Type', 'text/plain')  # Set content type to plain text
            self.end_headers()  # End headers
            self.wfile.write(b'Hello, this is a simple API!')  # Write welcome message
        else:
            # Handle other paths
            self.send_response(404)  # HTTP status code 404 (Not Found)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()  # End headers
            self.wfile.write(b'Endpoint not found')  # Write error message

if __name__ == "__main__":
    # Create an HTTP server instance
    httpd = http.server.HTTPServer(('localhost', PORT), MyHandler)
    print(f"Serving on port {PORT}")  # Print server status
    httpd.serve_forever()  # Start the server
