import pygame, math

from src.ball import Ball
from src.course import Course
from src.obstacle import Obstacle
from src.hole import Hole


class GameData:

    def __init__(self) -> None:

        self.strokes = 0
        
        self.line_pos = [(), ()]
        self.offset = ()

        
        self.obstacles = [Obstacle((2, 7), (0, 0)),
                          Obstacle((6, 1), (7, 6)),
                          Obstacle((1, 13), (12, 7)),
                          
                          Obstacle((7, 1), (1, 11)),
                          Obstacle((1, 5), (7 ,12)),
                          
                          Obstacle((3, 1), (15, 13)),
                          Obstacle((2, 1), (13, 8)),
                          Obstacle((2, 1), (18, 8)),
                          Obstacle((1, 2), (11, 2))]

        self.is_draw_line = False

    def get_offset(self):

        offset = [(self.line_pos[0][0] - self.line_pos[1][0]) / 25, 
                (self.line_pos[0][1] - self.line_pos[1][1]) / 25]

        return offset
              
    def get_line_pos(self):

        return self.line_pos
    
    def draw_line(self, startpos, win):

        pygame.draw.line(win, "red", startpos, pygame.mouse.get_pos(), 10)

    def draw_obstacles(self, win):

        for obs in self.obstacles:

            obs.draw(win)

class Window:

    def __init__(self):

        self.win = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Golf Without Friends!")
        self.clock = pygame.time.Clock()

    def setup_objects(self):

        self.data = GameData()
        self.ball = Ball((16, 17))
        self.course = Course(800)
        self.hole = Hole((5, 13))

    def update_objects(self):

        self.ball.update()
        self.ball.collision(self.data.obstacles, self.hole)
        pygame.display.update()
        self.clock.tick(60)

    def draw_objects(self):
 
        self.win.fill((155, 192, 72))

        self.course.draw_course(self.win)

        self.data.draw_obstacles(self.win)

        self.hole.draw(self.win)

        self.ball.draw(self.win)

        if self.data.is_draw_line:
            self.data.draw_line(self.data.line_pos[0], self.win)


    def check_for_input(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                self.data.line_pos[0] = pygame.mouse.get_pos()
                self.data.is_draw_line = True

            elif event.type == pygame.MOUSEBUTTONUP:

                self.data.line_pos[1] = pygame.mouse.get_pos()

                self.ball.move_ball(self.data.get_line_pos(), self.data.get_offset())
                self.ball.get_hole_pos((self.hole.x * 40, self.hole.y * 40))
                
                self.ball.x_friction, self.ball.y_friction = self.ball.vel[0] / 100, self.ball.vel[1] / 100

                self.data.is_draw_line = False

                self.data.strokes += 1
    

    def main_loop(self, run=True):

        while run:

            self.check_for_input()
            self.update_objects()
            self.draw_objects()

    def start(self):

        self.setup_objects()
        self.main_loop()

window = Window()
window.start()
    