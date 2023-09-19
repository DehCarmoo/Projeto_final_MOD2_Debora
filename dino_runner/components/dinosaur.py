import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import (RUNNING,JUMPING,DUCKING,DEFAULT_TYPE,SHIELD_TYPE,DUCKING_SHIELD,JUMPING_SHIELD,RUNNING_SHIELD,)


pygame.init()
jump = pygame.mixer.Sound("dino_runner/components/som_jogo/sons_jump_sound.wav")

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}


X_POS = 70 
Y_POS = 345 #posição do chão
Y_POS_DUCK = 350 #posição dele quando abaixar0
JUMP_VEL = 7 #velocidade do pulo 


class Dinosaur(Sprite): #características do personagem do jogo
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True # está true porque ele começa o jog ocorrendo 
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = JUMP_VEL
        self.setup_state()

    def setup_state(self): #Quando tiver o poder, vai aparecer o shil, o tempo e tudo mais
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0  

    def update(self, user_input): #Aqui estou chamando o update do user input, aqui é o inicio da configuração das teclas
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump: #quando apertar a setinha pra cima, o personagem irá pular
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
            if self.dino_jump == True:  # Se o personagem pular, então dê player ao som
                jump.play() #Adicionei
        elif user_input[pygame.K_DOWN] and not self.dino_jump: #significa abaixar, a setinha de baixo
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck: #o run não aperta nenhum teclado para o personagem correr 
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
            
        if self.step_index >= 9: #Aqui significa que os passos estão sendo contados, o step index significa passos 
            self.step_index = 0

    def run(self): #Aqui é a condiguração do meu personagem correndo 
        self.image = RUN_IMG[self.type][self.step_index // 5] #aqui vai fazendo a troca de imagem para dar a sensação de que está andando
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1 #a cada += 1 passo vai dar a sensação de que a image está sendo trocada

    def jump(self): #Quando o personagem pula, ele dá uma diminuida na velocidade 
        self.image = JUMP_IMG[self.type] #chamou a imagem dele pulando 
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 #posição vertical 
            self.jump_vel -= 0.5  # mudei
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5] #mudando a imagem 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen): #Ele dá continuidado no jogo
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
