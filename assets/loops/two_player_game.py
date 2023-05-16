"""
The window test is a game loop for testing development features coming to the custard class
"""
# - Modules necessary for testing operation
import pygame
from assets import Pause, Developer, Hammer

# - This loop is used for testing the responsiveness of the game window
def two_player_game(game):
    "This game loop stores tests for me to trial frame rate and other features"
    # - Create a variable for time keeping

    # PLAYER ONE IS KEY 115 ---> ( S )
    # PLAYER TWO IS KEY 1073741905 ---> ( DOWN ARROW )
    p1_hammer_obj = Hammer(1, [100, 100])
    p2_hammer_obj = Hammer(2, [940, 100])

    game.get_prev_time()
    developer_obj = Developer(game)
    pause_obj = Pause(game, [4, 4])

    while game.loop == 'two player game':
        # - Delta time clock
        game.delta_clock()

        # - Events are caught and processed here
        for event in pygame.event.get():
            game.events(event)
            p1_hammer_obj.events(event)
            p2_hammer_obj.events(event)
            developer_obj.events(event)
            pause_obj.events(event, game)

        p1_hammer_obj.update(game)
        p2_hammer_obj.update(game)

            # - Hammer events. Hitting and lifting:
            # if event.type == 768:
            #     match event.key:
            #         case 115:
            #             p1_state = 'down'
            #         case 1073741905:
            #             p2_state = 'down'

            # if event.type == 769:
            #     match event.key:
            #         case 115:
            #             p1_state = 'up'
            #         case 1073741905:
            #             p2_state = 'up'


        # - Game logic is processed here
        developer_obj.update(game)
        pause_obj.update(game)

        # - Apply all normal pygame functions to the offscreen_surface
        game.surface.fill([200, 200, 200])
        pygame.draw.rect(game.surface, [155, 155, 155], [0, 640, 1280, 80])

        # - Hammers
        p1_hammer_obj.draw(game.surface)
        p2_hammer_obj.draw(game.surface)

        # - Draw the screen
        developer_obj.draw(game.surface)
        pause_obj.draw(game.surface)
        game.draw()
