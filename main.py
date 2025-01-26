import os
import random
from colorama import Fore, Style, init

init(autoreset=True)

map_lst = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' ,'*', '*'],
    ['*', '&', ' ', '$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', '&', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', '@', '&', ' ', ' ', ' ', ' ', '&', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
    ['*', '&', '$', '$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '$', '$', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', '&', ' ', ' ', '&', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '&', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*', '*' ,'*', '*'],
    ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
    ['*', '$', '$', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
    ['*', '$', '$', ' ', '&', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '&', '*', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' ,'*', '*'],
]

x, y = 3, 2
gold_collected = 0
goblins_killed = 0
health = 10

def print_map():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in map_lst:
        row_str = ''
        for cell in row:
            if cell == '*':
                row_str += Fore.RED + cell
            elif cell == '$':
                row_str += Fore.YELLOW + cell
            elif cell == '&':
                row_str += Fore.GREEN + cell
            elif cell == '@':
                row_str += Fore.WHITE + cell
            else:
                row_str += cell
        print(row_str)
    print(f"Gold collected: {gold_collected}, Goblins killed: {goblins_killed}, Health: {health}")
    print()

def move(dx, dy):
    global x, y, gold_collected, goblins_killed, health
    new_x, new_y = x + dx, y + dy
    target = map_lst[new_x][new_y]

    if target == ' ':
        map_lst[x][y] = ' '
        x, y = new_x, new_y
        map_lst[x][y] = '@'
    elif target == '$':
        map_lst[x][y] = ' '
        x, y = new_x, new_y
        map_lst[x][y] = '@'
        gold_collected += 1
        print("You picked up gold!")
    elif target == '&':
        if random.random() < 0.5:
            health -= 1
            print("A goblin attacks! You lose 1 health.")
            if health <= 0:
                print("You died! Game over.")
                exit()
        map_lst[x][y] = ' '
        x, y = new_x, new_y
        map_lst[x][y] = '@'
        goblins_killed += 1
        print("You killed a goblin!")
    elif target == '*':
        print("You can't pass through the wall!")

    x, y = new_x, new_y

def restart_game():
    global x, y, gold_collected, goblins_killed, health, map_lst
    x, y = 3, 2
    gold_collected = 0
    goblins_killed = 0
    health = 10
    map_lst = [
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' ,'*', '*'],
        ['*', '&', ' ', '$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', '&', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', '@', '&', ' ', ' ', ' ', ' ', '&', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
        ['*', '&', '$', '$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '$', '$', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', '&', ' ', ' ', '&', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '&', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
        ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*', '*' ,'*', '*'],
        ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
        ['*', '$', '$', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
        ['*', '$', '$', ' ', '&', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', '&', '*', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ' ,' ', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' ,'*', '*'],
    ]

print_map()

while True:
    move_input = input("Enter W/A/S/D to move (or Q to quit, R to restart): ").lower()
    if move_input == 'w':
        move(-1, 0)
    elif move_input == 's':
        move(1, 0)
    elif move_input == 'a':
        move(0, -1)
    elif move_input == 'd':
        move(0, 1)
    elif move_input == 'q':
        print("Exiting the game.")
        break
    elif move_input == 'r':
        restart_game()
        print("Game restarted!")
    else:
        print("Invalid command!")
    print_map()

    if goblins_killed == 10:
        print("You win!")
        break
