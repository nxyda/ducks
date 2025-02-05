import pygame
import random


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ducks")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


duck_image = pygame.image.load("data/duck.png")
duck_image = pygame.transform.scale(duck_image, (50, 50))

crosshair_image = pygame.image.load("data/crosshair.png")
crosshair_image = pygame.transform.scale(crosshair_image, (50, 50))


clock = pygame.time.Clock()


def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font("arial"), size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


class Duck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = duck_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)
        self.speedx = random.randint(-4, 4)
        self.speedy = random.randint(1, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > screen_height or self.rect.left < 0 or self.rect.right > screen_width:
            self.kill()


all_sprites = pygame.sprite.Group()
ducks = pygame.sprite.Group()


def add_duck():
    if len(ducks) < 5:
        duck = Duck()
        all_sprites.add(duck)
        ducks.add(duck)


for i in range(5):
    add_duck()


score = 0


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in ducks if s.rect.collidepoint(pos)]
            for duck in clicked_sprites:
                score += 1
                duck.kill()
                add_duck()

    all_sprites.update()


    add_duck()

    screen.fill(WHITE)
    all_sprites.draw(screen)


    mouse_pos = pygame.mouse.get_pos()
    crosshair_rect = crosshair_image.get_rect(center=mouse_pos)
    screen.blit(crosshair_image, crosshair_rect)


    draw_text(screen, "Score: " + str(score), 30, screen_width / 2, 10)

    pygame.display.flip()

pygame.quit()
