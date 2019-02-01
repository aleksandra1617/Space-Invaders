# # # # # # # # # # # # # # # # # # # # # # # # # SPACIFICATION (LOOSE) # # # # # # # # # # # # # # # # # # # # # # # #
# TODO (2) : add fire rate                                                                                            #                                                                  #
#                                                                                                                     #
# TODO (3) : Spawn alien, add alien route                                                                             #
# TODO (4) : Alien collision and response                                                                             #
# For consecutive shots:                                                                                              #
#  A) Assuming we only use the one bullet and keep reusing it, we can move the bullet back onto the player            #
#     when the bullet is out of the screen, but that would mean the player cannot shoot again until the bullet is reset.
#  B) We can spawn a new bullet every time the player shoots, and let it move out of the screen uninterrupted.        #
#     This will with time (long long time in this case) slow down the frame rate,                                     #
#     so we will have to delete the bullets which are going out of the screen.                                        #
# - when bullet hits alien, it dies                                                                                   #
# - when alien collides with player, player dies)                                                                     #
# - EXTRA: can add a bullet sprite/img just for the looks                                                             #
# - EXTRA: we can add a special alien which will shoot as well to make the game harder                                #
# - EXTRA: also adding a reload and a delay                                                                           #
# TODO (5) : Main Menu and Game Settings (can refer back to p.243 in book)                                            #
# TODO (6) : Create a save file and add two options for start on the menu "start new game" or "continue".             #
# - not secure as the file can be deleted and altered to get bonus score, level, auto kill an enemy, etc.             #
# TODO (7) : Score and Leaderboard                                                                                    #
# - we would need to have an array or a file with player names                                                        #
# Options:                                                                                                            #
#  A) ask the player to login with a password and username                                                            #
#  B) or use the menu "start new game" or "continue" in the main menu and add an additional player name on the save   #
# TODO (8) : Different bullets and enemies                                                                            #
# TODO (9) : Animation                                                                                                #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# imports
import pygame
from Player import Player

pygame.init()


def main():
    loop = True

    window = pygame.display.set_mode((800, 520))
    pygame.display.set_caption("Invaders")

    # Create objects & Setup
    pl = Player()
    pl.setup(window)
    bullet_scale = 10

    # Game loop
    while loop:
        window.fill((10, 28, 48))

        # Render
        pl.draw(window)

        # Update
        pl.fire(bullet_scale)
        pl.movement(0.5)

        for bullet in pl.ammunition:
            bullet.update()
            bullet.draw(window)

            # if the ammo is past the top border of the window
            if bullet.rect.y == 0:
                # Remove ammo
                pl.ammunition.remove(bullet)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                # Quit the game
                loop = False
                pygame.quit()
                quit()

        pygame.time.Clock().tick(30)
        pygame.display.update()


main()
