import pygame 

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, GAME_OVER, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager #Importando os obstáculos 
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manage import PowerUpManager #Importando o super poder




pygame.init() #adicionei para ter acesso a sons no jogo
pygame.mixer.music.load("dino_runner/components/som_jogo/musica_jogo.wav") # musica do jogo
score = pygame.mixer.Sound("dino_runner/components/som_jogo/sons_score_sound.wav") #som do score
pygame.mixer_music.play(-1) #coloquei -1 para que a musica rodasse sem parar


class Game: #base do jogo
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.recorde = 0 #Adicionado
        self.death_count = 0 #cotagem de vidas 
        self.game_speed = 20
        self.x_pos_bg = 0 #posição do objeto
        self.y_pos_bg = 340
        self.x_pos_cloud = 0 #adicionado
        self.y_pos_cloud = 40
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
       
    
    
    def execute(self): #Enquanto meu personagem estive correndo, o jgo continua rodando, se não, vai para a tela do restart
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
       
        pygame.display.quit()
        pygame.quit()
    
    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles() #Aqui irá resetar os obstaculos
        self.power_up_manager.reset_power_up()
        self.game_speed = 10
        self.score = 0
         #base do jogo
        while self.playing:
            self.events()
            self.update()
            self.draw ()
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.ruinning = False
                    
            
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):  #A cada 100 pontos a velocidade vai aumentando 
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed +=  5
            score.play() # som do score, foi adicionado 
        if self.score >= self.recorde: #adicionando recorde 
            self.recorde = self.score  
             
        
    def draw(self): # Desenhando a tela do jogo
        self.clock.tick(FPS)  
        self.screen.fill((246, 102, 19))
        self.draw_blackground()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_cloud() #adicionado
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
      
        
    def draw_blackground(self): #Background do jogo
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
       
        if self.x_pos_bg <= - image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self): #Desenhando a pontuação do jogo
        draw_message_component(
            f"score:{self.score}", #recebe a pontuação do jogo
            self.screen,
            pos_x_center = 1000, #Posição que irá aparecer a pontuação do jogo
            pos_y_center = 50
        )
        draw_message_component(
            f"recorde:{self.recorde}", #recebeo record do jogo
            self.screen,
            pos_x_center = 1000, #Posição que irá aparecero record do jogo
            pos_y_center = 75
        )
        
        

    def draw_power_up_time(self): #tempo para mostrar
        if self.player.has_power_up:
            time_to_Show = round((self.player.power_up_timing - pygame.time.get_ticks()) / 1000, 5) # mostra a contagem 
            if time_to_Show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} disponível por  {time_to_Show} segundos",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            else:
                    self.player.has_power_up = False
                    self.player.type = DEFAULT_TYPE
                    
    def draw_cloud(self):
        image_width = CLOUD.get_width() #atribuindo a largura na imagem da nuvem 
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud)) #aqui a imagem está sendo desenhada  e está sendo atribuida a posição da nuvem
        if self.x_pos_cloud <= - image_width: #essa condicional irá verificar a posição da nuvem e vai verificar se ela saiu completamente da tela
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud)) #desenha outra nuvem caso a nuvem anterior tenha saido da tela, dando a impressão que a nuve mestá se movimentando
            self.x_pos_cloud = 1000 #posição da nuvem 
          

        self.x_pos_cloud -= self.game_speed #controla a velocidade do movimento da nuvem 
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            
            elif event.type == pygame.KEYDOWN: #interação do teclado, se apertar qualquer tecla o restart acontece 
                self.run()

    def show_menu(self): #desenvolvendo todos os menus 
        self.screen.fill((246, 102, 19)) #modifiquei a cor
        half_screen_height = SCREEN_HEIGHT // 2
        hals_screen_width = SCREEN_WIDTH // 2 
        
        if self.death_count == 0: # se a contagem da morte for igual a zero
            
            draw_message_component("Pressione qualquer tecla para iniciar", self.screen)
        
        else:
            draw_message_component("Pressione qualquer tecla para reiniciar", self.screen, pos_y_center = half_screen_height + 170)
            draw_message_component(
                f"Sua pontuaçao: {self.score}",
                self.screen,
                pos_y_center = half_screen_height - 10
            )


            draw_message_component(
                f"Contagem de vidas: {self.death_count} ",
                self.screen,
                pos_y_center = half_screen_height - 100
            )
            draw_message_component(
                f"Maior pontuação: {self.recorde}",
                self.screen,
                pos_y_center = half_screen_height + 100
            )#adicionei


            self.screen.blit(ICON, (hals_screen_width - 20, half_screen_height - 60))#modifiquei o icone e ajustei a posição
            self.screen.blit(GAME_OVER, (hals_screen_width - 200, half_screen_height - 190))#Adicionei o gamer over no final 
            
        pygame.display.flip()
        self.handle_events_on_menu()