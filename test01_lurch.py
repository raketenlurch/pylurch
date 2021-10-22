import pygame

class TestGame:

    def __init__(self):
        self.screen = None
        self.game_is_running = True

    def draw_box(self):
        box_colour = (245, 101, 44)
        pygame.draw.rect(self.screen, box_colour, (10, 10, 20, 20))

    def run_game(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        pygame.init()

        pygame.display.set_caption("Teeeeeeeeeeeeeest")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True

        while self.game_is_running:
            # limit frame speed to 30 fps
            time_passed = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False
                    elif event.key == pygame.K_DOWN:
                        pass

            self.draw_box()
            # final draw
            pygame.display.flip()

myGame = TestGame()
myGame.run_game()