import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


pygame.init()
dead = pygame.mixer.Sound("dino_runner/components/som_jogo/sons_death_sound.wav")

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game): #O que eu quero que atualize no jogo
        obstacle_type = [
            Cactus(),
            Bird(),
            
        ]
        
        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)]) #A cada 0 e 1 ponto, meu cacto vai aparece
        for obstacle in self.obstacles: #para os obstaculos dentro da lista 
            obstacle.update(game.game_speed, self.obstacles) #game_speed é a velocidade, aqui estou atualizando a velocidade e os meus obstáculos 
            if game.player.dino_rect.colliderect(obstacle.rect): #se meu jogador colidi com os obstaculos
                if not game.player.has_power_up: #se o jogador não estiver com  super poder ao coligir 
                    pygame.time.delay(500) #quando ele morre demora pra aoarecer atela do menu
                    dead.play()# adicionei 
                    game.playing = False
                    game.death_count += 1
                    break #break pra findar o bloco
                else:
                    self.obstacles.remove(obstacle)
                    
    def reset_obstacles(self): #Quandos os obstáculos são remvidos o jogo vai reiniciar
        self.obstacles = []
        
    def draw(self,screen): #Vai continuar desenhando os obstáculos 
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        