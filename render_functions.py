import util


def render_all(screen, entities, game_map, colors):
    # draw all the tiles in the game map
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight

            color = colors["dark_wall"] if wall else colors["dark_ground"]
            color.x = x
            color.y = y
            draw_entity(screen, color)

    # draw all entities in the list
    for entity in entities:
        draw_entity(screen, entity)


def draw_entity(screen, entity):
    screen.blit(entity.surface, (util.to_pixel(entity.x), util.to_pixel(entity.y)))
