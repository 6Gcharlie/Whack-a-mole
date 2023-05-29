"""
The window test is a game loop for testing development features coming to the custard class
"""
# - Modules necessary for testing operation
import pygame
from assets import Pause, Developer, Hammer, Mole

# - This loop is used for testing the responsiveness of the game window
def two_player_game(game):
    "This game loop stores tests for me to trial frame rate and other features"

    # TODO: ADD A MATCH TIMER SO THAT THE GAME ENDS AFTER 60 SECONDS
    # TODO: HAVE HAMMER POINTS DISPLAYED ON SCREEN

    game.get_prev_time()
    developer_obj = Developer(game)
    pause_obj = Pause(game, [4, 4])
    p1_hammer_obj = Hammer(1, [100, 100])
    p2_hammer_obj = Hammer(2, [940, 100])
    mole = Mole()

    while game.loop == 'two player game':
        # - Delta time clock
        game.delta_clock()

        # - Events are caught and processed here
        for event in pygame.event.get():
            game.events(event)
            p1_hammer_obj.events(event, p2_hammer_obj, mole)
            p2_hammer_obj.events(event, p1_hammer_obj, mole)
            developer_obj.events(event)
            pause_obj.events(event, game)

        # - Game logic is processed here
        developer_obj.update(game)
        pause_obj.update(game)
        p1_hammer_obj.update(game)
        p2_hammer_obj.update(game)
        mole.update(game, p1_hammer_obj, p2_hammer_obj)

        # - Apply all normal pygame functions to the offscreen_surface
        game.surface.fill([200, 200, 200])
        pygame.draw.rect(game.surface, [155, 155, 155], [0, 640, 1280, 80])
        mole.draw(game.surface)
        p1_hammer_obj.draw(game.surface)
        p2_hammer_obj.draw(game.surface)

        # - Draw the screen
        developer_obj.draw(game.surface)
        pause_obj.draw(game.surface)

        game.draw()
