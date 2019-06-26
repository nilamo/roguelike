from .tile import Tile

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]

        for i in range(30, 33):
            tiles[i][22].blocked = True
            tiles[i][22].block_sight = True
        
        return tiles

    def is_blocked(self, x, y):
        return self.tiles[x][y].blocked

        