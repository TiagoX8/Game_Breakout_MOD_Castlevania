import pygame
BLACK = (0,0,0)

class Brick(pygame.sprite.Sprite):
    #Esta classe representa um tijolo. Deriva da classe "Sprite" no Pygame.

    def __init__(self, color, width, height, letter ):
        #Chame o construtor da classe pai (Sprite)
        super().__init__()

        #Passe na cor do tijolo, e sua posição x e y, largura e altura.
        #Defina a cor de fundo e defina-a como transparente
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(BLACK)

        #Desenhe o tijolo (um retângulo!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #Busca o objeto retângulo que tem as dimensões da imagem.
        self.rect = self.image.get_rect()

        self.letter = letter  # Adicione o atributo 'letter' e atribua a letra correspondente ao tijolo
        self.color = color  # Adiciona o atributo 'color' à classe Brick
