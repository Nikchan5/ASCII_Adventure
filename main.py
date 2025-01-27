############################
# Name: ASCII Odyssey
# Author: Eloen Dune
# Studio: 5Handsnakes Studio
# Version: 0.1.3
# Last Update: 27.01.2025
# Description: ASCII Odyssey is a console-based ASCII game created for fun.
#              Explore randomly generated dungeons, fight goblins, and survive
#              the depths of the odyssey.
# Repository: https://github.com/Nikchan5/ASCII_Adventure.git
# My Itchio: https://5handshakes-studio.itch.io/
# Contact: eloen007@gmail.com (for feedback and inquiries)
############################

import random
import os
from colorama import Fore, Style

EMPTY = ' '
WALL = '*'
GOLD = '$'
GOBLIN = '&'
PLAYER = '@'
CHEST = '!'
HEALTH = 100

def inventory(coins, chests_collected, health):
    inventory_ui = [
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', ' ', f'Coins: {coins}', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', f'Health: {health}', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', f'Chests: {chests_collected}', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ]
    for row in inventory_ui:
        print(''.join(row))

def generate_dungeon():
    dungeon_one = [
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', '*', '*', '*', '*', ' ', ' ', '*', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ]

    dungeon_two = [
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ]

    dungeon_three = [
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', '*', '*', '*', '*', ' ', ' ', '*', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ]

    dungeon_four = [
        ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',],
        ['*',' ',' ',' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ','*',],
        ['*',' ',' ',' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ','*',],
        ['*',' ',' ',' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ','*',],
        ['*',' ',' ',' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ','*',],
        ['*',' ',' ',' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ','*',],
        ['*','*','*','*','*','*',' ','*','*',' ','*','*',' ',' ','*',],
        ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',],
        ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',],
        ['*',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',],
        ['*',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',],
        ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',],
    ]

    dungeons = [dungeon_one, dungeon_two, dungeon_three, dungeon_four]
    return random.choice(dungeons)

player_x = 1
player_y = 1
monster_count = 0
coins = 0
chests_collected = 0
health = HEALTH

def place_items(dungeon, item, count):
    global monster_count
    map_height = len(dungeon)
    map_width = len(dungeon[0])
    
    for _ in range(count):
        while True:
            y = random.randint(1, map_height - 2)
            x = random.randint(1, map_width - 2)
            if 0 <= y < map_height and 0 <= x < map_width and dungeon[y][x] == ' ':
                dungeon[y][x] = item
                if item == GOBLIN:
                    monster_count += 1
                break

def generate_game():
    global dungeon, player_x, player_y, monster_count, MAP_HEIGHT, MAP_WIDTH, coins, chests_collected, health
    dungeon = generate_dungeon()
    MAP_HEIGHT, MAP_WIDTH = len(dungeon), len(dungeon[0])
    player_x, player_y = 1, 1
    monster_count = 0
    coins = 0
    chests_collected = 0
    health = HEALTH
    place_items(dungeon, GOLD, 3)
    place_items(dungeon, GOBLIN, 3)
    place_items(dungeon, CHEST, 2)

def get_map_dimensions(dungeon):
    return len(dungeon), len(dungeon[0])

MAP_HEIGHT, MAP_WIDTH = get_map_dimensions(generate_dungeon())

def print_dungeon(dungeon):
    for y, row in enumerate(dungeon):
        for x, cell in enumerate(row):
            if x == player_x and y == player_y:
                print(Fore.BLUE + PLAYER + Style.RESET_ALL, end='')
            elif cell == GOLD:
                print(Fore.YELLOW + cell + Style.RESET_ALL, end='')
            elif cell == GOBLIN:
                print(Fore.RED + cell + Style.RESET_ALL, end='')
            elif cell == CHEST:
                print(Fore.GREEN + cell + Style.RESET_ALL, end='')  # Color chest differently
            else:
                print(cell, end='')
        print()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def move_player(dx, dy, dungeon):
    global player_x, player_y, monster_count, coins, chests_collected, health
    new_x = player_x + dx
    new_y = player_y + dy
    if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
        if dungeon[new_y][new_x] != WALL:
            player_x, player_y = new_x, new_y
            if dungeon[new_y][new_x] == GOLD:
                coins += 1
                dungeon[new_y][new_x] = EMPTY
            elif dungeon[new_y][new_x] == GOBLIN:
                health -= 10
                if health <= 0:
                    print("You died!")
                    exit()
                dungeon[new_y][new_x] = EMPTY
                monster_count -= 1
            elif dungeon[new_y][new_x] == CHEST:
                chests_collected += 1
                chest_reward = random.choice(['gold', 'monster'])
                if chest_reward == 'gold':
                    coins += 3
                    dungeon[new_y][new_x] = GOLD
                elif chest_reward == 'monster':
                    dungeon[new_y][new_x] = GOBLIN
                    monster_count += 1
            
            # Transition to the next dungeon if all goblins are defeated
            if monster_count == 0:
                print("All goblins are defeated! Proceeding to the next dungeon...")
                input("Press Enter to continue...")
                generate_game()  # Transition to the next level


def main():
    global dungeon, messages, coins, chests_collected, health
    generate_game()

    while True:
        clear_screen()
        print_dungeon(dungeon)

        # Check for 'E' press to show inventory
        move = input("Press 'E' to open inventory, or use WASD to move: ").lower()
        if move == 'e':
            inventory(coins, chests_collected, health)
            input("Press Enter to continue...")
            continue
        
        if move == 'w':
            move_player(0, -1, dungeon)
        elif move == 'a':
            move_player(-1, 0, dungeon)
        elif move == 's':
            move_player(0, 1, dungeon)
        elif move == 'd':
            move_player(1, 0, dungeon)
        elif move == 'r':
            print("Game restarted!")
            generate_game()
        elif move == 'q':
            print("You exited the game.")
            break

if __name__ == '__main__':
    main()
