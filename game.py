import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 9
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

# Colors
ALIVE_COLOR = (0, 255, 0)  # Green for alive cells
DEAD_COLOR = (0, 0, 0)     # Black for dead cells

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Initialize grid with dead cells
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Function to draw the grid
def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            color = ALIVE_COLOR if grid[y][x] == 1 else DEAD_COLOR
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (50, 50, 50), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)  # Grid lines

# Function to update the grid based on Conway's rules
def update_grid():
    global grid
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    
    for y in range(ROWS):
        for x in range(COLS):
            neighbors = count_neighbors(x, y)
            if grid[y][x] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[y][x] = 1  # Stay alive
                else:
                    new_grid[y][x] = 0  # Die
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1  # Become alive
                
    grid = new_grid

# Function to count the neighbors of a cell
def count_neighbors(x, y):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % COLS, (y + dy) % ROWS  # Wrap around the grid
            count += grid[ny][nx]
    return count

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True
    simulate = False  # To toggle simulation on/off

    while running:
        screen.fill((0, 0, 0))  # Clear the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Toggle cell state on mouse click
                x, y = event.pos
                grid[y // CELL_SIZE][x // CELL_SIZE] = 1 - grid[y // CELL_SIZE][x // CELL_SIZE]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press SPACE to toggle simulation
                    simulate = not simulate

        if simulate:
            update_grid()

        # Draw the grid
        draw_grid()

        # Update the display
        pygame.display.flip()

        # Control the speed of the simulation
        clock.tick(10)  # Update at 10 FPS for a reasonable simulation speed

    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()
