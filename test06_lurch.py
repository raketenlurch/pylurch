import random
import pygame


class TestGame:

    def __init__(self):
        self.screen = None
        self.game_is_running = True
        self.box_position_x = 0
        self.box_position_y = 0
        self.background_rect = pygame.Rect(0, 0, 800, 600)
        self.food = 5
        self.food_position_x = random.randrange(0, 800, 20)
        self.food_position_y = random.randrange(0, 600, 20)
        self.food_position_list = []
        self.score = 0

    def draw_box(self):
        box_colour = (245, 101, 44)
        pygame.draw.rect(self.screen, box_colour, (self.box_position_x, self.box_position_y,  20, 20))

    def food_positions(self, amount):
        for i in range(amount):
            self.food_position_x = random.randrange(0, 800, 20)
            self.food_position_y = random.randrange(0, 600, 20)
            self.food_position_list.append((self.food_position_x, self.food_position_y))

    def draw_food(self, food_position_x, food_position_y):
        box_colour = (20, 240, 120)
        pygame.draw.rect(self.screen, box_colour, (food_position_x, food_position_y, 20, 20))

    def eat_food(self):
        for coordinates in self.food_position_list:
            if self.box_position_x == coordinates[0] and self.box_position_y == coordinates[1]:
                self.food_position_list.remove((coordinates[0], coordinates[1]))
                self.score += 1
                self.food_positions(1)
                print(self.score)
                break

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
            self.box_position_y += 20
        elif event.key == pygame.K_UP:
            self.box_position_y -= 20
        elif event.key == pygame.K_RIGHT:
            self.box_position_x += 20
        elif event.key == pygame.K_LEFT:
            self.box_position_x -= 20

        self.eat_food()

    def run_game(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        pygame.init()

        pygame.display.set_caption("Test")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True
        self.food_positions(self.food)
        while self.game_is_running:
            # limit frame speed to 30 fps
            time_passed = clock.tick(30)
            self.screen.fill((55, 55, 55), self.background_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False
                    else:
                        self.box_control(event)
                        self.border_patrol()

            for i in range(len(self.food_position_list)):
                self.draw_food(self.food_position_list[i][0], self.food_position_list[i][1])
            self.draw_box()
            # final draw
            pygame.display.flip()


myGame = TestGame()
myGame.run_game()
