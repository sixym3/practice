import json
from ocr import OCRNeuralNetwork
import BaseHTTPServer
import numpy as np

HOST_NAME = "localhost"
PORT_NUMBER = 8000

data_matrix = np.loadtxt(open("data.csv", "rb"), delimiter=",")
data_labels = np.loadtxt(open("dataLabels.csv", "rb"), delimiter=",")

nn = OCRNeuralNetwork(15, data_matrix, data_labels, list(range(5000)))

class JSONHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_POST(s):
        response_code = 200
        response = ""
        var_len = int(s.header.get("Content-Length"))
        content = s.rfile.read(var_len)
        payload = json.loads(content)
        
        if payload.get("train"):
            nn.train(payload["trainArray"])
            nn.save()
        elif payload.get("predict"):
            try:
                response = {
                    "type": "test",
                    "result": nn.predict(str(payload["image"]))
                }
            except:
                response_code = 500
        else:
            response_code = 400
        
        s.send_response(response_code)
        s.send_header("Content-type", "application/json")
        s.send_header("Access-Control-Allow-Origin", "*")
        s.end_headers()
        if response:
            s.wfile.write(json.dumps(response))
        return

if __name__ == "__main__":
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), JSONHandler)
    
    try:
        httpd.server_forever()
    except KeyboardInterrupt:
        pass
    else:
        print("Unexpected server exception occurred.")
    finally:
        httpd.server_close()