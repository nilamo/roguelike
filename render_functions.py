import util


def render_all(screen, entities, game_map, fov_map, colors):
    for y in range(game_map.height):
        for x in range(game_map.width):
            visible = fov_map[x][y]
            wall = game_map.tiles[x][y].block_sight

            color = None
            if visible:
                color = colors["light_wall"] if wall else colors["light_ground"]
                # keep track of what we've seen, so previously seen things are still visible
                game_map.tiles[x][y].explored = True
            elif game_map.tiles[x][y].explored:
                color = colors["dark_wall"] if wall else colors["dark_ground"]

            if color:
                color.x = x
                color.y = y
                draw_entity(screen, color, fov_map, True)

    # draw all entities in the list
    for entity in entities:
        draw_entity(screen, entity, fov_map)


def draw_entity(screen, entity, fov_map, bypass_fov=False):
    # only draw things that are within the player's view
    if bypass_fov or fov_map[entity.x][entity.y]:
        screen.blit(entity.surface, (util.to_pixel(entity.x), util.to_pixel(entity.y)))
