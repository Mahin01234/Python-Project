import pygame
import random
import sys
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

PLAYER_WIDTH = 80
PLAYER_HEIGHT = 20
PLAYER_SPEED = 7

STAR_RADIUS = 12
STAR_SPAWN_DELAY = 25

font = pygame.font.SysFont("arial", 30)
big_font = pygame.font.SysFont("arial", 60)

HIGH_SCORE_FILE = "highscore.txt"

def load_background():
    try:
        bg = pygame.image.load('background.jpg').convert()
        bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        return bg
    except:
        return None

background_img = load_background()

def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as f:
            try:
                return int(f.read())
            except:
                return 0
    return 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))

class Player:
    def __init__(self):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 20
        self.speed = PLAYER_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        if direction == "right" and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 3)

    def reset_position(self):
        self.rect.x = SCREEN_WIDTH // 2 - self.width // 2
        self.rect.y = SCREEN_HEIGHT - self.height - 20

class Star:
    def __init__(self):
        self.radius = STAR_RADIUS
        self.x = random.randint(self.radius, SCREEN_WIDTH - self.radius)
        self.y = -self.radius
        self.fall_speed = random.randint(3, 6)

    def fall(self):
        self.y += self.fall_speed

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, (255, 255, 150), (int(self.x), int(self.y)), self.radius-3)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius*2, self.radius*2)

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Catch The Falling Stars - P: Pause, R: Reset stars, ESC: Quit")

    high_score = load_high_score()
    score = 0
    player = Player()
    stars = []
    spawn_counter = 0
    paused = False

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_r:
                    # রিস্টার্ট কিন্তু স্কোর রিসেট না করে: শুধু তারা ও প্লেয়ার পজিশন রিসেট
                    stars.clear()
                    spawn_counter = 0
                    player.reset_position()
                    paused = False

        if not running:
            break

        if paused:
            screen.fill(BLACK)
            pause_text = big_font.render("PAUSED", True, GREEN)
            hint_text = font.render("Press P to resume, R to reset stars, ESC to quit", True, WHITE)
            screen.blit(pause_text, (SCREEN_WIDTH//2 - pause_text.get_width()//2, SCREEN_HEIGHT//2 - 50))
            screen.blit(hint_text, (SCREEN_WIDTH//2 - hint_text.get_width()//2, SCREEN_HEIGHT//2 + 50))
            pygame.display.flip()
            continue

        # ----- গেম লজিক (পজ না থাকলে) -----
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")

        spawn_counter += 1
        if spawn_counter >= STAR_SPAWN_DELAY:
            spawn_counter = 0
            stars.append(Star())

        for star in stars[:]:
            star.fall()
            if star.y + star.radius > SCREEN_HEIGHT:
                stars.remove(star)
            elif player.rect.colliderect(star.get_rect()):
                stars.remove(star)
                score += 1
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)

        # ----- ড্রইং -----
        if background_img:
            screen.blit(background_img, (0, 0))
        else:
            screen.fill(BLACK)

        player.draw(screen)
        for star in stars:
            star.draw(screen)

        score_text = font.render(f"Score: {score}", True, WHITE)
        high_score_text = font.render(f"High Score: {high_score}", True, YELLOW)
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (SCREEN_WIDTH - high_score_text.get_width() - 10, 10))

        hint = font.render("P: Pause  |  R: Reset stars (keep score)  |  ESC: Quit", True, (200,200,200))
        screen.blit(hint, (SCREEN_WIDTH//2 - hint.get_width()//2, SCREEN_HEIGHT - 30))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


    