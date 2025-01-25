import os
import random

map_lst = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' ,'*', '*'],
           ['*', '₽', ' ', '$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
           ['*', ' ', '₽', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
           ['*', ' ', '@', '₽', ' ', ' ', ' ', ' ', '₽', ' ', ' ', ' ' ,' ', '*'],
           ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
           ['*', '₽', '$', '$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
           ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '$', '$', ' ', ' ' ,' ', '*'],
           ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
           ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
           ['*', ' ', '₽', ' ', ' ', '₽', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', '*'],
           ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '₽', ' ', ' ' ,' ', '*'],
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
    print(f"Собрано золота: {gold_collected}, убито гоблинов: {goblins_killed}, здоровье: {health}")
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
        print("Вы подобрали золото!")
    elif target == '₽':
        # 50% шанс на атаку
        if random.random() < 0.5:  # Используем random.random() для более явного 50% шанса
            health -= 1
            print("Гоблин атакует! Вы теряете 1 здоровье.")
            if health <= 0:
                print("Вы погибли! Игра окончена.")
                exit()
        map_lst[x][y] = ' '
        x, y = new_x, new_y
        map_lst[x][y] = '@'
        goblins_killed += 1
        print("Вы убили гоблина!")
    elif target == '*':
        print("Вы не можете пройти сквозь стену!")

print_map()

while True:
    move_input = input("Введите W/A/S/D для управления (или Q для выхода): ").lower()
    if move_input == 'w':
        move(-1, 0)
    elif move_input == 's':
        move(1, 0)
    elif move_input == 'a':
        move(0, -1)
    elif move_input == 'd':
        move(0, 1)
    elif move_input == 'q':
        print("Выход из игры.")
        break
    else:
        print("Некорректная команда!")
    print_map()