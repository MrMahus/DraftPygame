import pygame

class Window:

    def __init__(self):

        self.window_width = 640
        self.window_height = 640
        self.window_caption = 'Title'
        self.window_framerate = 60
        self.game_display = None

        self.createWindow()

        # Color constants

        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.black = (0,0,0)


    def createWindow(self):

        self.game_display = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(self.window_caption)


    def getWindowSize(self):
        return (self.window_width, self.window_height)
