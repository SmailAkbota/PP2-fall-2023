import pygame
pygame.init()
# print(pygame.font.get_fonts())

W, H = 600, 400

f_sys = pygame.font.SysFont('arial', 12)
f = pygame.font.Font('Strawbale.ttf', 24)

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Fonts")
pygame.display.set_icon(pygame.image.load("MicrosoftTeams-image (3).png"))

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

sc_text = f.render("Hello world!", 1, RED, YELLOW)
pos = sc_text.get_rect(center=(W//2, H//2))

sc.fill(WHITE)
sc.blit(sc_text, pos)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    clock.tick(FPS)