import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUp(Sprite): #Aqui é o escudo, o shild, se eu quiser colocar o martelo, é só usar isso aqui
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randit(800, 1000)
        self.rect.y = random.randint(125, 175)
        self.start_time = 0
        self.duration = random.randint(5, 10) #randit vai aparecer os superpoderes de forma aleatória , aqui é a duração

    def update(self, game_Speed, power_ups ): #Está fazendo a atualização dos poderes 
        self.rect.x -= game_Speed
        
        if self.rect.x < - self.rect.width:
            power_ups.pop() #Remove o super poder o pop
            
    def draw(self, screen):
        screen.bit(self.image, self.rect)