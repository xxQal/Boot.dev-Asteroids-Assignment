import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    x_pos = SCREEN_WIDTH // 2
    y_pos = SCREEN_HEIGHT // 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)
    player = Player(x_pos, y_pos)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        dt = (game_clock.tick(60)/1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        shot.kill()
                        asteroid.kill()
                if player.collides_with(asteroid):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
 