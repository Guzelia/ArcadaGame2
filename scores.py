import pygame.font


class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color =(155, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
    def image_score(self):

