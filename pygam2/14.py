import pygame
import sys
import random
import os
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        # Draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

# Настройки окна
width, height = 1080, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Life Adventure Game")
sprite_folder = os.path.join('/Users/akbotasmail/pygam2','sprites')

# Загрузка изображений для анимации бега
player_frames_original = [pygame.image.load(os.path.join(sprite_folder, f'{i}.png')) for i in range(2, 4)]
player_frames = [pygame.transform.scale(image, (100, 160)) for image in player_frames_original]
player_index = 0

# Загрузка изображений для деталей с измененными размерами
detail_images = {
    "HEALTH": pygame.transform.scale(pygame.image.load(os.path.join(sprite_folder, 'gpt.png')), (50, 50)),
    "MOOD": pygame.transform.scale(pygame.image.load(os.path.join(sprite_folder, 'coffee.png')), (80, 80)),
    "NEGATIVE": pygame.transform.scale(pygame.image.load(os.path.join(sprite_folder, 'vape.png')), (80, 80)),
    "LIGHT_BLUE": pygame.transform.scale(pygame.image.load(os.path.join(sprite_folder, 'books.png')), (80, 80)),
    "PINK": pygame.transform.scale(pygame.image.load(os.path.join(sprite_folder, 'dumbell.png')), (80, 80)),
    "GPA": pygame.transform.scale(pygame.image.load(os.path.join(sprite_folder, 'gpa.png')), (50, 50)),
    "MOODSCALE": pygame.transform.scale(pygame.image.load(os.path.join(sprite_folder, 'smile.png')), (50, 50)),
}


background_image = pygame.image.load(os.path.join(sprite_folder, '88.png'))
background_image = pygame.transform.scale(background_image, (width, height/1.43))
bg_x = 0

# Игрок
player_size = 150
player_x = 50
player_y = height - player_size - 70
jump_count = 10
is_jumping = False

# Детали для сбора
details = []
detail_speed = 30

# Здоровье и очки
health = 100
score = 0
font = pygame.font.Font(None, 36)
mood = 100

# Зона для появления деталей
spawn_zone = pygame.Rect(0, 0, width, height - player_size)

# Menu button settings
start_img = pygame.image.load(os.path.join('sprites', 'start_btn.png'))
exit_img = pygame.image.load(os.path.join('sprites', 'exit_btn.png'))

# Create button instances for the menu
start_button = Button(250, 200, start_img, 0.8)
exit_button = Button(650, 200, exit_img, 0.8)

# Initial state is the menu
state = "MENU"

# Main game loop
clock = pygame.time.Clock()
running = True

def draw_images_near_scales():
    screen.blit(detail_images["GPA"], (width - 250, 5))
    screen.blit(detail_images["MOODSCALE"], (width - 250, 40))

def draw_player(x, y):
    global player_index
    screen.blit(player_frames[player_index], (x, y))
    player_index = (player_index + 1) % len(player_frames)

def draw_details(details_list):
    for detail in details_list:
        screen.blit(detail["image"], detail["rect"])

def draw_health_bar():
    health_bar_width = int(200 * (health / 100))
    pygame.draw.rect(screen, GREEN, (width - 220, 20, health_bar_width, 20))

def show_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

def draw_mood_bar(mood):
    mood_bar_width = int(200 * (mood / 100))
    pygame.draw.rect(screen, ORANGE, (width - 220, 60, mood_bar_width, 20))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if state == "MENU":
        # Menu button logic
        if start_button.draw(screen):
            state = "GAME"
        elif exit_button.draw(screen):
            running = False
    elif state == "GAME":
        # Game logic
        if not is_jumping:
            if keys[pygame.K_SPACE]:
                is_jumping = True

        if is_jumping:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                player_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 10

        if random.randint(0, 100) < 20:
            horizontal_gap = 200
            detail_x = width + horizontal_gap
            if details:
                last_detail = details[-1]
                detail_x = last_detail["rect"].x + last_detail["rect"].w + horizontal_gap
            max_jump_height = player_y - (jump_count ** 2) * 2.0
            detail_y = random.randint(int(max_jump_height), height - player_size)
            health_effect = random.uniform(-10, 10)
            mood_effect = random.uniform(-10, 10)
            color = "HEALTH" if health_effect > 0 else "MOOD" if mood_effect > 0 else "NEGATIVE"
            details.append({"rect": pygame.Rect(detail_x, detail_y, 50, 50),
                            "health_effect": health_effect,
                            "mood_effect": mood_effect,
                            "image": detail_images[color]})

        for _ in range(5):
            if random.randint(0, 100) < 10:
                horizontal_gap = 200
                detail_x = width + horizontal_gap
                if details:
                    last_detail = details[-1]
                    detail_x = last_detail["rect"].x + last_detail["rect"].w + horizontal_gap
                max_jump_height = player_y - (jump_count ** 2) * 2.0
                detail_y = random.randint(int(max_jump_height), height - player_size)
                health_effect = random.uniform(5, 10) if random.choice([True, False]) else random.uniform(-10, -5)
                mood_effect = random.uniform(5, 10) if random.choice([True, False]) else random.uniform(-10, -5)
                color = "LIGHT_BLUE" if health_effect > 0 else "PINK" if mood_effect > 0 else "NEGATIVE"
                details.append({"rect": pygame.Rect(detail_x, detail_y, 50, 50),
                                "health_effect": health_effect,
                                "mood_effect": mood_effect,
                                "image": detail_images[color]})

        for detail in details:
            detail["rect"].x -= detail_speed

        for detail in details:
            if detail["rect"].colliderect(pygame.Rect(player_x, player_y, player_size, player_size)):
                details.remove(detail)
                score += 1
                health = min(100, health + detail["health_effect"])
                mood = min(100, mood + detail["mood_effect"])
            elif detail["rect"].x < 0:
                details.remove(detail)
                mood = max(0, mood - 0.5)
        if mood <= 0:
            health = max(0, health - 1)  
        else:
            health = max(0, health - 0.2)

        mood = max(0, mood - 0.4)

        if health <= 0:
            print("Game Over!")
            
            running = False
        #     screen.blit(game_over_image, (0, 0))
        bg_x -= 10
        screen.blit(background_image, (bg_x, 110))
        screen.blit(background_image, (bg_x + width, 110))

        # Reset the background position to create a looping effect
        if bg_x <= -width:
            bg_x = 0

        draw_player(player_x, player_y)
        draw_details(details)
        draw_health_bar()
        draw_mood_bar(mood)
        show_score()
        

        draw_images_near_scales()
    pygame.display.flip()
    clock.tick(10)

pygame.display.flip()
pygame.quit()
sys.exit()