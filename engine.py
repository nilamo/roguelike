# font: https://www.dafont.com/speculum.font

import pygame

from entity import Entity
from fov_functions import initialize_fov, recompute_fov
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import render_all
import util

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    # in "block" units, not pixels
    screen_width = 80
    screen_height = 45
    map_width = 80
    map_height = 45
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    max_monsters_per_room = 3
    is_fullscreen = False

    fov_light_walls = True
    fov_radius = 10
    fov_recompute = True

    size = (util.to_pixel(screen_width), util.to_pixel(screen_height))
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("roguelike pygame tutorial")

    colors = {
        "dark_wall": Entity(0, 0, "dark_wall"),
        "dark_ground": Entity(0, 0, "dark_ground"),
        "light_wall": Entity(0, 0, "light_wall"),
        "light_ground": Entity(0, 0, "light_ground"),
    }

    player = Entity(0, 0, "character")
    entities = [player]

    game_map = GameMap(map_width, map_height)
    game_map.make_map(
        max_rooms,
        room_min_size,
        room_max_size,
        map_width,
        map_height,
        player,
        entities,
        max_monsters_per_room,
    )

    fov_map = initialize_fov(game_map)

    running = True
    while running:
        for event in pygame.event.get():
            action = handle_keys(event)
            if action.get("exit"):
                running = False
            elif action.get("fullscreen"):
                is_fullscreen = not is_fullscreen
                flags = pygame.FULLSCREEN if is_fullscreen else 0
                window = pygame.display.set_mode(size, flags)
            elif "move" in action:
                move_x, move_y = action["move"]
                if not game_map.is_blocked(player.x + move_x, player.y + move_y):
                    player.move(move_x, move_y)
                    fov_recompute = True

        if fov_recompute:
            fov_map = recompute_fov(
                game_map, player.x, player.y, fov_radius, fov_light_walls
            )

        window.fill(BLACK)
        render_all(window, entities, game_map, fov_map, colors)
        fov_recompute = False
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
