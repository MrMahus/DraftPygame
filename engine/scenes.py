import pygame


class Map:

    def __init__(self, _display_settings):

        self.map_size = _display_settings

        self.current_map = [0,0]
        self.north_map =        []
        self.northwest_map =    []
        self.northeast_map =    []
        self.east_map =         []
        self.west_map =         []
        self.south_map =        []
        self.southeast_map =    []
        self.southwest_map =    []

        self.current_map_layers     = []
        self.north_map_layers       = []
        self.northwest_map_layers   = []
        self.northeast_map_layers   = []
        self.east_map_layers        = []
        self.west_map_layers        = []
        self.south_map_layers       = []
        self.southeast_map_layers   = []
        self.southwest_map_layers   = []


        self.current_map_surface = pygame.Surface(_display_settings)
        self.north_map_surface = pygame.Surface(_display_settings)
        self.northwest_map_surface = pygame.Surface(_display_settings)
        self.northeast_map_surface = pygame.Surface(_display_settings)
        self.east_map_surface = pygame.Surface(_display_settings)
        self.west_map_surface = pygame.Surface(_display_settings)
        self.south_map_surface = pygame.Surface(_display_settings)
        self.southeast_map_surface = pygame.Surface(_display_settings)
        self.southwest_map_surface = pygame.Surface(_display_settings)

        self.updateMapsArroundPlayer()



    def updateMapsArroundPlayer(self):

        self.north_map =        [ self.current_map[0]    ,  self.current_map[1] - 1 ]
        self.northwest_map =    [ self.current_map[0] - 1,  self.current_map[1] - 1 ]
        self.northeast_map =    [ self.current_map[0] + 1,  self.current_map[1] - 1 ]
        self.east_map =         [ self.current_map[0] + 1,  self.current_map[1] ]
        self.west_map =         [ self.current_map[0] - 1,  self.current_map[1] ]
        self.south_map =        [ self.current_map[0],  self.current_map[1] + 1 ]
        self.southeast_map =    [ self.current_map[0] + 1,  self.current_map[1] + 1 ]
        self.southwest_map =    [ self.current_map[0] - 1,  self.current_map[1] + 1 ]



    def loadMaps(self, _loader):

        self.current_map_layers =      _loader.loadMapFile(self.current_map)
        self.north_map_layers =        _loader.loadMapFile(self.north_map)
        self.northwest_map_layers =    _loader.loadMapFile(self.northwest_map)
        self.northeast_map_layers =    _loader.loadMapFile( self.northeast_map)
        self.east_map_layers =         _loader.loadMapFile( self.east_map)
        self.west_map_layers =         _loader.loadMapFile(self.west_map)
        self.south_map_layers =        _loader.loadMapFile(self.south_map)
        self.southeast_map_layers =    _loader.loadMapFile(self.southeast_map)
        self.southwest_map_layers =    _loader.loadMapFile(self.southwest_map)

    def drawMapsSurface(self, _loader):

        self.current_map_surface =      _loader.drawTileMap(self.current_map_layers, self.current_map_surface)
        self.north_map_surface =        _loader.drawTileMap(self.north_map_layers, self.north_map_surface)
        self.northwest_map_surface =    _loader.drawTileMap(self.northwest_map_layers, self.northwest_map_surface)
        self.northeast_map_surface =    _loader.drawTileMap(self.northeast_map_layers, self.northeast_map_surface)
        self.east_map_surface =         _loader.drawTileMap(self.east_map_layers, self.east_map_surface)
        self.west_map_surface =         _loader.drawTileMap(self.west_map_layers, self.west_map_surface)
        self.south_map_surface =        _loader.drawTileMap(self.south_map_layers, self.south_map_surface)
        self.southeast_map_surface =    _loader.drawTileMap(self.southeast_map_layers, self.southeast_map_surface)
        self.southwest_map_surface =    _loader.drawTileMap(self.southwest_map_layers, self.southwest_map_surface)



    def assembleMapsTogether(self, _display, _player_pos):

        if self.current_map_surface != None:
            _display.blit(self.current_map_surface, _player_pos)
        if self.north_map_surface != None:
            _display.blit(self.north_map_surface, (_player_pos[0], _player_pos[1]-self.map_size[1]))
        if self.south_map_surface != None:
            _display.blit(self.south_map_surface, (_player_pos[0], _player_pos[1]+self.map_size[1]))
        if self.west_map_surface != None:
            _display.blit(self.west_map_surface, (_player_pos[0] - self.map_size[0], _player_pos[1]))
        if self.east_map_surface != None:
            _display.blit(self.east_map_surface, (_player_pos[0] + self.map_size[0], _player_pos[1]))
        if self.northwest_map_surface != None:
            _display.blit(self.northwest_map_surface, (_player_pos[0]- self.map_size[0], _player_pos[1]-self.map_size[1]))
        if self.northeast_map_surface != None:
            _display.blit(self.northeast_map_surface, (_player_pos[0]+ self.map_size[0], _player_pos[1]-self.map_size[1]))
        if self.southwest_map_surface != None:
            _display.blit(self.southwest_map_surface, (_player_pos[0] - self.map_size[0], _player_pos[1]+self.map_size[1]))
        if self.southeast_map_surface != None:
            _display.blit(self.southeast_map_surface, (_player_pos[0] + self.map_size[0], _player_pos[1]+self.map_size[1]))





    def update(self, _loader):
        self.updateMapsArroundPlayer()
        self.loadMaps(_loader)



    def draw(self, _loader, _display, _player_pos):
        self.drawMapsSurface(_loader)
        self.assembleMapsTogether(_display, _player_pos)
