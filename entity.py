import pygame
from tool import Tool

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spritesheet = pygame.image.load("./assets/sprites/hero_01_red_m_walk.png")
        self.image = Tool.split_image(self.spritesheet, 0, 0, 24, 32)
        self.position = [0, 0]
        self.rect: pygame.Rect = pygame.Rect(0, 0, 16, 32)

    def update(self):
        self.rect.topleft = self.position