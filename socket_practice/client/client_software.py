import socket
import threading
import time

class client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.recent_data = None

    def client_thread(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if not data:
                    break
                print(data)
                self.recent_data = data
            except socket.error:
                break

    def send(self, data):
        self.sock.send(data.encode())

if __name__ == '__main__':
    last_data = None

    s = client(host=socket.gethostname(), port=5002)
    client_thread = threading.Thread(target=s.client_thread)
    client_thread.daemon = True
    client_thread.start()
    
    while True:
        if last_data != s.recent_data:
            print(s.recent_data)
            last_data = s.recent_data
        s.send(input("Client: "))
