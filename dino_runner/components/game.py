import pygame 
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE  #dino_runner é o nome da pasta principal.
from dino_runner.components.dinosaur import Dinosaur # vamos contruir esse arquivo 
from dino_runner.components.obstacle_manager import Obstacle_Manager #Importanto obstáculos 
from dino_runner.components.powerups.power_up_manage import PowerUpManager #Importanto o super poder

class game: #base do jogo
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.plaiyng = False
        self.running = False
        self.score = 0
        self.death_count = 0 #contagem de vida
        self.game_Speed = 20
        self.x_pos_bg = 0  # posição do objeto
        self.y_pos_bg = 0 
        self.player = Dinosaur()
        self.obstacle_manager = Obstacle_Manager()
        self.power_up_manager = PowerUpManager
        
    def execute (self): #Enquanto meu dinoussauro estiver correndo, esta vivo, se não, aparece a tela o restart
        self.running = True
        while self.running:
            if not self.playing:
                self.show.menu()
                
            pygame.sisplay.quit()
            pygame.quit()
    
    def run(self):
        self.plaiyng = True
        self.obstacle_manager.reset_obstacle() #vai resetar quando perder 
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        
        #aqui é a base do jogo
        while self.plaiyng:
            self.events()
            self.update()
            self.draw()
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.plaiyng = False
                self.running = False
    
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)
            

    def update_score(self): # a cada 100 pontos a velocidade vai aumentando 
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5
    
    def draw(self): #desenhando a tela do meu jogo
        self.clock.tick(FPS)
        self.screen.fill(255, 255, 255)
        self.draw_background(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self): #bg é background 
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x.pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        
        if self.x_pos_bg <= - image_width: 
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
            self.x_pos_bg -= self.game_Speed
            
    def draw_score(self): #Estamos desnehando a pontuação
        draw_message_component(
            f"Score: {self.score}", #Aqui irá receber a pontuação 
            self.screen,
            pos_x_center = 1000, #Poisção que irá apareecr a pontuação
            pos_y_center = 50
        )
                    
        
    def draw_power_up_time(self): #tempo para mostrar
        if self.player.has_power_up:
            time_to_Show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2) # mostra a contagem 
            if time_to_Show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} disponível por  {time_to_Show} segundos",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
        else:
            self.player.has_power.up = False
            self.player.type = DEFAULT_TYPE
            
    def handle_events_on_menu(self):
        for event in pygame.evente.get():
         if event.type == pygame.QUIT:
             self.plaiyng = False
             self.running = False
             
         elif event.type == pygame.KEYDOWN: #interações do teclado, se apertar qualkquer tecla, acontece o restart
             self.run
             
    def show_menu(self): #Desenvolvendo todos os menus
        self.screen.fill((255, 255, 255)) #O menu estará branco
        half_Screen_height = SCREEN_HEIGHT // 2
        half_Screen_width = SCREEN_WIDTH // 2
        
        if self.death_count == 0: #se a contagem de morte for igual a zero
            draw_message_component("Pressione qualquer tecla para iniciar.", self.screen)
        
        else:
         draw_message_component("Pressione qualquer tecla para reiniciar", self.screen, pos_y_center = half_Screen_height + 140)
         draw_message_component(
            f"Sua posição: {self.score}",
            self.screen,
            pos_y_cemter = half_Screen_height - 50
        )
        
         draw_message_component(
             f"contagem de vidas: {self.death_count} ",
             self.screen,
             pos_y_center = half_Screen_height - 100
         )
         
         self.screen.blit(ICON, (half_Screen_width - 40, half_Screen_height - 30))
    
pygame.display.flip()
self.handle_events_on_menu()                         