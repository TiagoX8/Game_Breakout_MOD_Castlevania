# Importar a biblioteca pygame
import pygame
# Importar a classe Paddle(Barra)
from paddle import Paddle
# Importar a classe Ball(bola)
from ball import Ball,BallB,BallVersus
# Importar a classe Brick(tijolo)
from brick import Brick
from Obstacle import Obstacle
import sys
import os
import time
from screen import show_story_scene1
import pygame.mixer
from moviepy.editor import VideoFileClip



# inicializar o jogo


class Menu:
    def __init__(self):
        pygame.init()
        self.name = None
        self.screen = pygame.display.set_mode((800, 600))
        self.size = (800, 600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Menu")
        self.background = pygame.image.load("images/castle.png")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("fontes/ghosthey-Regular.ttf", 36)
        self.menu_items = ["Play", "Versus Mode", "Didact Mode", "Exit"]
        self.selected_item = 0
        self.music_playing = False  # Flag para controlar a reprodução da música principal


    @staticmethod
    def save_score( score, name):
        with open('scores.txt', 'a') as file:
            file.write(f'{score},{name}\n')

    def load_scores(self):
        scores = []
        with open('scores.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                score, name = line.strip().split(',')
                scores.append((int(score), name))
        scores.sort(reverse=True)
        return scores[:3]



    def show_top_3(self):
        scores = self.load_scores()
        font = pygame.font.Font(None, 24)
        text_color = (255, 0, 0)

        y = 70
        for i, (score, name) in enumerate(scores):
            text = font.render(f'{i + 1}. {name}: {score}', True, text_color)
            text_rect = text.get_rect(x=30, y=y)  # Defina a coordenada x desejada
            self.screen.blit(text, text_rect)
            y += 50

    def pause(self):
        pause_items = ["Resume", "Menu"]
        selected_item = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_item = (selected_item - 1) % len(pause_items)
                    elif event.key == pygame.K_DOWN:
                        selected_item = (selected_item + 1) % len(pause_items)
                    elif event.key == pygame.K_RETURN:
                        return selected_item

            WHITE = (255, 255, 255)
            font = pygame.font.Font(None, 74)
            text = font.render("PAUSE", 1, WHITE)
            self.screen.blit(text, (300, 200))

            for i, item in enumerate(pause_items):
                if i == selected_item:
                    text = self.font.render(item, True, (255, 255, 255))
                else:
                    text = self.font.render(item, True, (128, 128, 128))
                self.screen.blit(text, (400 - text.get_width() // 2, 300 + i * 50))

            pygame.display.flip()
            self.clock.tick(60)

    def over(self, score):
        name = ""  # Variável para armazenar o nome do jogador
        pygame.mixer.music.load("Sounds/Requiem of the Gods.mp3")
        pygame.mixer.music.play(-1)  # -1 significa reprodução em loop contínuo



        name_entered = False  # Flag para indicar se o jogador já digitou o nome
        while not name_entered:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        name_entered = True  # Define a flag como True para sair do loop
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]  # Remove o último caractere do nome
                    else:
                        name += event.unicode  # Adiciona o caractere digitado ao nome

            # Limpa a tela
            self.screen.fill((0, 0, 0))

            # Renderiza o texto para inserção do nome
            font_1 = pygame.font.Font("fontes/ghosthey-Regular.ttf", 32)
            WHITE = (255, 255, 255)
            font = pygame.font.Font("fontes/ghosthey-Regular.ttf", 34)
            text = font.render("GAME OVER", 1, WHITE)
            self.screen.blit(text, (260, 200))
            text = font_1.render("Digite seu nome: " + name, True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(text, text_rect)

            # Atualiza a tela
            pygame.display.flip()


        self.save_score(score, name)

        # Menu
        options = ["Restart", "Menu"]
        selected_option = 0

        while True:
            # Limpa a tela
            self.screen.fill((0, 0, 0))

            # Renderiza o texto do nome
            name_text = font.render("Nome: " + name, True, (255, 255, 255))
            name_text_rect = name_text.get_rect(center=(self.screen.get_width() // 2, 50))
            self.screen.blit(name_text, name_text_rect)

            # Renderiza as opções do menu
            for i, option in enumerate(options):
                if i == selected_option:
                    color = (255, 255, 0)  # Destaca a opção selecionada
                else:
                    color = (255, 255, 255)
                option_text = font.render(option, True, color)
                option_text_rect = option_text.get_rect(center=(self.screen.get_width() // 2, 200 + i * 50))
                self.screen.blit(option_text, option_text_rect)

            # Atualiza a tela
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(options)  # Seleciona a opção anterior
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(options)  # Seleciona a próxima opção
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 0:
                            pygame.mixer.music.stop()
                            self.play_game()  # Reinicia o jogo
                        elif selected_option == 1:
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Volta para o menu principal

    def show_options(self):
        restart_selected = True  # para indicar se a opção de reinício está selecionada
        menu_selected = False  # para indicar se a opção de menu está selecionada

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        # Alterna entre as opções de reinício e menu
                        restart_selected = not restart_selected
                        menu_selected = not menu_selected
                    elif event.key == pygame.K_RETURN:
                        if restart_selected:
                            self.play_game()  # Chama a função de restart
                        elif menu_selected:
                            menu.run()  # Chama a função de menu

    def run(self):
        pygame.mixer.music.load("sounds/intro.mp3")
        pygame.mixer.music.play(-1)  # Reproduz a música principal em loop
        self.music_playing = True  # Define a flag como True
        running = True
        self.screen.fill((0, 0, 0))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                    elif event.key == pygame.K_DOWN:
                        self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_item == 0:
                            self.play_game()
                        elif self.selected_item == 1:
                            self.play_versus_mode()
                        elif self.selected_item == 2:
                            self.play_didact_mode()
                        elif self.selected_item == 3:
                            running = False


            if self.selected_item == 2:
                self.background_2 = pygame.image.load("images/fundoinfantil.jpg")
                self.screen.blit(self.background_2, (0, 0))
                pygame.mixer.music.pause()  # musica da intro para
                pygame.mixer.music.play()  # musica da intro para
            else:

                self.screen.blit(self.background, (0, 0))  # Use o background padrão para os outros itens




            #self.show_top_3()

            for i, item in enumerate(self.menu_items):
                if i == self.selected_item:
                    text = self.font.render(item, True, (255, 0, 0))
                else:
                    text = self.font.render(item, True, (255, 255, 255))
                self.screen.blit(text, (150 - text.get_width() // 2, 220 + i * 60))

            pygame.display.flip()
            self.clock.tick(60)

    def play_game(self):
        # Adicione aqui a lógica para iniciar o jogo principal
        # Definir algumas cores
        WHITE = (255, 255, 255)
        DARKBLUE = (36, 90, 190)
        LIGHTBLUE = (0, 176, 240)
        RED = (255, 0, 0)
        ORANGE = (255, 100, 0)
        YELLOW = (255, 255, 0)
        BOSS = (255, 0, 0)
        pygame.mixer.music.stop()  # musica da intro para

        intro_video  = VideoFileClip("Cutscene/cutini.mp4")
        intro_video.preview()
        show_story_scene1(self)

        # Pontuação
        score = 0

        lives = 10

        # O jogo será executado em sua própria janela, para a qual você pode decidir um título, uma largura e uma altura
        size = (800, 600)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Breakout Game")
        background = pygame.image.load("images/fundo2.jpg")
        pygame.mixer.music.load("Sounds/soundtracks/f1.mpeg")
        pygame.mixer.music.play(-1)  # -1 significa reprodução em loop contínuo

        # Esta será uma lista que conterá todos os sprites que pretendemos utilizar em nosso jogo.
        all_sprites_list = pygame.sprite.Group()

        # Crie a Barra
        paddlePong = Paddle(WHITE, 150, 25)
        paddlePong.rect.x = 350
        paddlePong.rect.y = 580

        # Crie o sprite da bola
        ball = Ball(WHITE, 10, 10, [7, 7])
        ball.rect.x = 345
        ball.rect.y = 295

        # Crie o sprite das bola/ataque
        ballB = BallB(WHITE, 10, 10, 8)
        ballB.rect.x = 400
        ballB.rect.y = 20

        ballC = BallB(WHITE, 10, 10, 8)
        ballC.rect.x = 400
        ballC.rect.y = 20

        ballD = BallB(WHITE, 10, 10, 8)
        ballD.rect.x = 400
        ballD.rect.y = 20

        ballB_start_pos = (ballB.rect.x, ballB.rect.y)
        ballC_start_pos = (ballB.rect.x, ballB.rect.y)
        ballD_start_pos = (ballB.rect.x, ballB.rect.y)
        separation_distance = 5
        # criamos três linhas de tijolos e as adicionamos a um grupo chamado all_bricks.
        all_bricks = pygame.sprite.Group()

        for i in range(1):
            for i in range(1):
                BOSS_brick = Brick(BOSS, 80, 80, 0)  # bloco do boss
                BOSS_brick.rect.x = 350
                BOSS_brick.rect.y = 50
                BOSS_brick.image = pygame.image.load("images/Skele.png").convert_alpha()
                all_sprites_list.add(BOSS_brick)
                all_bricks.add(BOSS_brick)
        for i in range(12):
            brick = Brick(ORANGE, 70, 60, 0)
            brick.rect.x = 40 + i * 60
            brick.rect.y = 130
            brick.image = pygame.image.load("images/block/block.png").convert()
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(0):
            brick = Brick(YELLOW, 70, 30, 0)
            brick.rect.x = 20 + i * 100
            brick.rect.y = 140
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        # Fim do codigo tijolos

        # Adicionando a Barra(paddle) e a bola(ball) à lista de sprites
        all_sprites_list.add(ball)
        all_sprites_list.add(paddlePong)

        all_sprites_list.add(ballB)
        all_sprites_list.add(ballC)
        all_sprites_list.add(ballD)

        # O loop continuará até que o usuário saia do jogo (por exemplo, clique no botão Fechar).
        carryOn = True

        # O relógio será usado para controlar a rapidez com que a tela é atualizada
        clock = pygame.time.Clock()

        # -------- Loop do programa principal -----------
        BOSS_brick_hits = 0  # numero inicial de vidas do bloco
        last_spawn_time = 0 #para pegar o tempo inicial para o lance do ataque
        has_collided_recently = False #para evitar um loop vertical
        while carryOn:

            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - last_spawn_time

            if elapsed_time >= 5000:
                all_sprites_list.add(ballB)
                all_sprites_list.add(ballC)
                all_sprites_list.add(ballD)
                ballB.rect.x = 400
                ballB.rect.y = 80
                ballC.rect.x = 400
                ballC.rect.y = 80
                ballD.rect.x = 400
                ballD.rect.y = 80
                last_spawn_time = current_time


            # --- Loop de evento principal
            for event in pygame.event.get():  # O usuário fez algo
                if event.type == pygame.QUIT:  # Se o usuário clicou em fechar
                    carryOn = False  # Sinalize que terminamos, então saímos deste loop
                    menu.run()  # Retorna ao menu principal
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        carryOn = False  # Termina o loop principal
                        menu.run()  # Retorna ao menu principal

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    selected_option = self.pause()
                    if selected_option == 0:
                        continue  # Continua o Jogo de onde Parou
                    elif selected_option == 1:
                        carryOn = False  # Para o Loop
                        menu.run()  # Retorna para o menu inicial

            # Movendo a Barra quando o uso usa as teclas de seta
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddlePong.moveLeft(10)
            if keys[pygame.K_RIGHT]:
                paddlePong.moveRight(10)

            # --- A lógica do jogo deve ir aqui
            ballB.rect.x, ballB.rect.y = ballB.rect.x - separation_distance, ballB.rect.y + separation_distance
            ballC.rect.x, ballC.rect.y = ballC.rect.x, ballC.rect.y + separation_distance
            ballD.rect.x, ballD.rect.y = ballD.rect.x + separation_distance, ballD.rect.y + separation_distance

            all_sprites_list.update()
            if pygame.sprite.collide_rect(ballB, paddlePong):
                if not ballB.collided:
                    effect = pygame.mixer.Sound('Sounds/damn.mp3')
                    effect.play()
                    lives -= 1
                    ballB.collided = True
                    if lives == 0:
                        # Efeito sonoro game over
                        effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                        effect.play()

                        # Chamando a função game over
                        selected_option = self.over(score)
                        if selected_option == 0:
                            carryOn = False  # Para o Loop
                            self.play_game()
                        elif selected_option == 1:
                            carryOn = False  # Para o Loop
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Retorna para o menu inicial

            else:
                ballB.collided = False

            ballB.set_velocity(2)


            if pygame.sprite.collide_rect(ballC, paddlePong):
                if not  ballC.collided:
                    effect = pygame.mixer.Sound('Sounds/damn.mp3')
                    effect.play()
                    lives -= 1

                    ballC.collided = True
                    if lives == 0:
                        # Efeito sonoro game over
                        effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                        effect.play()

                        # Chamando a função game over
                        selected_option = self.over(score)
                        if selected_option == 0:
                            carryOn = False  # Para o Loop
                            self.play_game()
                        elif selected_option == 1:
                            carryOn = False  # Para o Loop
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Retorna para o menu inicial

            else:

                ballC.collided = False

            ballC.set_velocity(2)


            if pygame.sprite.collide_rect(ballD, paddlePong):
                if not ballD.collided:
                    effect = pygame.mixer.Sound('Sounds/damn.mp3')
                    effect.play()
                    lives -= 1

                    ballD.collided = True
                    if lives == 0:
                        # Efeito sonoro game over
                        effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                        effect.play()

                        # Chamando a função game over
                        selected_option = self.over(score)
                        if selected_option == 0:
                            carryOn = False  # Para o Loop
                            self.play_game()
                        elif selected_option == 1:
                            carryOn = False  # Para o Loop
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Retorna para o menu inicial
            else:

                ballD.collided = False


            ballD.set_velocity(2)



            # Verifique se a bola está quicando em alguma das 4 paredes:
            # Verifique colisões com as paredes laterais
            if ball.rect.x >= 790 or ball.rect.x <= 0:
                ball.velocity[0] = -ball.velocity[0]
                ball.velocity[1] *= 0.9  # Diminua a velocidade vertical após colidir com a parede

            # Verifique colisão com a parede inferior
            if ball.rect.y > 590:
                ball.velocity[1] = -ball.velocity[1]
                ball.velocity[0] *= 0.9# Diminua a velocidade horizontal após colidir com a parede

                # Efeito sonoro ao errar jogada
                effect = pygame.mixer.Sound('Sounds/damn.mp3')
                effect.play()

                # tiramos uma vida quando a bola bate na borda inferior da tela. Se o número de vidas atingir zero, exibiremos uma mensagem “ Game Over ”..
                lives -= 1

                if lives == 0:
                    # Efeito sonoro game over
                    effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                    effect.play()

                    # Chamando a função game over
                    selected_option = self.over(score)
                    if selected_option == 0:
                        carryOn = False  # Para o Loop
                        self.play_game()
                    elif selected_option == 1:
                        carryOn = False  # Para o Loop
                        pygame.mixer.music.stop()  # musica da intro para
                        menu.run()  # Retorna para o menu inicial

            if ball.rect.y < 40:
                ball.velocity[1] = -ball.velocity[1]

            # Detectar colisões entre a bola e a raquete
            if pygame.sprite.collide_rect(ball, paddlePong):
                # Verifique se a bola está abaixo da barra e ajuste a posição se necessário
                if ball.rect.bottom > paddlePong.rect.top:
                    ball.rect.bottom = paddlePong.rect.top
                    ball.velocity[1] = -ball.velocity[1]  # Inverta a direção vertical apenas uma vez após a colisão
                else:
                    ball.bounce()  # Se estiver acima da barra, faça a bola quicar normalmente


                # Efeito sonoro ao tocar na raquete
                effect = pygame.mixer.Sound('Sounds/beep1.wav')
                effect.play()

                # Verifique se a bola está abaixo da barra e ajuste a posição se necessário
                if ball.rect.bottom > paddlePong.rect.top:
                    ball.rect.bottom = paddlePong.rect.top

            # detectamos se a bola bate em um tijolo. Nesse caso, removemos o tijolo ( usando o matar ( ) método ) e incremente a pontuação em um.
            # Verifique se a bola colide com algum dos tijolos
            brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)

            for brick in brick_collision_list:
                ball.bounce()

                # Efeito sonoro da bola ao bater no tijolo
                effect = pygame.mixer.Sound('Sounds/moeda.mp3')
                effect.play()

                score += 1
                if brick == BOSS_brick:
                    BOSS_brick_hits += 1
                    if brick == BOSS_brick and BOSS_brick_hits == 3:
                        brick.kill()
                # se não for o bloco vermelho, morre em um hit normalmente
                else:
                    brick.kill()

                if len(all_bricks) == 0 or (BOSS_brick in brick_collision_list and BOSS_brick_hits == 3):
                    # Exibir mensagem de nível concluído por 3 segundos
                    font = pygame.font.Font("fontes/ghosthey-Regular.ttf", 34)
                    text = font.render("LEVEL 1 COMPLETE", 1, WHITE)
                    screen.blit(text, (200, 300))
                    pygame.display.flip()

                    # Efeito sonoro ao bater no tijolo
                    effect = pygame.mixer.Sound('Sounds/win.mp3')
                    effect.play()
                    pygame.mixer.music.stop()  # musica da intro para

                    pygame.time.wait(3000)

                    self.play_game2(lives, score)

            # --- O código do desenho deve ir aqui
            # Plano de fundo da fase do jogo.
            screen.blit(background, (0, 0))
            pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

            # Exiba a pontuação e o número de vidas na parte superior da tela
            font = pygame.font.Font(None, 34)
            text = font.render("Score: " + str(score), 1, WHITE)
            screen.blit(text, (20, 10))
            text = font.render("Lives: " + str(lives), 1, WHITE)
            screen.blit(text, (650, 10))

            # Agora vamos desenhar todos os sprites de uma só vez. (Por enquanto só temos 2 sprites!)
            all_sprites_list.draw(screen)

            # --- Vá em frente e atualize a tela com o que desenhamos.
            pygame.display.flip()

            # --- Limite a 60 quadros por segundo
            clock.tick(60)

    def play_game2(self,lives,score):
        # Adicione aqui a lógica para iniciar o jogo principal
        # Definir algumas cores
        WHITE = (255, 255, 255)
        DARKBLUE = (36, 90, 190)
        LIGHTBLUE = (0, 176, 240)
        RED = (255, 0, 0)
        ORANGE = (255, 100, 0)
        YELLOW = (255, 255, 0)
        BOSS = (0, 0, 0)

        pygame.mixer.music.stop()  # musica da intro para
        pygame.mixer.music.load("Sounds/soundtracks/sound2.mpeg")
        pygame.mixer.music.play(-1)  # -1 significa reprodução em loop contínuo




        # O jogo será executado em sua própria janela, para a qual você pode decidir um título, uma largura e uma altura
        size = (800, 600)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Breakout Game")
        background = pygame.image.load("images/dee.jpg")

        # Esta será uma lista que conterá todos os sprites que pretendemos utilizar em nosso jogo.
        all_sprites_list = pygame.sprite.Group()

        # Crie a Barra
        paddlePong = Paddle(WHITE, 150, 25)
        paddlePong.rect.x = 350
        paddlePong.rect.y = 580

        # Crie o sprite da bola
        ball = Ball(WHITE, 10, 10, [7, 7])
        ball.rect.x = 395
        ball.rect.y = 295

        # Crie o sprite das bola/ataque
        ballB = BallB(WHITE, 10, 10, 8)
        ballB.rect.x = 400
        ballB.rect.y = 20
        ballB.image = pygame.image.load("bolas/darkball.png").convert_alpha()

        ballC = BallB(WHITE, 10, 10, 8)
        ballC.rect.x = 400
        ballC.rect.y = 20
        ballC.image = pygame.image.load("bolas/darkball.png").convert_alpha()

        ballD = BallB(WHITE, 10, 10, 8)
        ballD.rect.x = 400
        ballD.rect.y = 20
        ballD.image = pygame.image.load("bolas/darkball.png").convert_alpha()

        ballB_start_pos = (ballB.rect.x, ballB.rect.y)
        ballC_start_pos = (ballB.rect.x, ballB.rect.y)
        ballD_start_pos = (ballB.rect.x, ballB.rect.y)
        separation_distance = 5


        # criamos três linhas de tijolos e as adicionamos a um grupo chamado all_bricks.
        all_bricks = pygame.sprite.Group()

        for i in range(1):
            for i in range(1):
                BOSS_brick = Brick(BOSS, 80, 80, 0)  # bloco do boss
                BOSS_brick.rect.x = 350
                BOSS_brick.rect.y = 50
                BOSS_brick.image = pygame.image.load("images/Death.png").convert_alpha()
                all_sprites_list.add(BOSS_brick)
                all_bricks.add(BOSS_brick)
        for i in range(12):
            brick = Brick(ORANGE, 70, 60, 0)
            brick.rect.x = 20 + i * 60
            brick.rect.y = 150
            brick.image = pygame.image.load("images/Skel.png").convert_alpha()
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(12):
            brick = Brick(YELLOW, 70, 50, 0)
            brick.rect.x = 20 + i * 60
            brick.rect.y = 230
            brick.image = pygame.image.load("images/block/lapide.png").convert_alpha()
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        # Fim do codigo tijolos

        # Adicionando a Barra(paddle) e a bola(ball) à lista de sprites
        all_sprites_list.add(paddlePong)
        all_sprites_list.add(ball)

        all_sprites_list.add(ballB)
        all_sprites_list.add(ballC)
        all_sprites_list.add(ballD)

        # O loop continuará até que o usuário saia do jogo (por exemplo, clique no botão Fechar).
        carryOn = True

        # O relógio será usado para controlar a rapidez com que a tela é atualizada
        clock = pygame.time.Clock()

        # -------- Loop do programa principal -----------
        BOSS_brick_hits = 0  # numero inicial de vidas do bloco
        last_spawn_time = 0  # para pegar o tempo inicial para o lance do ataque
        while carryOn:

            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - last_spawn_time

            if elapsed_time >= 5000:
                all_sprites_list.add(ballB)
                all_sprites_list.add(ballC)
                all_sprites_list.add(ballD)
                ballB.rect.x = 400
                ballB.rect.y = 80
                ballC.rect.x = 400
                ballC.rect.y = 80
                ballD.rect.x = 400
                ballD.rect.y = 80
                last_spawn_time = current_time

            # --- Loop de evento principal
            for event in pygame.event.get():  # O usuário fez algo
                if event.type == pygame.QUIT:  # Se o usuário clicou em fechar
                    carryOn = False  # Sinalize que terminamos, então saímos deste loop
                    menu.run()  # Retorna ao menu principal
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        carryOn = False  # Termina o loop principal
                        menu.run()  # Retorna ao menu principal

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    selected_option = self.pause()
                    if selected_option == 0:
                        continue  # Continua o Jogo de onde Parou
                    elif selected_option == 1:
                        carryOn = False  # Para o Loop
                        menu.run()  # Retorna para o menu inicial

            # Movendo a Barra quando o uso usa as teclas de seta
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddlePong.moveLeft(10)
            if keys[pygame.K_RIGHT]:
                paddlePong.moveRight(10)

            # --- A lógica do jogo deve ir aqui
            ballB.rect.x, ballB.rect.y = ballB.rect.x - separation_distance, ballB.rect.y + separation_distance
            ballC.rect.x, ballC.rect.y = ballC.rect.x, ballC.rect.y + separation_distance
            ballD.rect.x, ballD.rect.y = ballD.rect.x + separation_distance, ballD.rect.y + separation_distance

            all_sprites_list.update()
            if pygame.sprite.collide_rect(ballB, paddlePong):
                if not ballB.collided:
                    effect = pygame.mixer.Sound('Sounds/damn.mp3')
                    effect.play()
                    lives -= 1
                    ballB.collided = True
                    if lives == 0:
                        # Efeito sonoro game over
                        effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                        effect.play()

                        # Chamando a função game over
                        selected_option = self.over(score)
                        if selected_option == 0:
                            carryOn = False  # Para o Loop
                            self.play_game()
                        elif selected_option == 1:
                            carryOn = False  # Para o Loop
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Retorna para o menu inicial

            else:
                ballB.collided = False

            ballB.set_velocity(2)

            if pygame.sprite.collide_rect(ballC, paddlePong):
                if not ballC.collided:
                    effect = pygame.mixer.Sound('Sounds/damn.mp3')
                    effect.play()
                    lives -= 1

                    ballC.collided = True
                    if lives == 0:
                        # Efeito sonoro game over
                        effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                        effect.play()

                        # Chamando a função game over
                        selected_option = self.over(score)
                        if selected_option == 0:
                            carryOn = False  # Para o Loop
                            self.play_game()
                        elif selected_option == 1:
                            carryOn = False  # Para o Loop
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Retorna para o menu inicial

            else:

                ballC.collided = False

            ballC.set_velocity(2)

            if pygame.sprite.collide_rect(ballD, paddlePong):
                if not ballD.collided:
                    effect = pygame.mixer.Sound('Sounds/damn.mp3')
                    effect.play()
                    lives -= 1

                    ballD.collided = True
                    if lives == 0:
                        # Efeito sonoro game over
                        effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                        effect.play()

                        # Chamando a função game over
                        selected_option = self.over(score)
                        if selected_option == 0:
                            carryOn = False  # Para o Loop
                            self.play_game()
                        elif selected_option == 1:
                            carryOn = False  # Para o Loop
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Retorna para o menu inicial
            else:

                ballD.collided = False

            ballD.set_velocity(2)

            # Verifique se a bola está quicando em alguma das 4 paredes:
            # Verifique colisões com as paredes laterais
            if ball.rect.x >= 790 or ball.rect.x <= 0:
                ball.velocity[0] = -ball.velocity[0]
                ball.velocity[1] *= 0.9  # Diminua a velocidade vertical após colidir com a parede

            # Verifique colisão com a parede inferior
            if ball.rect.y > 590:
                ball.velocity[1] = -ball.velocity[1]
                ball.velocity[0] *= 0.9  # Diminua a velocidade horizontal após colidir com a parede

                # Efeito sonoro ao errar jogada
                effect = pygame.mixer.Sound('Sounds/damn.mp3')
                effect.play()

                # tiramos uma vida quando a bola bate na borda inferior da tela. Se o número de vidas atingir zero, exibiremos uma mensagem “ Game Over ”..
                lives -= 1

                if lives == 0:
                    # Efeito sonoro game over
                    effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                    effect.play()

                    # Chamando a função game over
                    selected_option = self.over(score)
                    if selected_option == 0:
                        carryOn = False  # Para o Loop
                        self.play_game()
                    elif selected_option == 1:
                        carryOn = False  # Para o Loop
                        pygame.mixer.music.stop()  # musica da intro para
                        menu.run()  # Retorna para o menu inicial

            if ball.rect.y < 40:
                ball.velocity[1] = -ball.velocity[1]

            # Detectar colisões entre a bola e a raquete
            if pygame.sprite.collide_rect(ball, paddlePong):
                # Verifique se a bola está abaixo da barra e ajuste a posição se necessário
                if ball.rect.bottom > paddlePong.rect.top:
                    ball.rect.bottom = paddlePong.rect.top
                    ball.velocity[1] = -ball.velocity[1]  # Inverta a direção vertical apenas uma vez após a colisão
                else:
                    ball.bounce()  # Se estiver acima da barra, faça a bola quicar normalmente

                # Efeito sonoro ao tocar na raquete
                effect = pygame.mixer.Sound('Sounds/beep1.wav')
                effect.play()

                # Verifique se a bola está abaixo da barra e ajuste a posição se necessário
                if ball.rect.bottom > paddlePong.rect.top:
                    ball.rect.bottom = paddlePong.rect.top

            # detectamos se a bola bate em um tijolo. Nesse caso, removemos o tijolo ( usando o matar ( ) método ) e incremente a pontuação em um.
            # Verifique se a bola colide com algum dos tijolos
            brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)

            for brick in brick_collision_list:
                ball.bounce()

                # Efeito sonoro da bola ao bater no tijolo
                effect = pygame.mixer.Sound('Sounds/moeda.mp3')
                effect.play()

                score += 1
                if brick == BOSS_brick:
                    BOSS_brick_hits += 1
                    if brick == BOSS_brick and BOSS_brick_hits == 3:
                        brick.kill()
                # se não for o bloco vermelho, morre em um hit normalmente
                else:
                    brick.kill()

                if len(all_bricks) == 0 or (BOSS_brick in brick_collision_list and BOSS_brick_hits == 3):
                    # Exibir mensagem de nível concluído por 3 segundos
                    font = pygame.font.Font("fontes/ghosthey-Regular.ttf", 34)
                    text = font.render("LEVEL 2 COMPLETE", 1, WHITE)
                    screen.blit(text, (200, 300))
                    pygame.display.flip()

                    # Efeito sonoro ao bater no tijolo
                    effect = pygame.mixer.Sound('Sounds/win.mp3')
                    effect.play()
                    pygame.mixer.music.stop()  # musica da intro para

                    pygame.time.wait(3000)

                    self.play_game3(lives, score)

            # --- O código do desenho deve ir aqui
            # Plano de fundo da fase do jogo.
            screen.blit(background, (0, 0))
            pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

            # Exiba a pontuação e o número de vidas na parte superior da tela
            font = pygame.font.Font(None, 34)
            text = font.render("Score: " + str(score), 1, WHITE)
            screen.blit(text, (20, 10))
            text = font.render("Lives: " + str(lives), 1, WHITE)
            screen.blit(text, (650, 10))

            # Agora vamos desenhar todos os sprites de uma só vez. (Por enquanto só temos 2 sprites!)
            all_sprites_list.draw(screen)

            # --- Vá em frente e atualize a tela com o que desenhamos.
            pygame.display.flip()

            # --- Limite a 60 quadros por segundo
            clock.tick(60)

    def play_game3(self,lives,score):
        # Adicione aqui a lógica para iniciar o jogo principal
        # Definir algumas cores
        WHITE = (255, 255, 255)
        DARKBLUE = (36, 90, 190)
        LIGHTBLUE = (0, 176, 240)
        RED = (255, 0, 0)
        ORANGE = (255, 100, 0)
        YELLOW = (255, 255, 0)
        BOSS = (0, 0, 0)

        pygame.mixer.music.stop()  # musica da intro para
        pygame.mixer.music.load("Sounds/soundtracks/bossf.mpeg")
        pygame.mixer.music.play(-1)  # -1 significa reprodução em loop contínuo
        effect = pygame.mixer.Sound('Sounds/defeat-you.mp3')
        effect.play()



        # O jogo será executado em sua própria janela, para a qual você pode decidir um título, uma largura e uma altura
        size = (800, 600)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Breakout Game")
        background = pygame.image.load("images/final.jpg")

        # Esta será uma lista que conterá todos os sprites que pretendemos utilizar em nosso jogo.
        all_sprites_list = pygame.sprite.Group()

        # Crie a Barra
        paddlePong = Paddle(WHITE, 150, 25)
        paddlePong.rect.x = 350
        paddlePong.rect.y = 580

        # Crie o sprite da bola
        ball = Ball(WHITE, 10, 10, [7, 7])
        ball.rect.x = 395
        ball.rect.y = 295

        # Crie o sprite das bola/ataque
        ballB = BallB(WHITE, 10, 10, 8)
        ballB.rect.x = 400
        ballB.rect.y = 20
        ballB.image = pygame.image.load("bolas/fire.png").convert_alpha()

        ballC = BallB(WHITE, 10, 10, 8)
        ballC.rect.x = 400
        ballC.rect.y = 20
        ballC.image = pygame.image.load("bolas/fire.png").convert_alpha()

        ballD = BallB(WHITE, 10, 10, 8)
        ballD.rect.x = 400
        ballD.rect.y = 20
        ballD.image = pygame.image.load("bolas/fire.png").convert_alpha()

        ballB_start_pos = (ballB.rect.x, ballB.rect.y)
        ballC_start_pos = (ballB.rect.x, ballB.rect.y)
        ballD_start_pos = (ballB.rect.x, ballB.rect.y)
        separation_distance = 5
        # criamos três linhas de tijolos e as adicionamos a um grupo chamado all_bricks.

        # criamos três linhas de tijolos e as adicionamos a um grupo chamado all_bricks.
        all_bricks = pygame.sprite.Group()

        for i in range(1):
            for i in range(1):
                BOSS_brick = Brick(BOSS, 80, 80, 0)  # bloco do boss
                BOSS_brick.rect.x = 350
                BOSS_brick.rect.y = 50
                BOSS_brick.image = pygame.image.load("images/Dr.png").convert_alpha()
                all_sprites_list.add(BOSS_brick)
                all_bricks.add(BOSS_brick)
        for i in range(12):
            brick = Brick(ORANGE, 70, 60, 0)
            brick.rect.x = 20 + i * 60
            brick.rect.y = 150
            brick.image = pygame.image.load("images/mur.png").convert_alpha()
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(12):
            brick = Brick(YELLOW, 70, 50, 0)
            brick.rect.x = 20 + i * 60
            brick.rect.y = 230
            brick.image = pygame.image.load("images/murci.png").convert_alpha()
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        # Fim do codigo tijolos

        # Adicionando a Barra(paddle) e a bola(ball) à lista de sprites
        all_sprites_list.add(paddlePong)
        all_sprites_list.add(ball)

        all_sprites_list.add(ballB)
        all_sprites_list.add(ballC)
        all_sprites_list.add(ballD)

        # O loop continuará até que o usuário saia do jogo (por exemplo, clique no botão Fechar).
        carryOn = True

        # O relógio será usado para controlar a rapidez com que a tela é atualizada
        clock = pygame.time.Clock()

        # -------- Loop do programa principal -----------
        BOSS_brick_hits = 0  # numero inicial de vidas do bloco
        last_spawn_time = 0  # para pegar o tempo inicial para o lance do ataque
        while carryOn:

            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - last_spawn_time

            if elapsed_time >= 5000:
                all_sprites_list.add(ballB)
                all_sprites_list.add(ballC)
                all_sprites_list.add(ballD)
                ballB.rect.x = 400
                ballB.rect.y = 80
                ballC.rect.x = 400
                ballC.rect.y = 80
                ballD.rect.x = 400
                ballD.rect.y = 80
                last_spawn_time = current_time

            # --- Loop de evento principal
            for event in pygame.event.get():  # O usuário fez algo
                if event.type == pygame.QUIT:  # Se o usuário clicou em fechar
                    carryOn = False  # Sinalize que terminamos, então saímos deste loop
                    menu.run()  # Retorna ao menu principal
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        carryOn = False  # Termina o loop principal
                        menu.run()  # Retorna ao menu principal

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    selected_option = self.pause()
                    if selected_option == 0:
                        continue  # Continua o Jogo de onde Parou
                    elif selected_option == 1:
                        carryOn = False  # Para o Loop
                        menu.run()  # Retorna para o menu inicial

            # Movendo a Barra quando o uso usa as teclas de seta
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddlePong.moveLeft(10)
            if keys[pygame.K_RIGHT]:
                paddlePong.moveRight(10)

            # --- A lógica do jogo deve ir aqui
            ballB.rect.x, ballB.rect.y = ballB.rect.x - separation_distance, ballB.rect.y + separation_distance
            ballC.rect.x, ballC.rect.y = ballC.rect.x, ballC.rect.y + separation_distance
            ballD.rect.x, ballD.rect.y = ballD.rect.x + separation_distance, ballD.rect.y + separation_distance

            all_sprites_list.update()
            if pygame.sprite.collide_rect(ballB, paddlePong):
                if not ballB.collided:
                    effect = pygame.mixer.Sound('Sounds/damn.mp3')
                    effect.play()
                    lives -= 1
                    ballB.collided = True
                    if lives == 0:
                        # Efeito sonoro game over
                        effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                        effect.play()

                        # Chamando a função game over
                        selected_option = self.over(score)
                        if selected_option == 0:
                            carryOn = False  # Para o Loop
                            self.play_game()
                        elif selected_option == 1:
                            carryOn = False  # Para o Loop
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Retorna para o menu inicial

            else:
                ballB.collided = False

            ballB.set_velocity(2)

            if pygame.sprite.collide_rect(ballC, paddlePong):
                if not ballC.collided:
                    effect = pygame.mixer.Sound('Sounds/damn.mp3')
                    effect.play()
                    lives -= 1

                    ballC.collided = True
                    if lives == 0:
                        # Efeito sonoro game over
                        effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                        effect.play()

                        # Chamando a função game over
                        selected_option = self.over(score)
                        if selected_option == 0:
                            carryOn = False  # Para o Loop
                            self.play_game()
                        elif selected_option == 1:
                            carryOn = False  # Para o Loop
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Retorna para o menu inicial

            else:

                ballC.collided = False

            ballC.set_velocity(2)

            if pygame.sprite.collide_rect(ballD, paddlePong):
                if not ballD.collided:
                    effect = pygame.mixer.Sound('Sounds/damn.mp3')
                    effect.play()
                    lives -= 1

                    ballD.collided = True
                    if lives == 0:
                        # Efeito sonoro game over
                        effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                        effect.play()

                        # Chamando a função game over
                        selected_option = self.over(score)
                        if selected_option == 0:
                            carryOn = False  # Para o Loop
                            self.play_game()
                        elif selected_option == 1:
                            carryOn = False  # Para o Loop
                            pygame.mixer.music.stop()  # musica da intro para
                            menu.run()  # Retorna para o menu inicial
            else:

                ballD.collided = False

            ballD.set_velocity(2)

            # Verifique se a bola está quicando em alguma das 4 paredes:
            # Verifique colisões com as paredes laterais
            if ball.rect.x >= 790 or ball.rect.x <= 0:
                ball.velocity[0] = -ball.velocity[0]
                ball.velocity[1] *= 0.9  # Diminua a velocidade vertical após colidir com a parede

            # Verifique colisão com a parede inferior
            if ball.rect.y > 590:
                ball.velocity[1] = -ball.velocity[1]
                ball.velocity[0] *= 0.9  # Diminua a velocidade horizontal após colidir com a parede

                # Efeito sonoro ao errar jogada
                effect = pygame.mixer.Sound('Sounds/damn.mp3')
                effect.play()

                # tiramos uma vida quando a bola bate na borda inferior da tela. Se o número de vidas atingir zero, exibiremos uma mensagem “ Game Over ”..
                lives -= 1

                if lives == 0:
                    # Efeito sonoro game over
                    effect = pygame.mixer.Sound('Sounds/sorry.mp3')
                    effect.play()

                    # Chamando a função game over
                    selected_option = self.over(score)
                    if selected_option == 0:
                        carryOn = False  # Para o Loop
                        self.play_game()
                    elif selected_option == 1:
                        carryOn = False  # Para o Loop
                        menu.run()  # Retorna para o menu inicial

            if ball.rect.y < 40:
                ball.velocity[1] = -ball.velocity[1]

            # Detectar colisões entre a bola e a raquete
            if pygame.sprite.collide_rect(ball, paddlePong):
                # Verifique se a bola está abaixo da barra e ajuste a posição se necessário
                if ball.rect.bottom > paddlePong.rect.top:
                    ball.rect.bottom = paddlePong.rect.top
                    ball.velocity[1] = -ball.velocity[1]  # Inverta a direção vertical apenas uma vez após a colisão
                else:
                    ball.bounce()  # Se estiver acima da barra, faça a bola quicar normalmente

                # Efeito sonoro ao tocar na raquete
                effect = pygame.mixer.Sound('Sounds/beep1.wav')
                effect.play()

                # Verifique se a bola está abaixo da barra e ajuste a posição se necessário
                if ball.rect.bottom > paddlePong.rect.top:
                    ball.rect.bottom = paddlePong.rect.top

            # detectamos se a bola bate em um tijolo. Nesse caso, removemos o tijolo ( usando o matar ( ) método ) e incremente a pontuação em um.
            # Verifique se a bola colide com algum dos tijolos
            brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)

            for brick in brick_collision_list:
                ball.bounce()

                # Efeito sonoro da bola ao bater no tijolo
                effect = pygame.mixer.Sound('Sounds/moeda.mp3')
                effect.play()

                score += 1
                if brick == BOSS_brick:
                    BOSS_brick_hits += 1
                    if brick == BOSS_brick and BOSS_brick_hits == 3:
                        brick.kill()
                # se não for o bloco vermelho, morre em um hit normalmente
                else:
                    brick.kill()

                if len(all_bricks) == 0 or (BOSS_brick in brick_collision_list and BOSS_brick_hits == 3):
                    # Exibir mensagem de nível concluído por 3 segundos
                    font = pygame.font.Font("fontes/ghosthey-Regular.ttf", 34)
                    text = font.render("LEVEL 3 COMPLETE", 1, WHITE)
                    screen.blit(text, (200, 300))
                    pygame.display.flip()

                    # Efeito sonoro ao bater no tijolo
                    effect = pygame.mixer.Sound('Sounds/win.mp3')
                    effect.play()

                    pygame.time.wait(3000)
                    menu.run()

            # --- O código do desenho deve ir aqui
            # Plano de fundo da fase do jogo.
            screen.blit(background, (0, 0))
            pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

            # Exiba a pontuação e o número de vidas na parte superior da tela
            font = pygame.font.Font(None, 34)
            text = font.render("Score: " + str(score), 1, WHITE)
            screen.blit(text, (20, 10))
            text = font.render("Lives: " + str(lives), 1, WHITE)
            screen.blit(text, (650, 10))

            # Agora vamos desenhar todos os sprites de uma só vez. (Por enquanto só temos 2 sprites!)
            all_sprites_list.draw(screen)

            # --- Vá em frente e atualize a tela com o que desenhamos.
            pygame.display.flip()

            # --- Limite a 60 quadros por segundo
            clock.tick(60)

    def play_versus_mode(self):
        # Adicione aqui a lógica para iniciar o modo versus
        # Definir algumas cores
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        # Abre uma nova janela
        size = (800, 600)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Pong")

        pygame.mixer.music.stop()  # musica da intro para
        pygame.mixer.music.load("Sounds/The Festival of Servants.mp3")
        pygame.mixer.music.play(-1)  # -1 significa reprodução em loop contínuo

        background = pygame.image.load("images/versus/versu.jpg")

        # Crie a Barra JOGADOR-1
        paddleA = Paddle(WHITE, 10, 100)
        paddleA.rect.x = 10
        paddleA.rect.y = 100
        paddleA.image = pygame.image.load("images/versus/ossoa.png").convert_alpha()

        # Crie a Barra JOGADOR-2
        paddleB = Paddle(WHITE, 10, 100)
        paddleB.rect.x = 780
        paddleB.rect.y = 100
        paddleB.image = pygame.image.load("images/versus/ossob.png").convert_alpha()

        # Crie o sprite da bola
        ball = BallVersus(10, 10, [5, 5])
        ball.rect.x = 345
        ball.rect.y = 195
        ball.image = pygame.image.load("images/versus/caveira.png").convert_alpha()

        # Crie o obstáculo
        obstacle = Obstacle(WHITE, 10, 100, 394, 280)
        obstacle.image = pygame.image.load("images/versus/tijolo.png").convert_alpha()

        # Esta será uma lista que conterá todos os sprites que pretendemos utilizar em nosso jogo.
        all_sprites_list = pygame.sprite.Group()

        # Adicione as 2 BARRAS, a BOLA e o OBSTÁCULO à lista de objetos
        all_sprites_list.add(paddleA)
        all_sprites_list.add(paddleB)
        all_sprites_list.add(ball)
        all_sprites_list.add(obstacle)

        # O loop continuará até que o usuário saia do jogo (por exemplo, clique no botão Fechar).
        carryOn = True

        # O relógio será usado para controlar a rapidez com que a tela é atualizada
        clock = pygame.time.Clock()

        # Inicializar as pontuações dos jogadores
        scoreA = 0
        scoreB = 0

        # -------- Loop do programa principal -----------
        while carryOn:
            # --- Loop de evento principal ---
            for event in pygame.event.get():  # O usuário fez algo
                if event.type == pygame.QUIT:  # Se o usuário clicou em fechar
                    carryOn = False  # Sinalize que terminamos, então saímos deste loop
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:  # Pressionar a tecla x encerrará o jogo
                        carryOn = False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    selected_option = self.pause()
                    if selected_option == 0:
                        continue  # Continua o Jogo de onde Parou
                    elif selected_option == 1:
                        carryOn = False  # Para o Loop
                        pygame.mixer.music.stop()  # musica da intro para
                        menu.run()  # Retorna para o menu inicial

            # Mover as BARRAS quando usa as teclas de seta (jogador A) ou as teclas "W/S" (jogador B)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddleA.moveUp(5)
            if keys[pygame.K_s]:
                paddleA.moveDown(5)
            if keys[pygame.K_UP]:
                paddleB.moveUp(5)
            if keys[pygame.K_DOWN]:
                paddleB.moveDown(5)

            # --- A lógica do jogo deve ir aqui ---
            all_sprites_list.update()

            # Verifique se a bola ultrapassou a barra do jogador A
            if ball.rect.x >= 790:
                # Efeito sonoro da bola ao bater no tijolo
                effect = pygame.mixer.Sound('Sounds/moeda.mp3')
                effect.play()

                scoreA += 1
                ball.velocity[0] = -ball.velocity[0]

                if scoreA == 10:
                    font = pygame.font.Font("fontes/ghosthey-Regular.ttf", 74)
                    text = font.render("Jogador 1 Venceu", 1, WHITE)
                    screen.blit(text, (200, 300))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    carryOn = False  # Termina o loop principal
                    pygame.mixer.music.stop()  # musica da intro para
                    menu.run()  # Retorna ao menu principal

            # Verifique se a bola ultrapassou a barra do jogador B
            if ball.rect.x <= 0:
                # Efeito sonoro da bola ao bater no tijolo
                effect = pygame.mixer.Sound('Sounds/moeda.mp3')
                effect.play()

                scoreB += 1
                ball.velocity[0] = -ball.velocity[0]

                if scoreB == 10:
                    font = pygame.font.Font("fontes/ghosthey-Regular.ttf", 74)
                    text = font.render("Jogador 2 Venceu", 1, WHITE)
                    screen.blit(text, (200, 300))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    carryOn = False  # Termina o loop principal
                    pygame.mixer.music.stop()  # musica da intro para
                    menu.run()  # Retorna ao menu principal

            if ball.rect.y > 590 or ball.rect.y < 0:
                # Inverta a direção vertical da bola
                ball.velocity[1] = -ball.velocity[1]

            # Detectar colisões entre a bola e as barras
            if pygame.sprite.collide_rect(ball, paddleA) or pygame.sprite.collide_rect(ball, paddleB):
                # Inverta a direção horizontal da bola
                ball.velocity[0] = -ball.velocity[0]

                # Efeito sonoro ao tocar na raquete
                effect = pygame.mixer.Sound('Sounds/versus/versu.mp3')
                effect.play()

                # Adicione um pequeno deslocamento vertical à bola para evitar que ela fique presa na barra
                ball.rect.y += ball.velocity[1]

            # Detectar colisão entre a bola e o obstáculo
            if pygame.sprite.collide_rect(ball, obstacle):
                # Inverter a direção horizontal da bola
                ball.velocity[0] = -ball.velocity[0]
                ball.velocity[1] = -ball.velocity[1]

                # Efeito sonoro ao colidir com o obstáculo
                effect = pygame.mixer.Sound('Sounds/beep2.wav')
                effect.play()

            # --- O código do desenho deve ir aqui ---
            # Primeiro, limpe a tela para preto.
            screen.blit(background, (0, 0))
            # Desenhe a rede
            pygame.draw.line(screen, WHITE, [400, 0], [400, 600], 5)





            # Desenhe as barras e o obstáculo
            screen.blit(paddleA.image, paddleA.rect)
            screen.blit(paddleB.image, paddleB.rect)
            screen.blit(obstacle.image, obstacle.rect)
            screen.blit(ball.image, ball.rect)

            # Exibir pontuações:
            font = pygame.font.Font("fontes/ghosthey-Regular.ttf", 74)
            text = font.render(str(scoreA), 1, WHITE)
            screen.blit(text, (250, 10))
            text = font.render(str(scoreB), 1, WHITE)
            screen.blit(text, (550, 10))

            # --- Vá em frente e atualize a tela com o que desenhamos.
            pygame.display.flip()

            # --- Limite a 60 quadros por segundo
            clock.tick(60)


    def play_didact_mode(self):
        # Adicione aqui a lógica para iniciar o jogo principal
        # Definir algumas cores
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        PINK = (255, 105, 180)
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        ORANGE = (255, 100, 0)
        PURPLE = (128, 0, 128)

        pygame.mixer.music.stop()

        letter_data = {
            'A': {
                'image': pygame.image.load('images/letras/A.png'),
                'sound': pygame.mixer.Sound('sounds/LetraseCores/A.mp3')
            },
            'B': {
                'image': pygame.image.load('images/letras/B.png'),
                'sound': pygame.mixer.Sound('sounds/LetraseCores/B.mp3')
            },
            'C': {
                'image': pygame.image.load('images/letras/C.png'),
                'sound': pygame.mixer.Sound('sounds/LetraseCores/C.mp3')
            },
            'D': {
                'image': pygame.image.load('images/letras/D.png'),
                'sound': pygame.mixer.Sound('sounds/LetraseCores/D.mp3')
            },
            'E': {
                'image': pygame.image.load('images/letras/E.png'),
                'sound': pygame.mixer.Sound('sounds/LetraseCores/E.mp3')
            },
            'F': {
                'image': pygame.image.load('images/letras/F.png'),
                'sound': pygame.mixer.Sound('sounds/LetraseCores/F.mp3')
            },
            'G': {
                'image': pygame.image.load('images/letras/G.png'),
                'sound': pygame.mixer.Sound('sounds/LetraseCores/G.mp3')
            },
            'H': {
                'image': pygame.image.load('images/letras/H.png'),
                'sound': pygame.mixer.Sound('sounds/LetraseCores/H.mp3')
            }

        }

        # Pontuação
        score = 0

        lives = 10

        # O jogo será executado em sua própria janela, para a qual você pode decidir um título, uma largura e uma altura
        size = (800, 600)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Breakout Game")
        background = pygame.image.load("images/fundoinfantil.jpg")

        # Esta será uma lista que conterá todos os sprites que pretendemos utilizar em nosso jogo.
        all_sprites_list = pygame.sprite.Group()

        # Crie a Barra
        paddlePong = Paddle(WHITE, 150, 25)
        paddlePong.rect.x = 350
        paddlePong.rect.y = 580
        paddlePong.image = pygame.image.load("images/barra/bar.png")


        # Crie o sprite da bola
        ball = Ball(WHITE, 10, 10, [7, 7])
        ball.rect.x = 345
        ball.rect.y = 195


        # criamos três linhas de tijolos e as adicionamos a um grupo chamado all_bricks.
        all_bricks = pygame.sprite.Group()

        # 4 fileira com 8 tijolos
        for i in range(1):
            brick = Brick(BLUE, 70, 30, 'A')
            brick.rect.x = 50 + i * 100
            brick.rect.y = 60
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(1):
            brick = Brick(GREEN, 70, 30, 'B')
            brick.rect.x = 140 + i * 100
            brick.rect.y = 60
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(1):
            brick = Brick(ORANGE, 70, 30, 'C')
            brick.rect.x = 230 + i * 100
            brick.rect.y = 60
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(1):
            brick = Brick(RED, 70, 30, 'D')
            brick.rect.x = 320 + i * 100
            brick.rect.y = 60
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(1):
            brick = Brick(PINK, 70, 30, 'E')
            brick.rect.x = 410 + i * 100
            brick.rect.y = 60
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(1):
            brick = Brick(BLUE, 70, 30, 'F')
            brick.rect.x = 500 + i * 100
            brick.rect.y = 60
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(1):
            brick = Brick(ORANGE, 70, 30, 'G')
            brick.rect.x = 590 + i * 100
            brick.rect.y = 60
            all_sprites_list.add(brick)
            all_bricks.add(brick)
        for i in range(1):
            brick = Brick(GREEN, 70, 30, 'H')
            brick.rect.x = 680 + i * 100
            brick.rect.y = 60
            all_sprites_list.add(brick)
            all_bricks.add(brick)

        # Fim do codigo tijolos
        # Adicionando a Barra(paddle) e a bola(ball) à lista de sprites
        all_sprites_list.add(ball)
        all_sprites_list.add(paddlePong)

        # O loop continuará até que o usuário saia do jogo (por exemplo, clique no botão Fechar).
        carryOn = True

        # O relógio será usado para controlar a rapidez com que a tela é atualizada
        clock = pygame.time.Clock()

        # -------- Loop do programa principal -----------

        while carryOn:
            # --- Loop de evento principal
            for event in pygame.event.get():  # O usuário fez algo
                if event.type == pygame.QUIT:  # Se o usuário clicou em fechar
                    carryOn = False  # Sinalize que terminamos, então saímos deste loop
                    menu.run()  # Retorna ao menu principal
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        carryOn = False  # Termina o loop principal
                        menu.run()  # Retorna ao menu principal

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    selected_option = self.pause()
                    if selected_option == 0:
                        continue  # Continua o Jogo de onde Parou
                    elif selected_option == 1:
                        carryOn = False  # Para o Loop
                        menu.run()  # Retorna para o menu inicial

            # Movendo a Barra quando o uso usa as teclas de seta
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddlePong.moveLeft(10)
            if keys[pygame.K_RIGHT]:
                paddlePong.moveRight(10)

            # --- A lógica do jogo deve ir aqui
            all_sprites_list.update()

            # Verifique se a bola está quicando em alguma das 4 paredes:
            if ball.rect.x >= 790:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x <= 0:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y > 590:
                ball.velocity[1] = -ball.velocity[1]

                # Efeito sonoro ao errar jogada
                effect = pygame.mixer.Sound('Sounds/beep2.wav')
                effect.play()

                # tiramos uma vida quando a bola bate na borda inferior da tela. Se o número de vidas atingir zero, exibiremos uma mensagem “ Game Over ”..
                lives -= 1

                if lives == 0:
                    # Efeito sonoro game over
                    effect = pygame.mixer.Sound('Sounds/gameOver.mp3')
                    effect.play()

                    # Exibir mensagem de fim de jogo por 3 segundos
                    font = pygame.font.Font(None, 74)
                    text = font.render("GAME OVER", 1, WHITE)
                    screen.blit(text, (250, 300))
                    pygame.display.flip()
                    pygame.time.wait(3000)

                    carryOn = False  # Termina o loop principal
                    menu.run()  # Retorna ao menu principal

            if ball.rect.y < 40:
                ball.velocity[1] = -ball.velocity[1]

            # Detectar colisões entre a bola e a raquete
            if pygame.sprite.collide_rect(ball, paddlePong):
                ball.bounce()

                # Efeito sonoro ao tocar na raquete
                effect = pygame.mixer.Sound('Sounds/beep1.wav')
                effect.play()

                # Verifique se a bola está abaixo da barra e ajuste a posição se necessário
                if ball.rect.bottom > paddlePong.rect.top:
                    ball.rect.bottom = paddlePong.rect.top

            # detectamos se a bola bate em um tijolo. Nesse caso, removemos o tijolo ( usando o matar ( ) método ) e incremente a pontuação em um.
            # Verifique se a bola colide com algum dos tijolos
            brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)

            for brick in brick_collision_list:
                ball.bounce()

                score += 1
                brick.kill()

                # Obtenha a letra associada ao tijolo
                letter = brick.letter

                # Verifique se a letra está presente no dicionário letter_data
                if letter in letter_data:
                    # Obtenha os dados da letra do dicionário
                    letter_info = letter_data[letter]

                    # Tamanho da tela do jogo
                    telaLargura = 800
                    telaAltura = 600

                    # Calcula as coordenadas para centralizar a imagem
                    x = (telaLargura - letter_info['image'].get_width()) // 2
                    y = (telaAltura - letter_info['image'].get_height()) // 2

                    # Exiba a imagem da letra na tela centralizada
                    screen.blit(letter_info['image'], (x, y))

                    # Reproduza o som da letra
                    letter_info['sound'].play()

                    # Atualize a tela
                    pygame.display.flip()

                    # Pausa o jogo por 3 segundos
                    pygame.time.delay(3000)

                # Limpe a tela
                screen.fill((0, 0, 0))

                # Desenhe novamente os sprites e atualize a tela
                all_sprites_list.draw(screen)
                pygame.display.flip()

                if len(all_bricks) == 0:
                    # Exibir mensagem de nível concluído por 3 segundos
                    font = pygame.font.Font(None, 74)
                    text = font.render("COMPLETE", 1, WHITE)
                    screen.blit(text, (200, 300))
                    pygame.display.flip()

                    pygame.time.wait(3000)

                    carryOn = False  # Termina o loop principal
                    menu.run()  # Retorna ao menu principal

            # --- O código do desenho deve ir aqui
            # Plano de fundo da fase do jogo.
            screen.blit(background, (0, 0))
            pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

            # Exiba a pontuação e o número de vidas na parte superior da tela
            font = pygame.font.Font(None, 34)
            text = font.render("Score: " + str(score), 1, WHITE)
            screen.blit(text, (20, 10))
            text = font.render("Lives: " + str(lives), 1, WHITE)
            screen.blit(text, (650, 10))

            # Agora vamos desenhar todos os sprites de uma só vez. (Por enquanto só temos 2 sprites!)
            all_sprites_list.draw(screen)

            # --- Vá em frente e atualize a tela com o que desenhamos.
            pygame.display.flip()

            # --- Limite a 60 quadros por segundo
            clock.tick(60)

    def quit(self):
        pygame.quit()

menu = Menu()
menu.run()
