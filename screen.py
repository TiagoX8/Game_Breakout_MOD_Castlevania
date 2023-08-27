import pygame
def show_story_scene1(self):
    # Código para exibir a primeira cena da história
    # Exemplo:

    self.screen.fill((0, 0, 0))
    self.backgroundh = pygame.image.load("images/fundo.jpg")
    self.screen.blit(self.backgroundh, (0, 0))

    # Configurações do balão
    balao_cor = (0, 0, 0)  # Cor do balão
    balao_borda = 6  # Espessura da borda do balão
    balao_padding = 70  # Espaçamento entre o texto e a borda do balão

    # Configurações do texto
    fonte = pygame.font.Font(None, 34)
    texto = "Acho que meu pai Acordou, Preciso ir ver o que está acontecendo."
    talk_1 = pygame.mixer.Sound('Sounds/Falas/alucard.mpeg')
    talk_1.play()
    texto_renderizado = fonte.render(texto, True, (255, 0, 0))

    # Dimensões do balão baseadas no tamanho do texto
    largura_balao = texto_renderizado.get_width() + 2 * balao_padding
    altura_balao = texto_renderizado.get_height() + 2 * balao_padding

    # Posição do balão
    x_balao = 10
    y_balao = 450

    balao_rect = pygame.Rect(x_balao, y_balao, largura_balao, altura_balao)

    self.image = pygame.image.load("images/Alucard.png")
    self.screen.blit(self.image, (20, 200))

    # Desenha o balão
    pygame.draw.rect(self.screen, balao_cor, balao_rect)
    pygame.draw.rect(self.screen, (20, 20, 50), balao_rect, balao_borda)

    # Posiciona o texto dentro do balão
    x_texto = 40
    y_texto = 520
    self.screen.blit(texto_renderizado, (x_texto, y_texto))

    pygame.display.flip()
    pygame.time.wait(5000)

    # segundo quadro

    self.screen.fill((0, 0, 0))
    self.backgroundh = pygame.image.load("images/backf.jpg")
    self.screen.blit(self.backgroundh, (20, 0))

    # Configurações do balão
    balao_cor = (0, 0, 0)  # Cor do balão
    balao_borda = 6  # Espessura da borda do balão
    balao_padding = 70  # Espaçamento entre o texto e a borda do balão

    # Configurações do texto
    fonte = pygame.font.Font(None, 32)
    texto = "Oh, Jovem Mestre, me parece que o Senhor Drácula despertou."
    talk_2 = pygame.mixer.Sound('Sounds/Falas/veio.mpeg')
    talk_2.play()
    texto_renderizado = fonte.render(texto, True, (255, 0, 0))

    # Dimensões do balão baseadas no tamanho do texto
    largura_balao = texto_renderizado.get_width() + 2 * balao_padding
    altura_balao = texto_renderizado.get_height() + 2 * balao_padding

    # Posição do balão
    x_balao = 10
    y_balao = 450

    balao_rect = pygame.Rect(x_balao, y_balao, largura_balao, altura_balao)

    self.image = pygame.image.load("images/biblio.png")
    self.screen.blit(self.image, (0, 240))

    # Desenha o balão
    pygame.draw.rect(self.screen, balao_cor, balao_rect)
    pygame.draw.rect(self.screen, (20, 20, 50), balao_rect, balao_borda)

    # Posiciona o texto dentro do balão
    x_texto = 40
    y_texto = 520
    self.screen.blit(texto_renderizado, (x_texto, y_texto))

    pygame.display.flip()
    pygame.time.wait(5000)

    # terceiro quadro

    self.screen.fill((0, 0, 0))
    self.backgroundh = pygame.image.load("images/backf.jpg")
    self.screen.blit(self.backgroundh, (20, 0))

    # Configurações do balão
    balao_cor = (0, 0, 0)  # Cor do balão
    balao_borda = 6  # Espessura da borda do balão
    balao_padding = 70  # Espaçamento entre o texto e a borda do balão

    # Configurações do texto
    fonte = pygame.font.Font(None, 36)
    texto = "Sim! Será que ele continuará com aquele plano louco?"
    talk_3 = pygame.mixer.Sound('Sounds/Falas/alucard2.mp3')
    talk_3.play()
    texto_renderizado = fonte.render(texto, True, (255, 0, 0))

    # Dimensões do balão baseadas no tamanho do texto
    largura_balao = texto_renderizado.get_width() + 2 * balao_padding
    altura_balao = texto_renderizado.get_height() + 2 * balao_padding

    # Posição do balão
    x_balao = 10
    y_balao = 450

    balao_rect = pygame.Rect(x_balao, y_balao, largura_balao, altura_balao)

    self.image = pygame.image.load("images/Alucardinv.png")
    self.screen.blit(self.image, (560, 270))

    # Desenha o balão
    pygame.draw.rect(self.screen, balao_cor, balao_rect)
    pygame.draw.rect(self.screen, (20, 20, 50), balao_rect, balao_borda)

    # Posiciona o texto dentro do balão
    x_texto = 40
    y_texto = 520
    self.screen.blit(texto_renderizado, (x_texto, y_texto))

    pygame.display.flip()
    pygame.time.wait(5000)

    # Quarto quadro

    self.screen.fill((0, 0, 0))
    self.backgroundh = pygame.image.load("images/backf.jpg")
    self.screen.blit(self.backgroundh, (20, 0))

    # Configurações do balão
    balao_cor = (0, 0, 0)  # Cor do balão
    balao_borda = 6  # Espessura da borda do balão
    balao_padding = 70  # Espaçamento entre o texto e a borda do balão

    # Configurações do texto
    fonte = pygame.font.Font(None, 22)
    texto = "Antes de adormecer ele queria a extinção dos humanos, talvez irá buscar isso novamente."
    talk_4 = pygame.mixer.Sound('Sounds/Falas/veio2.mp3')
    talk_4.play()
    texto_renderizado = fonte.render(texto, True, (255, 0, 0))

    # Dimensões do balão baseadas no tamanho do texto
    largura_balao = texto_renderizado.get_width() + 2 * balao_padding
    altura_balao = texto_renderizado.get_height() + 2 * balao_padding

    # Posição do balão
    x_balao = 10
    y_balao = 450

    balao_rect = pygame.Rect(x_balao, y_balao, largura_balao, altura_balao)

    self.image = pygame.image.load("images/biblio.png")
    self.screen.blit(self.image, (0, 240))

    # Desenha o balão
    pygame.draw.rect(self.screen, balao_cor, balao_rect)
    pygame.draw.rect(self.screen, (20, 20, 50), balao_rect, balao_borda)

    # Posiciona o texto dentro do balão
    x_texto = 40
    y_texto = 520
    self.screen.blit(texto_renderizado, (x_texto, y_texto))

    pygame.display.flip()
    pygame.time.wait(5000)

    # terceiro quadro

    self.screen.fill((0, 0, 0))
    self.backgroundh = pygame.image.load("images/backf.jpg")
    self.screen.blit(self.backgroundh, (20, 0))

    # Configurações do balão
    balao_cor = (0, 0, 0)  # Cor do balão
    balao_borda = 6  # Espessura da borda do balão
    balao_padding = 70  # Espaçamento entre o texto e a borda do balão

    # Configurações do texto
    fonte = pygame.font.Font(None, 36)
    texto = "Não posso deixar que isso aconteça!"
    talk_5 = pygame.mixer.Sound('Sounds/Falas/alucard3.mp3')
    talk_5.play()
    texto_renderizado = fonte.render(texto, True, (255, 0, 0))

    # Dimensões do balão baseadas no tamanho do texto
    largura_balao = texto_renderizado.get_width() + 2 * balao_padding
    altura_balao = texto_renderizado.get_height() + 2 * balao_padding

    # Posição do balão
    x_balao = 10
    y_balao = 450

    balao_rect = pygame.Rect(x_balao, y_balao, largura_balao, altura_balao)

    self.image = pygame.image.load("images/Alucardinv.png")
    self.screen.blit(self.image, (560, 270))

    # Desenha o balão
    pygame.draw.rect(self.screen, balao_cor, balao_rect)
    pygame.draw.rect(self.screen, (20, 20, 50), balao_rect, balao_borda)

    # Posiciona o texto dentro do balão
    x_texto = 40
    y_texto = 520
    self.screen.blit(texto_renderizado, (x_texto, y_texto))

    pygame.display.flip()
    pygame.time.wait(5000)