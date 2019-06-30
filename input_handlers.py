import pygame


def handle_keys(key):
    if key.type == pygame.KEYDOWN:
        button = key.key
        # movement keys
        if button == pygame.K_UP:
            return {"move": (0, -1)}
        if button == pygame.K_DOWN:
            return {"move": (0, 1)}
        if button == pygame.K_LEFT:
            return {"move": (-1, 0)}
        if button == pygame.K_RIGHT:
            return {"move": (1, 0)}

        if button == pygame.K_ESCAPE:
            return {"exit": True}

        mods = pygame.key.get_pressed()
        if button == pygame.K_RETURN and mods[pygame.K_RALT]:
            # Alt+Enter: toggle fullscreen
            return {"fullscreen": True}

    elif key.type == pygame.QUIT:
        return {"exit": True}
    return {}
