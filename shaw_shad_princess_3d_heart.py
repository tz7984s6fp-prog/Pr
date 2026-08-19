import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shaw shad princess")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 48, bold=True)
random.seed(7)
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 3)) for _ in range(100)]

def heart_points(cx, cy, scale, steps=220):
    pts = []
    for i in range(steps):
        t = 2 * math.pi * i / steps
        x = 16 * math.sin(t) ** 3
        y = -(13 * math.cos(t) - 5 * math.cos(2*t)
              - 2 * math.cos(3*t) - math.cos(4*t))
        pts.append((cx + x * scale, cy + y * scale))
    return pts

def draw_heart(surface, cx, cy, scale):
    # 3D depth
    depth = max(8, int(scale * 1.5))
    for d in range(depth, 0, -1):
        pts = heart_points(cx + d * 0.9, cy + d * 1.2, scale)
        pygame.draw.polygon(surface, (110, 8 + d, 55 + d), pts)

    # Pink heart
    pygame.draw.polygon(surface, (255, 70, 155), heart_points(cx, cy, scale))

    # Inner pink layer
    pygame.draw.polygon(
        surface, (255, 105, 180),
        heart_points(cx - scale * .15, cy - scale * .12, scale * .88)
    )

    # Bright highlight
    pygame.draw.polygon(
        surface, (255, 190, 225),
        heart_points(cx - scale * .45, cy - scale * .55, scale * .20)
    )

def draw_text(surface, cx, cy):
    text = font.render("Shaw shad princess", True, (255, 255, 255))
    surface.blit(text, text.get_rect(center=(cx, cy)))

running = True
while running:
    time_ms = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((8, 3, 14))

    # Background stars
    for x, y, r in stars:
        twinkle = .5 + .5 * math.sin(time_ms * .002 + x)
        pygame.draw.circle(screen, (255, 180, 220), (x, y), max(1, int(r * twinkle + 1)))

    # Pulsing / moving heart
    beat = 1.0 + .045 * math.sin(time_ms * .006)
    float_y = 10 * math.sin(time_ms * .0022)
    cx, cy = WIDTH // 2, HEIGHT // 2 + float_y

    # Large 3D pink heart
    draw_heart(screen, cx, cy, 15.2 * beat)

    # White writing inside the heart
    draw_text(screen, cx, cy + 8)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
