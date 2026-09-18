import pygame
from settings import YELLOW

bullets = []

bullet_speed = 10
bullet_width = 6
bullet_height = 20

MAX_BULLETS = 5


def create_bullet(ship):

    if len(bullets) < MAX_BULLETS:

        bullet = pygame.Rect(
            ship.centerx - bullet_width // 2,
            ship.top - bullet_height,
            bullet_width,
            bullet_height
        )

        bullets.append(bullet)


def move_bullets():

    for bullet in bullets[:]:

        bullet.y -= bullet_speed

        if bullet.bottom < 0:
            bullets.remove(bullet)


def draw_bullets(screen):

    for bullet in bullets:

        pygame.draw.rect(
            screen,
            YELLOW,
            bullet
        )