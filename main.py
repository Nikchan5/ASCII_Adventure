import os
import random
from colorama import Fore, Style, init

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
    for x in range(1, MAP_HEIGHT - 1):
        for y in range(1, MAP_WIDTH - 1):
            if random.random() < 0.7:
                dungeon[x][y] = EMPTY
    for _ in range(random.randint(5, 10)):
        x, y = random.randint(1, MAP_HEIGHT - 2), random.randint(1, MAP_WIDTH - 2)
        dungeon[x][y] = GOLD
    for _ in range(random.randint(3, 7)):
        x, y = random.randint(1, MAP_HEIGHT - 2), random.randint(1, MAP_WIDTH - 2)
        dungeon[x][y] = GOBLIN
    dungeon[3][2] = PLAYER
    return dungeon

def print_map(dungeon):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "ASCII Odyssey V0.2")
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

def move(dx, dy, dungeon):
    global x, y, gold_collected, goblins_killed, health
    new_x, new_y = x + dx, y + dy
    target = dungeon[new_x][new_y]

    if target == EMPTY:
        dungeon[x][y] = EMPTY
        x, y = new_x, new_y
        dungeon[x][y] = PLAYER
    elif target == GOLD:
        dungeon[x][y] = EMPTY
        x, y = new_x, new_y
        dungeon[x][y] = PLAYER
        gold_collected += 1
        print("You picked up gold!")
    elif target == GOBLIN:
        if random.random() < 0.5:
            health -= 1
            print("A goblin attacks! You lose 1 health.")
            if health <= 0:
                print("You died! Game over.")
                exit()
        dungeon[x][y] = EMPTY
        x, y = new_x, new_y
        dungeon[x][y] = PLAYER
        goblins_killed += 1
        print("You killed a goblin!")
    elif target == WALL:
        print("You can't pass through the wall!")

    x, y = new_x, new_y

def restart_game():
    global x, y, gold_collected, goblins_killed, health, dungeon
    x, y = 3, 2
    gold_collected = 0
    goblins_killed = 0
    health = 10
    dungeon = generate_dungeon()

dungeon = generate_dungeon()
x, y = 3, 2
gold_collected = 0
goblins_killed = 0
health = 10

print_map(dungeon)

while True:
    move_input = input("Enter W/A/S/D to move (or Q to quit, R to restart): ").lower()
    if move_input == 'w':
        move(-1, 0, dungeon)
    elif move_input == 's':
        move(1, 0, dungeon)
    elif move_input == 'a':
        move(0, -1, dungeon)
    elif move_input == 'd':
        move(0, 1, dungeon)
    elif move_input == 'q':
        print("Exiting the game.")
        break
    elif move_input == 'r':
        restart_game()
        print("Game restarted!")
    else:
        print("Invalid command!")
    print_map(dungeon)

    if goblins_killed == 11:
        print("You win!")
        break
