import pygame
# from game.game_logic import GameLogic
from ui.display import Display
# from ui.input_handler import InputHandler

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('PyCheckers')

    # game_logic = GameLogic()
    display = Display(screen)
    # input_handler = InputHandler()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # input_handler.handle_event(event, game_logic)

        # game_logic.update()
        # display.draw(game_logic.board)
        pygame.display.flip() 


    pygame.quit()
    

if __name__ == "__main__":
    main()
