import random
import pygame
from dino_runner.components.powerups.shield import Shield

class PowerUpManager(): #criando power up
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appers == score:
            self.when_appers += random.randint(300, 500) #A cada 300 ou 500 pontos que o jogador fizer, o shield irá aparecer 
            self.power_ups.append(Shield())

    def update(self, score, game_speed, player): #Estamos colocando as coisas que eu qeuro atualizar em meu jogo
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect): #O personagem irá colidir com algum objeto, se o powupr estiver ativo, ele não morre, se não, ele morre.
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_timing = power_up.start_time + (power_up.duration * 1000) #duração do superpoder 
                self.power_ups.remove(power_up)

    def draw(self, screen): #Aqui a tela está sendo redesenhada para dar continuidade ao meu jogo
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_up(self):
        self.power_ups = []
        self.when_appers = random.randint(150, 300) #Quando meu jogo irá mostras superpoderes novamente, modifiquei