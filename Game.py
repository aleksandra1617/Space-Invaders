# # # # # # # # # # # # # # # # # # # # # # # # # SPACIFICATION (LOOSE) # # # # # # # # # # # # # # # # # # # # # # # #
# TODO (1) : Change the player movement to work with velocity                                                         #
# - consistently updating position by a set amount (+) or (-)                                                         #
# - make sure the ship will stops moving if not pressing any keys to move                                             #
# - limit the player movement so that they do not go out of the screen  TODO                                          #
# TODO (2) : Create a bullet                                                                                          #
# - Spawn a small rectangle at the position of the player                                                             #
# - Create an Update function for the bullet to make sure it moves with the player Update(player_x_pos)               #
# - On key press shoot projectiles                                                                                    #
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
from Player import Player, Bullet

pygame.init()


def main():
    loop = True

    window = pygame.display.set_mode((800, 520))
    pygame.display.set_caption("Invaders")

    # Create objects & Setup
    pl = Player()
    pl.setup(window)

    bullet_scale = 10

    # Dividing bullet_scale by 4 because the bullet width is half of the bullet_scale/height
    # halving that is the middle of the width
    bullet = Bullet(34, 3, pl.rect.centerx-bullet_scale/4, pl.rect.y, bullet_scale)

    # Game loop
    while loop:
        window.fill((10, 28, 48))

        # Render
        bullet.draw(window)
        pl.draw(window)

        # Update
        pl.fire(Bullet(34, 3, pl.rect.centerx-bullet_scale/4, pl.rect.y, bullet_scale))
        pl.movement(0.5)
        bullet.update(pl.rect)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                # Quit the game
                loop = False
                pygame.quit()
                quit()

        pygame.time.Clock().tick(30)
        pygame.display.update()


main()
