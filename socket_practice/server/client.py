class client(object):
    def __init__(self, socket, address):
        self.socket = socket
        self.address = address
    
    def send(self, data):
        self.socket.send(data)