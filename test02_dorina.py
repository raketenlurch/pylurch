import pygame


class TestGame:

    def __init__(self):
        self.screen = None
        self.game_is_running = True
        self.box_position_x = 0
        self.box_position_y = 0
        self.background_rect = pygame.Rect(0, 0, 800, 600)

    def draw_box(self):
        box_color = (245, 101, 44)
        pygame.draw.rect(self.screen, box_color, (self.box_position_x, self.box_position_y, 20, 20))

    def run_game(self):
        SCREENWIDTH = 800
        SCREENHEIGHT = 600

        pygame.init()
        pygame.display.set_caption("Test")
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True

        while self.game_is_running:
            # limit framespeed to 30fps
            time_passed = clock.tick(30)

            self.screen.fill((55, 55, 55), self.background_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False
                    elif event.key == pygame.K_DOWN:
                        self.box_position_y += 10
                    elif event.key == pygame.K_UP:
                        self.box_position_y -= 10
                    elif event.key == pygame.K_RIGHT:
                        self.box_position_x += 10
                    elif event.key == pygame.K_LEFT:
                        self.box_position_x -= 10

            self.draw_box()
            # final draw
            pygame.display.flip()


my_game = TestGame()
my_game.run_game()