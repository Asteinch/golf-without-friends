import pygame, random


class Hole:

    def __init__(self, pos):
        
        self.x, self.y = pos[0], pos[1]
        self.rect = pygame.Rect(self.x * 40 + 10, self.y * 40 + 10, 20, 20)


    def draw(self, win):

        pygame.draw.circle(win, pygame.Color("gray30"), (self.x * 40 + 20,self.y*40+20), 20)

    def get_hole_pos(self):

        return (self.x, self.y)

    