import socket
import threading
import time
from client import client

class server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.recent_data = None
        self.connected_client = []

    def connection_thread(self):
        self.sock.listen(2)
        global stop_connection_thread

        while True:
            
            if stop_connection_thread:
                break

            client_socket, client_address = self.sock.accept()
            # if not client_address in [i.address for i in self.connected_client]:
            #     self.connected_client.append(client(client_socket, client_address))

            if client_socket:
                self.recent_data = client_socket.recv(1024).decode()
                if self.recent_data:
                    print(self.recent_data)
                            
                    client_socket.send("Reply: ".encode() + self.recent_data.encode())
                    ## self.authenticate(client_socket, client_address)
            
    def authenticate(client_socket, client_address):
        client(client_socket, client_address)

    def shutdown(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

    def send_to_client(self):
        pass
        
if __name__ == '__main__':
    stop_connection_thread = False

    s = server(host=socket.gethostname(), port=5050)
    server_thread = threading.Thread(target=s.connection_thread)
    server_thread.daemon = True
    server_thread.start()
    
    while True:
        command = input("host: ")
        command = command.strip()
        if command == "quit":
            s.shutdown()
            stop_connection_thread = True
            break
        # else:
        #     s.send_to_client()