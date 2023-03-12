import pygame

# initialize pygame
pygame.init()

# screen dimensions
screen_width = 700
screen_height = 500

# initialize screen
screen = pygame.display.set_mode((screen_width, screen_height))

# paddle dimensions
paddle_width = 15
paddle_height = 100

# initialize paddles
paddle1_x = 20
paddle1_y = (screen_height - paddle_height) / 2
paddle2_x = screen_width - 20 - paddle_width
paddle2_y = (screen_height - paddle_height) / 2

# ball dimensions
ball_width = 20
ball_height = 20

# initialize ball position
ball_x = (screen_width - ball_width) / 2
ball_y = (screen_height - ball_height) / 2

# ball speed
ball_speed_x = 5
ball_speed_y = 5

# paddle speed
paddle_speed = 5

# run the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update paddle position based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle_speed
    if keys[pygame.K_w]:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s]:
        paddle1_y += paddle_speed

    # keep paddles within screen
    paddle1_y = max(0, min(paddle1_y, screen_height - paddle_height))
    paddle2_y = max(0, min(paddle2_y, screen_height - paddle_height))

    # update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # bounce ball if it hits top/bottom of screen
    if ball_y <= 0 or ball_y + ball_height >= screen_height:
        ball_speed_y = -ball_speed_y

    # check for paddle collision
    if (ball_x <= paddle1_x + paddle_width and
        ball_y + ball_height >= paddle1_y and
        ball_y <= paddle1_y + paddle_height):
        ball_speed_x = -ball_speed_x
    if (ball_x + ball_width >= paddle2_x and
        ball_y + ball_height >= paddle2_y and
        ball_y <= paddle2_y + paddle_height):
        ball_speed_x = -ball_speed_x

    # check for game over
    if ball_x <= 0 or ball_x + ball_width >= screen_width:
        running = False

    # draw objects on screen
    screen.fill((0, 0, 0))
    pygame.dra
    w.rect(screen, (255, 255, 255), (paddle1_x, paddle1_y, paddle_width))
