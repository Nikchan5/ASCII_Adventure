import os
import random

map_lst = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' ,'*', '*'],
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
           ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' ,'*', '*']]

x, y = 3, 2
gold_collected = 0
goblins_killed = 0
health = 10

def print_map():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in map_lst:
        print(''.join(row))
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
    elif target == '₽':
        # 50% chance for an attack
        if random.random() < 0.5:  # Using random.random() for a more explicit 50% chance
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

print_map()

while True:
    move_input = input("Enter W/A/S/D to move (or Q to quit): ").lower()
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
    else:
        print("Invalid command!")
    print_map()
