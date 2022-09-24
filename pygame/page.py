from cmath import e
from tkinter import E
import pygame
import json
import socket

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class page(object):
    def __init__(self, window, connection = None):
        self.COLS = self.ROWS = 90
        self.window = window
        self.BG = WHITE
        self.BORDER_THICKNESS = 2
        self.window_size = (self.window.get_width(), self.window.get_height())
        self.full_size = (self.window_size[0] - 1, self.window_size[1] - 1)
        self.board = self.create_board()
        self.x = 0
        self.y = 0
        self.status = None

        """
        Communication

        -1 - board not set
        1 - pull board data
        2 - push board data
        3 - disconnect
        """
        if connection:
            self.connection = connection

    def connection_status(self, status):
        self.status = status

        
    def download_board(self):
        if self.connection:
            try:
                response = self.send({1: []})
                self.board = response
            except Exception as e:
                print(e)
        

    def create_board(self):
        return [[(255,255,255) for _ in range(self.COLS)] for _ in range(self.ROWS)]
    
    def draw(self):
        self.window.fill(self.BG)
        pygame.draw.rect(self.window, BLACK, (self.x - self.BORDER_THICKNESS/2, self.y-self.BORDER_THICKNESS/2, self.window_size[0] + self.BORDER_THICKNESS, self.window_size[1] + self.BORDER_THICKNESS), self.BORDER_THICKNESS)
        for y, _ in enumerate(self.board):
            for x, col in enumerate(self.board[y]):
                pygame.draw.rect(self.window, col, (self.x + x*8, self.y + y*8, 8, 8), 0)
        # pygame.draw.rect(surface=self.window, color=BLACK, rect=self.full_size)
        pygame.display.update()

    def send(self, data):
        try:
            self.connection.send(json.dumps(data).encode())

            d = ""
            while 1:
                last = self.connection.recv(1024).decode()
                d += last
                try:
                    if d.count(".") == 1:
                        break
                except:
                    pass

            try:
                if d[-1] == ".":
                    d = d[:-1]
            except:
                pass

            keys = [key for key in data.keys()]
            return json.loads(d)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server:", msg)
        self.connection.close()

    def check_clicks(self):
        mouse = pygame.mouse.get_pos()
        selected_pixel = self.click(*mouse)

        if selected_pixel:
            try:
                response = self.send({2: selected_pixel})
                print(response)
            except Exception as e:
                print(e)

        self.update_board(*selected_pixel)

    def update_board(self, row, col, color=BLACK):
        self.board[col][row] = color

    def click(self,x,y):
        row = int((x - self.x)/8)
        col = int((y - self.y)/8)

        if 0 <= row < self.ROWS and 0 <= col < self.COLS:
            return row, col

        return None

    def center_window(self, event):
        if self.x < int((event.w - self.window_size[0]) / 2):
            self.x = int((event.w - self.window_size[0]) / 2)
        else:
            self.x = 0
        if self.y < int((event.h - self.window_size[1]) / 2):
            self.y = int((event.h - self.window_size[1]) / 2)
        else:
            self.y = 0

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            #clock.tick(25)
            if self.status == 'connected':
                self.download_board()
                
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif pygame.mouse.get_pressed()[0]:
                    self.check_clicks()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                elif event.type == pygame.VIDEORESIZE:
                    self.center_window(event)
        pygame.quit()
            

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode((720, 720), pygame.RESIZABLE)
    window = pygame.display.get_surface()
    board = page(window)
    board.run()