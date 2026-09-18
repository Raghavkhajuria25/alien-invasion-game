import pygame
import sys

from settings import WIDTH, HEIGHT, BLACK
from player import ship, draw_ship, move_ship
from bullets import bullets, create_bullet, move_bullets, draw_bullets
from aliens import (
    aliens,
    alien_speed,
    alien_direction,
    alien_drop_distance,
    create_fleet,
    draw_alien
)
from screen import draw_score, start_screen, game_over_screen


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")

clock = pygame.time.Clock()


score = 0
lives = 3
level = 1

game_active = False


create_fleet()


while True:

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if not game_active:

                if event.key == pygame.K_SPACE:

                    game_active = True

                elif event.key == pygame.K_r:

                    game_active = True

            elif event.key == pygame.K_SPACE:

                create_bullet(ship)


    # GAME ACTIVE
    if game_active:

        # Ship
        keys = pygame.key.get_pressed()
        move_ship(keys)

        # Bullets
        move_bullets()

        # Aliens
        hit_edge = False

        for alien in aliens:

            next_x = alien.x + (
                alien_speed * alien_direction
            )

            if next_x <= 0:

                hit_edge = True
                break

            if next_x + alien.width >= WIDTH:

                hit_edge = True
                break

        if hit_edge:

            alien_direction *= -1

            for alien in aliens:

                alien.y += alien_drop_distance

        for alien in aliens:

            alien.x += (
                alien_speed * alien_direction
            )

        # Collision
        for bullet in bullets[:]:

            for alien in aliens[:]:

                if bullet.colliderect(alien):

                    if bullet in bullets:
                        bullets.remove(bullet)

                    if alien in aliens:
                        aliens.remove(alien)

                    score += 10

                    break

        # Alien reaches ship
        for alien in aliens:

            if alien.bottom >= ship.top:

                lives -= 1

                bullets.clear()

                ship.centerx = WIDTH // 2

                create_fleet()

                alien_direction = 1

                if lives <= 0:

                    game_active = False

                break

        # New level
        if len(aliens) == 0:

            level += 1

            create_fleet()

            alien_direction = 1


    # DRAW
    screen.fill(BLACK)

    if game_active:

        draw_ship(screen)

        draw_bullets(screen)

        for alien in aliens:

            draw_alien(screen, alien)

        draw_score(
            screen,
            score,
            level,
            lives
        )

    else:

        if lives <= 0:

            game_over_screen(
                screen,
                score
            )

        else:

            start_screen(screen)


    pygame.display.flip()

    clock.tick(60)