import pygame

class Soundmanager:
    def __init__(self):
        self.sounds = {
            'click' : pygame.mixer.Sound("assets/sounds/click.ogg"),
            'draga' : pygame.mixer.Sound("assets/sounds/draga.ogg"),
            'tir' : pygame.mixer.Sound("assets/sounds/tir.ogg"),
        }

    def play(self, name): 
       self.sounds[name].play()