import pygame


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x, y, file_name):
        self.x = x
        self.y = y
        self.surface = self.load_image(file_name)

    def load_image(self, file_name):
        surface = pygame.image.load(f"res/{file_name}.png")
        return surface.convert_alpha()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
