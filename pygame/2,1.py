import pygame
import math
import time

pygame.init()


window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Clock')

clock_center = (200, 200)
clock_radius = 150


hour_hand_length = 60
hour_hand_width = 10
minute_hand_length = 90
minute_hand_width = 5
second_hand_length = 90
second_hand_width = 1


background_color = (255, 255, 255)
hour_hand_color=(0,0,0)


clock = pygame.image.load('main-clock.png')
rect = clock.get_rect()
rect.center = clock_center

def drawHand(angle, center, width, length):
  
    hour_hand_end = (clock_center[0] + length * math.cos(angle),
                     clock_center[1] + length * math.sin(angle))
    pygame.draw.line(window, hour_hand_color, center, hour_hand_end, width)



while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
   
    current_time = time.localtime()
    window.fill(background_color)
    window.blit(clock, rect)

    hour_angle = (current_time.tm_hour % 12 + current_time.tm_min / 60) * math.pi / 6 - math.pi / 2
    drawHand(hour_angle, clock_center, hour_hand_width, hour_hand_length)

    minute_angle = current_time.tm_min * math.pi / 30 - math.pi / 2
    drawHand(minute_angle, clock_center, minute_hand_width, minute_hand_length)

    second_angle = current_time.tm_sec * 2.0 * math.pi / 60.0 - math.pi / 2
    drawHand(second_angle, clock_center, second_hand_width, second_hand_length)

    pygame.display.update()