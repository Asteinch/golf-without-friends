import pygame, math

from src.ball import Ball
from src.course import Course
from src.obstacle import Obstacle
from src.hole import Hole

class Game:

    def __init__(self):

        self.win = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Golf Without Friends!")
        self.clock = pygame.time.Clock()

        self.is_draw_line = False
        self.line_pos = [(), ()]

        self.strokes = 0
        self.level = 1

    def setup_objects(self):

        self.ball = Ball((16, 17))
        self.course = Course(800)
        self.hole = Hole((5, 13))

        self.load_level(self.level)

    def update_objects(self):

        self.ball.update()
        self.ball.collision(self.obstacles, self.hole)

        if self.ball.win_state():
            print("cock")
            self.level += 1
            self.load_level(self.level)

        pygame.display.update()
        self.clock.tick(60)

    def draw_objects(self):
 
        self.win.fill((155, 192, 72))

        self.course.draw_course(self.win)
        
        for ob in self.obstacles:

            ob.draw(self.win)

        self.hole.draw(self.win)
        self.ball.draw(self.win)

        if self.is_draw_line:
            pygame.draw.line(self.win, "red", self.line_pos[0], pygame.mouse.get_pos(), 10)



    def check_for_input(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                self.line_pos[0] = pygame.mouse.get_pos()
                self.is_draw_line = True

            elif event.type == pygame.MOUSEBUTTONUP:

                self.line_pos[1] = pygame.mouse.get_pos()

                self.ball.move_ball(self.line_pos, self.get_line_offset())
                self.ball.get_hole_pos((self.hole.x * 40, self.hole.y * 40))
                
                self.ball.x_friction, self.ball.y_friction = self.ball.vel[0] / 100, self.ball.vel[1] / 100

                self.is_draw_line = False

                self.strokes += 1


    def load_level(self, level):

        if level == 1:
            self.obstacles = [Obstacle((2, 7), (0, 0)),
                Obstacle((6, 1), (7, 6)),
                Obstacle((1, 13), (12, 7)),
                          
                Obstacle((7, 1), (1, 11)),
                Obstacle((1, 5), (7 ,12)),
                          
                Obstacle((3, 1), (15, 13)),
                Obstacle((2, 1), (13, 8)),
                Obstacle((2, 1), (18, 8)),
                Obstacle((1, 2), (11, 2))]
            
        if level == 2:
            self.obstacles = []
            self.ball = Ball((16, 17))
            

            
    def get_line_offset(self):

        offset = [(self.line_pos[0][0] - self.line_pos[1][0]) / 25, 
                (self.line_pos[0][1] - self.line_pos[1][1]) / 25]

        return offset
    

    def main_loop(self, run=True):

        while run:

            self.check_for_input()
            self.update_objects()
            self.draw_objects()

    def start(self):

        self.setup_objects()
        self.main_loop()

window = Game()
window.start()
    