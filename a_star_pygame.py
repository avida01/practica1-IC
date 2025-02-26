import pygame
import math
import heapq

# Configuración de la cuadrícula
GRID_SIZE = (10, 10)
CELL_SIZE = 50
SCREEN_SIZE = (GRID_SIZE[1] * CELL_SIZE, GRID_SIZE[0] * CELL_SIZE)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

MOVES = [
    (0, 1), (1, 0), (0, -1), (-1, 0),
    (1, 1), (-1, 1), (1, -1), (-1, -1)
]

class Node:
    def __init__(self, x, y, g, h, parent=None):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
    
    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def a_star(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, Node(start[0], start[1], 0, heuristic(start, goal)))
    visited = set()
    
    while open_list:
        current = heapq.heappop(open_list)
        
        if (current.x, current.y) == goal:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]
        
        visited.add((current.x, current.y))
        
        for dx, dy in MOVES:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < GRID_SIZE[0] and 0 <= ny < GRID_SIZE[1] and grid[nx][ny] == 0 and (nx, ny) not in visited:
                cost = current.g + (1.41 if dx != 0 and dy != 0 else 1)
                heapq.heappush(open_list, Node(nx, ny, cost, heuristic((nx, ny), goal), current))
    
    return []

def draw_grid(screen, grid, path, waypoints):
    for x in range(GRID_SIZE[0]):
        for y in range(GRID_SIZE[1]):
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE if grid[x][y] == 0 else BLACK
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLUE, rect, 1)
            
            if (x, y) in waypoints:
                pygame.draw.rect(screen, YELLOW, rect)
            elif (x, y) in path:
                pygame.draw.rect(screen, GREEN, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("A* Pathfinding with Waypoints")
    clock = pygame.time.Clock()

    def reset():
        return [
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        ]
    
    grid = reset()
    start = (0, 0)
    goal = (9, 9)
    waypoints = [(2, 2), (0, 9), (6, 7)]
    
    def find_path():
        full_path = []
        prev = start
        for wp in waypoints + [goal]:
            sub_path = a_star(grid, prev, wp)
            if not sub_path:
                print("No path found!")
                return []
            full_path.extend(sub_path[1:])
            prev = wp
        return full_path
    
    full_path = find_path()
    running = True
    vehicle_pos = start
    step = 0
    
    while running:
        screen.fill(WHITE)
        draw_grid(screen, grid, full_path[:step], waypoints)
        
        if step < len(full_path):
            vehicle_pos = full_path[step]
            step += 1
        
        pygame.draw.rect(screen, RED, (vehicle_pos[1] * CELL_SIZE, vehicle_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        clock.tick(5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    grid = reset()
                    full_path = find_path()
                    vehicle_pos = start
                    step = 0
    
    pygame.quit()

if __name__ == "__main__":
    main()
