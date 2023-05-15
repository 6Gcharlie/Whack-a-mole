"""
The window test is a game loop for testing development features coming to the custard class
"""
# - Modules necessary for testing operation
import pygame
from assets import Pause, Developer

# - This loop is used for testing the responsiveness of the game window
def two_player_game(game):
    "This game loop stores tests for me to trial frame rate and other features"
    # - Create a variable for time keeping

    # PLAYER ONE IS KEY 115 ---> ( S )
    # PLAYER TWO IS KEY 1073741905 ---> ( DOWN ARROW )
    p1_state = 'up'
    p2_state = 'up'

    game.get_prev_time()
    developer_obj = Developer(game)
    pause_obj = Pause(game, [4, 4])

    while game.loop == 'two player game':
        # - Delta time clock
        game.delta_clock()

        # - Events are caught and processed here
        for event in pygame.event.get():
            game.events(event)
            developer_obj.events(event)
            pause_obj.events(event, game)



            # - Hammer events. Hitting and lifting:
            if event.type == 768:
                match event.key:
                    case 115:
                        p1_state = 'down'
                    case 1073741905:
                        p2_state = 'down'

            if event.type == 769:
                match event.key:
                    case 115:
                        p1_state = 'up'
                    case 1073741905:
                        p2_state = 'up'


        # - Game logic is processed here
        developer_obj.update(game)
        pause_obj.update(game)

        # - Apply all normal pygame functions to the offscreen_surface
        game.surface.fill([200, 200, 200])

        if p1_state == 'down':
            pygame.draw.rect(game.surface, [255, 0, 0], [100, 100, 50, 50])
        
        if p2_state == 'down':
            pygame.draw.rect(game.surface, [0, 0, 255], [150, 100, 50, 50])

        # - Draw the screen
        developer_obj.draw(game.surface)
        pause_obj.draw(game.surface)
        game.draw()
