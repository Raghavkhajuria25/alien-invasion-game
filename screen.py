from settings import (
    WIDTH,
    HEIGHT,
    BLACK,
    WHITE,
    GREEN,
    RED,
    YELLOW,
    font,
    big_font
)


def draw_score(screen, score, level, lives):

    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    level_text = font.render(
        f"Level: {level}",
        True,
        WHITE
    )

    lives_text = font.render(
        f"Lives: {lives}",
        True,
        WHITE
    )

    screen.blit(score_text, (30, 20))

    screen.blit(
        level_text,
        (WIDTH // 2 - 50, 20)
    )

    screen.blit(
        lives_text,
        (WIDTH - 160, 20)
    )


def start_screen(screen):

    screen.fill(BLACK)

    title = big_font.render(
        "ALIEN INVASION",
        True,
        GREEN
    )

    instruction = font.render(
        "Press SPACE to Start",
        True,
        WHITE
    )

    controls = font.render(
        "LEFT / RIGHT = Move     SPACE = Shoot",
        True,
        WHITE
    )

    screen.blit(
        title,
        (
            WIDTH // 2 - title.get_width() // 2,
            HEIGHT // 2 - 130
        )
    )

    screen.blit(
        instruction,
        (
            WIDTH // 2 - instruction.get_width() // 2,
            HEIGHT // 2
        )
    )

    screen.blit(
        controls,
        (
            WIDTH // 2 - controls.get_width() // 2,
            HEIGHT // 2 + 60
        )
    )


def game_over_screen(screen, score):

    screen.fill(BLACK)

    game_over = big_font.render(
        "GAME OVER",
        True,
        RED
    )

    final_score = font.render(
        f"Final Score: {score}",
        True,
        WHITE
    )

    restart = font.render(
        "Press R to Restart",
        True,
        YELLOW
    )

    screen.blit(
        game_over,
        (
            WIDTH // 2 - game_over.get_width() // 2,
            HEIGHT // 2 - 130
        )
    )

    screen.blit(
        final_score,
        (
            WIDTH // 2 - final_score.get_width() // 2,
            HEIGHT // 2 - 10
        )
    )

    screen.blit(
        restart,
        (
            WIDTH // 2 - restart.get_width() // 2,
            HEIGHT // 2 + 60
        )
    )