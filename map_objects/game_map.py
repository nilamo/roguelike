import random
from .rectangle import Rect
from .tile import Tile


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def make_map(
        self, max_rooms, room_min_size, room_max_size, map_width, map_height, player
    ):
        rooms = []

        for r in range(max_rooms):
            # random width/height
            width = random.randint(room_min_size, room_max_size)
            height = random.randint(room_min_size, room_max_size)

            # random position inside the map
            x = random.randint(0, map_width - width - 1)
            y = random.randint(0, map_height - height - 1)

            # make sure this room doesn't touch any others
            new_room = Rect(x, y, width, height)
            for other in rooms:
                if new_room in other:
                    break
            else:
                self.create_room(new_room)

                center = new_room.center()
                if len(rooms) == 0:
                    # this is the first room, so set the player to start in it
                    player.x = center[0]
                    player.y = center[1]
                else:
                    # this isn't the first room, so connect it to the previous room with a tunnel
                    prev_center = rooms[-1].center()

                    # 50% random
                    if random.randint(0, 1) == 0:
                        # first horizonal, then vertical
                        self.create_h_tunnel(prev_center[0], center[0], prev_center[1])
                        self.create_v_tunnel(prev_center[1], center[1], center[0])
                    else:
                        self.create_v_tunnel(prev_center[1], center[1], prev_center[0])
                        self.create_h_tunnel(prev_center[0], center[0], center[1])

                # keep track of the room, so we can check for intersections next loop
                rooms.append(new_room)

    def create_room(self, rect):
        # go through the tiles in the rect and make them passable
        for x in range(rect.x1 + 1, rect.x2):
            for y in range(rect.y1 + 1, rect.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        for x in range(min_x, max_x + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        for y in range(min_y, max_y + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        return self.tiles[x][y].blocked
