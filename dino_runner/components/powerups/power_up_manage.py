import random
import pygame
from dino_runner.components.powerups.shield import Shield

class PowerUpManager: #Estamos criando o power up
    def __init__(self) :
        self.power_ups = []
        self.when_appars = 0
        
    def generate_power_up(self, score): 
        if len(self.power_ups) == 0 and self.when_appars == score:
            self.when_appars += random.randit(200, 300)  #A cada 200 ou 300 pontos que o meu jogo fizer, o superpoder irá aparece
            self.power_ups.append(Shield())
            
    def update (self, score, game_speed, player): #Estamos colocando as coisas que eu quero que atualize em meu jogo
        self.generate_power_up(score)
        
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            
        if player.dino_rect.colliderect(power_up.rect): #Ele vai colidir com algum objeto, se o power up estiver ativo, ele não morre
            power_up.start_time = pygame.time.get_ticks()
            player.shield = True
            player.has_power_up = True
            player.type = power_up.type
            player.power_up_timing = power_up.start_time + (power_up.duration * 1000) #duração do poder, irá durar por 10 segundos 
            self.power_ups.remove(power_up)
    
    def draw(self, screen): #estou redesenhando a tela para dar continuidade ao meu jogo
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset_power_ups(self): #Quando o meu jogo irá trazer os superpoderes novamente 
        self.power_ups = []
        self.when_appars = random.randint(200, 300)