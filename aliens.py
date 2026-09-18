import pygame
from settings import GREEN, BLACK, WIDTH

aliens = []

alien_speed = 1.5
alien_direction = 1
alien_drop_distance = 20


def create_fleet():

    aliens.clear()

    rows = 4
    columns = 10

    for row in range(rows):

        for column in range(columns):

            x = 100 + column * 100
            y = 100 + row * 65

            alien = pygame.Rect(
                x,
                y,
                55,
                45
            )

            aliens.append(alien)


def draw_alien(screen, alien):

    pygame.draw.rect(
        screen,
        GREEN,
        alien,
        border_radius=8
    )

    pygame.draw.circle(
        screen,
        BLACK,
        (alien.x + 17, alien.y + 16),
        5
    )

    pygame.draw.circle(
        screen,
        BLACK,
        (alien.x + 38, alien.y + 16),
        5
    )

    pygame.draw.line(
        screen,
        GREEN,
        (alien.x + 12, alien.bottom),
        (alien.x + 5, alien.bottom + 10),
        5
    )

    pygame.draw.line(
        screen,
        GREEN,
        (alien.right - 12, alien.bottom),
        (alien.right - 5, alien.bottom + 10),
        5
    )