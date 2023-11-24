import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
done = False
color = (255, 0, 0)
x = 200
y = 200
radius = 25
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > radius: y -= 20
    if pressed[pygame.K_DOWN] and y < 400 - radius: y += 20
    if pressed[pygame.K_LEFT] and x > radius: x -= 20
    if pressed[pygame.K_RIGHT] and x < 400 - radius: x += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x,y), radius)
    pygame.display.flip()

    clock.tick(60)