import pygame
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image_orig = pygame.image.load('images/versus/tijolo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_orig, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


