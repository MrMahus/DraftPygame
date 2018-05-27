import pygame
import time

from engine.window import Window
from engine.events import Events
from engine.loader import Loader
from engine.scenes import Map
from engine.entities.player import Player


# ----- Initialisation ------
        # Pygame
pygame.init()

        # Window
game_window = Window()
game_display = game_window.game_display
game_window_settings = game_window.getWindowSize()


        # Events
loop = True
event_manager = Events()


        # Loader
loader = Loader()


        # Entities
user_player = Player()


        #Scenes
map_manager = Map(game_window_settings)
map_manager.loadMaps(loader)


        # Time
clock = pygame.time.Clock()




# ------ Main game loop -----


while(loop):

    # Time
    start_time = time.time()

    # Get events
    event_manager.processEvent()

    # Clear screen
    game_display.fill(game_window.black)

    # Update datas
    user_player.updatePlayer(event_manager.getKeyStates())
    map_manager.update(loader)

    # Draw things
    map_manager.draw(loader, game_display, user_player.getPlayerPos())
    user_player.drawPlayer(game_display, game_window_settings)



    # Flip screen
    pygame.display.flip()

    # Set framerate
    clock.tick(30)
    framerate = 1 / (time.time() - start_time)
    FPS = "FPS : "+ str(int(framerate))

    pygame.display.set_caption(FPS)


pygame.quit()
quit()