# font: https://www.dafont.com/speculum.font

import pygame
from input_handlers import handle_keys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLOCK_SIZE = 15

def to_pixel(block_num):
    return block_num * BLOCK_SIZE

def main():
    # in "block" units, not pixels
    screen_width = 80
    screen_height = 50
    is_fullscreen = False

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    size = (to_pixel(screen_width), to_pixel(screen_height))
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("roguelike pygame tutorial")
    character = pygame.image.load("res/character.png").convert_alpha()

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
                player_x += move_x
                player_y += move_y

        window.fill(BLACK)
        window.blit(character, (to_pixel(player_x), to_pixel(player_y)))
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
