import pygame
from page import page
import socket

class software(object):
    def __init__(self, window, name=None):
        if name:
            self.name = name
        else: 
            self.name = input("Enter your name please:")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.target = (socket.gethostname(), 5050)
        self.page = page(window, self.socket)

    def connect(self):
        try:
            self.socket.connect(self.target)
            self.socket.send(f'{self.name}'.encode())
            response = self.socket.recv(1024).decode()
            self.page.connection_status(response)
        except Exception as e:
            print(e)
    
    

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode((720, 720), pygame.RESIZABLE)
    window = pygame.display.get_surface()
    s = software(window)
    s.connect()
    s.page.run()
    