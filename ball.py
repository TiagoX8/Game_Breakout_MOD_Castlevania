import pygame,os,random
from random import randint

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


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height, velocity):
        super().__init__()
        self.screen_width = 800
        self.screen_height = 600
        self.image = pygame.Surface([width, height])
        self.image, self.rect = load_image('bolas/fogo.png')
        self.velocity = velocity


    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.choice([-8, -6, -4, 4, 6, 8])

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height



class BallB(pygame.sprite.Sprite):
    # Esta classe representa uma bola. Deriva da classe "Sprite" em Pygame.

    def __init__(self, color, width, height, initial_velocity):
        # Chame o construtor da classe pai (Sprite)
        super().__init__()

        # Passe na cor do carro, e sua posição x e y, largura e altura.
        # Defina a cor de fundo e defina-a como transparente
        self.image = pygame.Surface([width, height])
        self.image, self.rect = load_image('bolas/S.png')

        # Define a velocidade inicial da bola
        self.velocity = [0, initial_velocity]

    # O método update() desta classe será chamado para cada quadro do loop do programa principal. Ele se move ( altera as coordenadas ( x, y ) da bola usando seu vetor de velocidade.
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def set_velocity(self, velocity):
        self.velocity[1] = velocity

    def bounce(self):
        self.velocity[0] = -self.velocity[0]

        # Verifica se a velocidade no eixo x é diferente de zero
        if self.velocity[0] != 0:
            # Altera a direção vertical aleatoriamente, mas diferente de zero
            self.velocity[1] = randint(-8, 8)
            while self.velocity[1] == 0:
                self.velocity[1] = randint(-8, 8)

        self.collided = False


class BallVersus(pygame.sprite.Sprite):
    def __init__(self, width, height, velocity):
        super().__init__()
        self.screen_width = 800
        self.screen_height = 600
        self.image = pygame.Surface([width, height])
        self.image, self.rect = load_image('images/versus/caveira.png')
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]

        # Define uma direção vertical fixa após a colisão
        self.velocity[1] = random.choice([-8, -6, -4, 4, 6, 8])

        # Ajuste a posição da bola após a colisão
        self.rect.x += self.velocity[0] * 2
        self.rect.y += random.randint(-5, 5)

        # Verifique se a bola está dentro dos limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
