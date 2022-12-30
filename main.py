import pygame as pg
from random import randrange

pg.init()

WINDOW = 1000

background_image = pg.image.load("images/background.png")

screen = pg.display.set_mode([WINDOW] * 2)
pg.display.set_caption("Cool Snake")
clock = pg.time.Clock()

def game():
    WINDOW = 1000
    TILE_SIZE = 50
    RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
    snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
    snake.center = get_random_position()
    length = 1
    segments = [snake.copy()]
    snake_dir = (0, 0)
    time, time_step = 0, 110
    food = snake.copy()
    food.center = get_random_position()
    game_over_show = 0
    font = pg.font.Font('freesansbold.ttf', 90)
    font2 = pg.font.Font('freesansbold.ttf', 80)
    select_button = 1

    game_over_text = font.render('GAME OVER!', True, 'blue')
    game_over_textRect = game_over_text.get_rect()
    game_over_textRect.center = (WINDOW // 2, WINDOW // 2 - 200)

    restart_text = font2.render('Restart', True, 'blue')
    restart_textRect = restart_text.get_rect()
    restart_textRect.center = (WINDOW // 2, WINDOW // 2 + 90)

    menu_text = font2.render('Main Menu', True, 'blue')
    menu_textRect = menu_text.get_rect()
    menu_textRect.center = (WINDOW // 2 + 80, WINDOW // 2 + 170)

    x_text = font2.render('X', True, 'white')
    x_textRect = x_text.get_rect()
    x_textRect.center = (WINDOW // 2 - 180, WINDOW // 2 + 90)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    snake_dir = (0, -TILE_SIZE)
                if event.key == pg.K_s:
                    snake_dir = (0, TILE_SIZE)
                if event.key == pg.K_a:
                    snake_dir = (-TILE_SIZE, 0)
                if event.key == pg.K_d:
                    snake_dir = (TILE_SIZE, 0)
                if game_over_show == 1 and event.key == pg.K_DOWN:
                    x_textRect.center = (WINDOW // 2 -180, WINDOW // 2 + 170)
                    select_button = 2
                if game_over_show == 1 and event.key == pg.K_UP:
                    x_textRect.center = (WINDOW // 2 - 180, WINDOW // 2 + 90)
                    select_button = 1
                if game_over_show == 1 and select_button == 1 and event.key == pg.K_RETURN:
                    snake.center, food.center = get_random_position(), get_random_position()
                    length, snake_dir = 1, (0, 0)
                    segments = [snake.copy()]
                    game_over_show = 0
                if game_over_show == 1 and select_button == 2 and event.key == pg.K_RETURN:
                    main_menu()

        screen.fill('black')
        screen.blit(background_image, (0, 0))

        self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1

        if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
            game_over_show = 1
            snake.right = 5000000
            food.right = 5000000

        pg.draw.rect(screen, 'red', food)
        [pg.draw.rect(screen, 'green', segment) for segment in segments]

        if game_over_show == 1:
            screen.blit(game_over_text, game_over_textRect)
            screen.blit(restart_text, restart_textRect)
            screen.blit(x_text, x_textRect)
            screen.blit(menu_text, menu_textRect)

        if snake.center == food.center:
            food.center = get_random_position()
            length += 1

        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]
        pg.display.flip()
        clock.tick(60)

def main_menu():
    select_option = 1

    font = pg.font.Font('freesansbold.ttf', 100)
    font2 = pg.font.Font('freesansbold.ttf', 90)
    font3 = pg.font.Font('freesansbold.ttf', 60)
    font4 = pg.font.Font('freesansbold.ttf', 20)

    game_name_text = font.render('Cool Snake', True, 'blue')
    game_name_textRect = game_name_text.get_rect()
    game_name_textRect.center = (WINDOW // 2, WINDOW // 2 - 300)

    start_text = font2.render('Start', True, 'blue')
    start_textRect = start_text.get_rect()
    start_textRect.center = (WINDOW // 2, WINDOW // 2)

    exit_text = font2.render('Exit', True, 'blue')
    exit_textRect = exit_text.get_rect()
    exit_textRect.center = (WINDOW // 2 - 15, WINDOW // 2 + 110)

    x_text = font2.render('X', True, 'white')
    x_textRect = x_text.get_rect()
    x_textRect.center = (WINDOW // 2 - 160, WINDOW // 2)

    creator_text = font3.render('Made by MikeyDevStuff', True, 'white')
    creator_textRect = creator_text.get_rect()
    creator_textRect.center = (500, 960)

    control_text = font4.render('Controls: WASD to move, Up and down arrow keys to choose option,Enter to confirm your choice', True, 'white')
    control_textRect = control_text.get_rect()
    control_textRect.center = (500, 20)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    select_option = 2
                    x_textRect.center = (WINDOW // 2 - 160, WINDOW // 2 + 110)
                if event.key == pg.K_UP:
                    select_option = 1
                    x_textRect.center = (WINDOW // 2 - 160, WINDOW // 2)
                if select_option == 1 and event.key == pg.K_RETURN:
                    game()
                if select_option == 2 and event.key == pg.K_RETURN:
                    exit()


        screen.fill('black')
        screen.blit(background_image, (0,0))

        screen.blit(game_name_text, game_name_textRect)
        screen.blit(start_text, start_textRect)
        screen.blit(x_text, x_textRect)
        screen.blit(exit_text, exit_textRect)
        screen.blit(creator_text, creator_textRect)
        screen.blit(control_text, control_textRect)

        pg.display.flip()
        clock.tick(60)
main_menu()