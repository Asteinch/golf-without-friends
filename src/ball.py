import pygame
import math

from settings import * 

class Ball:

    def __init__(self, pos):

        self.sprite = pygame.image.load(RES_PATH + "ball.png")
        self.x, self.y = pos[0] * 40 + self.sprite.get_width() / 2, pos[1] * 40 + self.sprite.get_height() / 2

        self.x_friction, self.y_friction = 0, 0

        self.frames_since_goal = 0

        self.target_pos = (self.x, self.y)
        self.vel = (0, 0)

        self.mask = pygame.mask.from_surface(self.sprite)

        self.in_hole = False

    def move_ball(self, line_pos, offset):

        self.target_pos = line_pos[1]
        self.vel = offset
        
    def update(self):

        if (self.x, self.y) != (0,0):

            self.x += self.vel[0]
            self.y += self.vel[1]

            # Applies friciton when the ball moves to the right
            if self.vel[0] > 0:
                self.vel = (self.vel[0] - abs(self.x_friction), self.vel[1])
                if self.vel[0] < 0:
                    self.vel = (0, self.vel[1]) 

            # Applies friciton when the ball moves to the left
            if self.vel[0] < 0:
                self.vel = (self.vel[0] + abs(self.x_friction), self.vel[1])
                if self.vel[0] > 0:
                    self.vel = (0, self.vel[1])

            # Applies friciton when the ball moves down
            if self.vel[1] > 0:
                self.vel = (self.vel[0], self.vel[1] - abs(self.y_friction))
                if self.vel[1] < 0:
                    self.vel = (self.vel[0], 0)

            # Applies friciton when the ball moves up
            if self.vel[1] < 0:
                self.vel = (self.vel[0], self.vel[1] + abs(self.y_friction))
                if self.vel[1] > 0:
                    self.vel = (self.vel[0], 0)

    def collision(self, obs, hole):

        # Wall collision  
        if self.x + self.vel[0] > 800 - self.sprite.get_width() or self.x +self.vel[0]< 0:

            self.vel = (self.vel[0] * -1, self.vel[1])
            
        if self.y + self.vel[1] > 800 - self.sprite.get_height() or self.y + self.vel[1] < 0:
            
            self.vel = (self.vel[0], self.vel[1] * -1)

        # Obstacle collisions

        for ob in obs:
            if pygame.Rect(self.x + self.vel[0], self.y, self.sprite.get_width(), self.sprite.get_height()).colliderect(ob):
                self.vel = (self.vel[0] * -1, self.vel[1])
            if pygame.Rect(self.x, self.y + self.vel[1], self.sprite.get_width(), self.sprite.get_height()).colliderect(ob):
                self.vel = (self.vel[0], self.vel[1] * -1)


        # Hole Collisions

        if pygame.Rect(self.x - (self.vel[0]), self.y - (self.vel[1]), self.sprite.get_width(), self.sprite.get_height()).colliderect(hole.rect):
            self.vel = (0, 0)
            self.goal_animation()


    def goal_animation(self):

        self.frames_since_goal += 1
        self.sprite = pygame.transform.scale(self.sprite, (25 - self.frames_since_goal, 25- self.frames_since_goal))
        self.sprite = pygame.transform.rotate(self.sprite, 5)

        self.x = self.hole_pos[0] + self.sprite.get_width() / 2
        self.y = self.hole_pos[1] + self.sprite.get_height() / 2

    def win_state(self):


        if self.sprite.get_height() == 7:

            return True

    def get_hole_pos(self, holepos):

        self.hole_pos = holepos 
            
    def draw(self, win):

        win.blit(self.sprite, (self.x, self.y))

