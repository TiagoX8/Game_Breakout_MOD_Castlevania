import pygame,os

BLACK = (0, 0, 0)


def load_image(name):
    """carrega uma imagem na memoria"""
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print("Cannot load image:", fullname)
        raise SystemExit(message)
    return image, image.get_rect()
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # Define cor da Barra, sua largura e altura.
        # Defina a cor de fundo e defina-a como transparente
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(BLACK)

        # Carrega a imagem desejada
        self.image, self.rect = load_image('images/barra/Belm.png')
        # Ajuste o tamanho da imagem para corresponder ao tamanho da paddle
        self.image = pygame.transform.scale(self.image, (width, height))

        # Defina o objeto retângulo com as dimensões da imagem
        self.rect = self.image.get_rect()




    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # Verifique se você não está indo muito longe (fora da tela)
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        #Verifique se você não está indo muito longe (fora da tela)
        if self.rect.x > 660:
            self.rect.x = 660

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 500:
            self.rect.y = 500