import os
import random
from colorama import Fore, init

init(autoreset=True)

MAP_WIDTH = 14
MAP_HEIGHT = 14

WALL = '*'
EMPTY = ' '
GOLD = '$'
GOBLIN = '&'
PLAYER = '@'

def generate_dungeon():
    dungeon = [[WALL for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

    def carve_path(x, y):
        if x < 1 or y < 1 or x >= MAP_HEIGHT - 1 or y >= MAP_WIDTH - 1:
            return
        if dungeon[x][y] == EMPTY:
            return
        dungeon[x][y] = EMPTY
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            if 0 <= x + dx * 2 < MAP_HEIGHT and 0 <= y + dy * 2 < MAP_WIDTH:
                carve_path(x + dx * 2, y + dy * 2)
                dungeon[x + dx][y + dy] = EMPTY  # Ensure the path is continuous

    start_x, start_y = random.randint(1, MAP_HEIGHT // 2) * 2, random.randint(1, MAP_WIDTH // 2) * 2
    carve_path(start_x, start_y)

    # Check and ensure connectivity
    def is_connected():
        visited = [[False for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        stack = [(start_x, start_y)]  # Start from the initial carve point

        while stack:
            cx, cy = stack.pop()
            if not visited[cx][cy] and dungeon[cx][cy] != WALL:
                visited[cx][cy] = True
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < MAP_HEIGHT and 0 <= ny < MAP_WIDTH and not visited[nx][ny] and dungeon[nx][ny] != WALL:
                        stack.append((nx, ny))

        # Check if all accessible cells are visited
        for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                if dungeon[i][j] != WALL and not visited[i][j]:
                    return False
        return True

    # Ensure dungeon connectivity
    while not is_connected():
        carve_path(random.randint(1, MAP_HEIGHT // 2) * 2, random.randint(1, MAP_WIDTH // 2) * 2)

    # Add gold and goblins
    for _ in range(random.randint(5, 10)):
        x, y = random.randint(1, MAP_HEIGHT - 2), random.randint(1, MAP_WIDTH - 2)
        if dungeon[x][y] == EMPTY:
            dungeon[x][y] = GOLD

    for _ in range(random.randint(3, 7)):
        x, y = random.randint(1, MAP_HEIGHT - 2), random.randint(1, MAP_WIDTH - 2)
        if dungeon[x][y] == EMPTY:
            dungeon[x][y] = GOBLIN

    # Place the player at a valid spot
    placed_player = False
    while not placed_player:
        player_x, player_y = random.randint(1, MAP_HEIGHT - 2), random.randint(1, MAP_WIDTH - 2)
        if dungeon[player_x][player_y] == EMPTY:
            dungeon[player_x][player_y] = PLAYER
            placed_player = True

    return dungeon

def print_map(dungeon, gold_collected, goblins_killed, health):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "ASCII Odyssey V0.1")
    for row in dungeon:
        row_str = ''
        for cell in row:
            if cell == WALL:
                row_str += Fore.RED + cell
            elif cell == GOLD:
                row_str += Fore.YELLOW + cell
            elif cell == GOBLIN:
                row_str += Fore.GREEN + cell
            elif cell == PLAYER:
                row_str += Fore.WHITE + cell
            else:
                row_str += cell
        print(row_str)
    print(f"Gold collected: {gold_collected}, Goblins killed: {goblins_killed}, Health: {health}")
    print()

def move_player(dungeon, x, y, dx, dy, gold_collected, goblins_killed, health):
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < MAP_HEIGHT and 0 <= new_y < MAP_WIDTH:
        target = dungeon[new_x][new_y]
        if target == EMPTY:
            dungeon[x][y] = EMPTY
            dungeon[new_x][new_y] = PLAYER
            return new_x, new_y, gold_collected, goblins_killed, health
        elif target == GOLD:
            dungeon[x][y] = EMPTY
            dungeon[new_x][new_y] = PLAYER
            return new_x, new_y, gold_collected + 1, goblins_killed, health
        elif target == GOBLIN:
            if random.random() < 0.5:
                health -= 1
                if health <= 0:
                    print("You died! Game over.")
                    return x, y, gold_collected, goblins_killed, health  # No movement if dead
            dungeon[x][y] = EMPTY
            dungeon[new_x][new_y] = PLAYER
            return new_x, new_y, gold_collected, goblins_killed + 1, health
        elif target == WALL:
            print("You can't pass through the wall!")
    return x, y, gold_collected, goblins_killed, health  # If movement isn't valid, return current state

def restart_game():
    dungeon = generate_dungeon()
    x, y = 3, 2
    gold_collected = 0
    goblins_killed = 0
    health = 10
    return dungeon, x, y, gold_collected, goblins_killed, health

def inventory_and_heart(health, inventory):
    print(f"Health: {health}")
    print("Inventory: ", inventory)

dungeon = generate_dungeon()
x, y = 3, 2
gold_collected = 0
goblins_killed = 0
health = 10
inventory = []

print_map(dungeon, gold_collected, goblins_killed, health)

try:
    while True:
        move_input = input("Enter W/A/S/D to move (or Q to quit, R to restart, I to check inventory): ").lower()

        # Ensure the input is not empty before checking
        if move_input == '':
            print("Please enter a valid command.")
            continue

        if move_input in 'wasd':
            dx, dy = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}[move_input]
            x, y, gold_collected, goblins_killed, health = move_player(dungeon, x, y, dx, dy, gold_collected, goblins_killed, health)

        elif move_input == 'q':
            print("Exiting the game.")
            break

        elif move_input == 'r':
            dungeon, x, y, gold_collected, goblins_killed, health = restart_game()
            print("Game restarted!")

        elif move_input == 'i':
            inventory_and_heart(health, inventory)

        else:
            print("Invalid command!")

        print_map(dungeon, gold_collected, goblins_killed, health)

        if goblins_killed == 11:
            print("You win!")
            break

except KeyboardInterrupt:
    print("\nGame interrupted. Exiting...")
