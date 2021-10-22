import random
import pygame

class TestGame:

    def __init__(self):
        self.screen = None
        self.game_is_running = True
        self.box_position_x = 0
        self.box_position_y = 0
        self.background_rect = pygame.Rect(0, 0, 800, 600)
        self.food = 0

    def draw_box(self):
        box_colour = (245, 101, 44)
        pygame.draw.rect(self.screen, box_colour, (self.box_position_x, self.box_position_y,  20, 20))

    def draw_food(self, amount):
        box_colour = (20, 240, 120)

        for i in range(amount):
            pygame.draw.rect(self.screen, box_colour, (random.randrange(800), random.randrange(600),  20, 20))

    def border_patrol(self):
        if self.box_position_x < 0:
            self.box_position_x = 0
        elif self.box_position_x >= 780:
            self.box_position_x = 780

        if self.box_position_y < 0:
            self.box_position_y = 0
        elif self.box_position_y >= 580:
            self.box_position_y = 580

    def box_control(self, event):
        if event.key == pygame.K_DOWN:
            self.box_position_y += 50
        elif event.key == pygame.K_UP:
            self.box_position_y -= 50
        elif event.key == pygame.K_RIGHT:
            self.box_position_x += 50
        elif event.key == pygame.K_LEFT:
            self.box_position_x -= 50

    def run_game(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        pygame.init()

        pygame.display.set_caption("Teeeeeeeeeeeeeest")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True
        self.draw_food(5)

        while self.game_is_running:
            # limit frame speed to 30 fps
            time_passed = clock.tick(30)
            #self.screen.fill((55, 55, 55), self.background_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False
                    else:
                        self.box_control(event)
                        self.border_patrol()

            self.draw_box()
            # final draw
            pygame.display.flip()

myGame = TestGame()
myGame.run_game()