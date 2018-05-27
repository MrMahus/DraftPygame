import pygame
import os


class Loader:

    def __init__(self):

        self.tile_collection = {

            0       :   None,    # Tile Transparent
            1       :   None,    # Tile Grass
            2       :   None,    # Tile 2
            3       :   None,    # Tile 3
            4       :   None,    # Tile 4
            5       :   None,    # Tile 5
            6       :   None,    # Tile 6
            7       :   None,    # Tile 7
            8       :   None,    # Tile 8

        }

        self.tile_width = 32
        self.tile_height = 32
        self.tile_rows = 20 - 1
        self.tile_cols = 20 - 1

        self.loadTilesFiles()


    def loadTilesFiles(self):

        for id in self.tile_collection:

            if os.path.exists("res/tiles/tile_" + str(id) + ".png") == True:

                self.tile_collection[id] =\
                    pygame.image.load("res/tiles/tile_" + str(id) + ".png").convert_alpha()

            else:
                self.tile_collection[id] = None


    def loadMapFile(self,_map_index):

        if os.path.exists("res/maps/map_" + str(_map_index[0])
                          + "_" + str(_map_index[1]) + ".txt"):

            file_map = open("res/maps/map_" + str(_map_index[0])
                          + "_" + str(_map_index[1]) + ".txt", "r")
            buffer = []

            for lines in file_map:
                buffer.append(lines.rstrip('\n'))

            file_map.close()

            current_layer = 1
            layer_1 = ''
            layer_2 = ''
            layer_3 = ''

            for element in buffer:

                if element == 'first_layer,':
                    current_layer = 1

                if element == 'second_layer,':
                    current_layer = 2

                if element == 'third_layer,':
                    current_layer = 3

                if current_layer == 1 and element != 'first_layer,':
                    layer_1 += element

                if current_layer == 2 and element != 'second_layer,':
                    layer_2 += element

                if current_layer == 3 and element != 'third_layer,':
                    layer_3 += element

            layer_1 = layer_1.replace(',', "")
            layer_1 = list(layer_1)

            layer_2 = layer_2.replace(',', "")
            layer_2 = list(layer_2)

            layer_3 = layer_3.replace(',', "")
            layer_3 = list(layer_3)

            map_infos = (layer_1, layer_2, layer_3)

            return map_infos

        else:
            #print("map file "+str(_map_index)+ " could not be read")
            return None


    def drawTileMap(self, _map_layers, _surface):

        if _map_layers != None:

            for layer in _map_layers:

                tile_xPos =  0
                tile_yPos =  0

                for cell in layer:
                    _surface.blit(self.tile_collection[int(cell)], (tile_xPos,tile_yPos))
                    if tile_xPos < self.tile_width*self.tile_cols:
                        tile_xPos += 32
                    else:
                        tile_xPos = 0
                        tile_yPos += 32


            return _surface