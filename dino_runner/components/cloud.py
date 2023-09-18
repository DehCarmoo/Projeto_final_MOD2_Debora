import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD, DEFAULT_TYPE

CLOUD_IMG = {DEFAULT_TYPE: CLOUD}

class cloud(pygame.sprite.Sprite):
    def __init__(self):
        
   