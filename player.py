import pygame
from settings import WIDTH, HEIGHT, BLUE, WHITE

ship = pygame.Rect(
    WIDTH // 2 - 30,
    HEIGHT - 100,
    60,
    50
)

ship_speed = 7


def draw_ship(screen):

    pygame.draw.polygon(
        screen,
        BLUE,
        [
            (ship.centerx, ship.top),
            (ship.left, ship.bottom),
            (ship.centerx, ship.bottom - 15),
            (ship.right, ship.bottom)
        ]
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (ship.centerx, ship.top + 22),
        8
    )


def move_ship(keys):

    if keys[pygame.K_LEFT]:
        ship.x -= ship_speed

    if keys[pygame.K_RIGHT]:
        ship.x += ship_speed

    if ship.left < 0:
        ship.left = 0

    if ship.right > WIDTH:
        ship.right = WIDTH