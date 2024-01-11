# Imports
import pygame
import random

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
GRID_SIZE = 20
SNAKE_SIZE = 20
FPS = 12

# Colors # RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Directions x y
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# Classes


# Snake Class
class Snake:
    def __init__(self):
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def get_head_position(self):
        # Head
        return self.positions[0]

    def get_body(self):
        return self.positions[1:]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (
            ((cur[0] + (x * SNAKE_SIZE)) % SCREEN_WIDTH),
            (cur[1] + (y * SNAKE_SIZE)) % SCREEN_HEIGHT,
        )

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()

        self.positions.insert(0, new)
        if len(self.positions) > self.score + 1:
            self.positions.pop()

    def reset(self):
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def change_direction(self, direction):
        if (
            direction[0] * -1 != self.direction[0]
            or direction[1] * -1 != self.direction[1]
        ):
            self.direction = direction


# Food Class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE * SNAKE_SIZE,
            random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE * SNAKE_SIZE,
        )

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.color,
            pygame.Rect(self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE),
        )


# Functions


# Make grid


# Game start condition


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SNAKE GAME PST")

    snake = Snake()
    food = Food()

    # Game to run infinitely until we quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)

        snake.update()
        screen.fill(BLACK)
        # Based on actions -> snake needs to update position

        # body rendering
        snake_body = snake.get_body()
        for pos in snake_body:
            pygame.draw.rect(
                screen, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE)
            )

        # head rendering
        snake_head = snake.get_head_position()
        pygame.draw.rect(
            screen,
            GREEN,
            pygame.Rect(snake_head[0], snake_head[1], SNAKE_SIZE, SNAKE_SIZE),
        )

        food.draw(screen)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
