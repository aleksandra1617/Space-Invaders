import pygame

pygame.init()


class Bullet:

    def __init__(self, dmg, speed, pos_x, pos_y, scale):
        self.dmg = dmg
        self.speed = speed
        self.rect = pygame.Rect(pos_x, pos_y, scale - scale/2, scale)
        self.col = (50, 180, 255)
        self.fired = False

    def update(self):
        # Move the bullet up
        self.rect.y -= self.speed

    def draw(self, window):
        # Render self.img using the self.rect dimensions
        self.rect = pygame.draw.rect(window, self.col, self.rect)


class Player:

    def __init__(self, init_vel=0):
        self.velocity = init_vel
        self.img = pygame.image.load("Assets\playership.png")  # Load Img
        self.rect = self.img.get_rect()
        self.ammunition = []
        # No need to keep track of y becasue we are not moving up or down

    def setup(self, window):
        wind_rect = window.get_rect()

        # Set the self.rect pos to bottom center of screen
        self.rect.midbottom = wind_rect.midbottom

    # Draw will be almost the same no matter what we are drawing so it could be done in Utilities
    def draw(self, window):
        # Render player self.img using the rect dimensions
        window.blit(self.img, self.rect)

    # Magnitude serves to set the magnitude of velocity
    def movement(self, magnitude=1):
        key_state = pygame.key.get_pressed()

        # Instead of updating the position here we will only set velocity
        if key_state[pygame.K_RIGHT]:
            self.velocity += magnitude

        elif key_state[pygame.K_LEFT]:
            self.velocity -= magnitude

        # Smooth motion stop
        else:
            if self.velocity > 0:
                self.velocity -= magnitude
            else:
                self.velocity += magnitude

        # Update position
        self.rect.x += self.velocity

    def fire(self, bullet_scale):
        pygame.key.set_repeat(1, 10)
        key_state = pygame.key.get_pressed()

        # The second condition (len(self.ammunition) == 0) is to prevent adding more then one bullet per fire click.
        if key_state[pygame.K_SPACE]:

            # Load the bullet
            self.ammunition.append(Bullet(34, 7, self.rect.centerx - bullet_scale / 4, self.rect.y, bullet_scale))

