############################
# Name: ASCII Odyssey
# Author: Eloen Dune
# Studio: 5Handsnakes Studio
# Version: 0.1.2
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

# Константы
EMPTY = ' '
WALL = '*'
GOLD = '$'
GOBLIN = '&'
PLAYER = '@'

# Функция для создания нового подземелья
def generate_dungeon():
    dungeon_one = [
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', '*', '*', '*', '*', ' ', ' ', '*', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
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

    # Список всех подземелий
    dungeons = [dungeon_one, dungeon_two, dungeon_three]
    return random.choice(dungeons)

# Игрок
player_x = 1
player_y = 1

# Счетчик монстров
monster_count = 0

# Функция для случайной генерации золота и гоблинов на карте
def place_items(dungeon, item, count):
    """Распределяем элементы (золото или гоблинов) случайным образом по карте."""
    global monster_count
    map_height = len(dungeon)
    map_width = len(dungeon[0])
    
    for _ in range(count):
        while True:
            # Генерируем случайные координаты, избегая стен
            y = random.randint(1, map_height - 2)
            x = random.randint(1, map_width - 2)

            # Проверка, чтобы координаты не выходили за пределы карты
            if 0 <= y < map_height and 0 <= x < map_width and dungeon[y][x] == ' ':
                dungeon[y][x] = item
                if item == GOBLIN:
                    monster_count += 1  # Увеличиваем счетчик монстров
                break

# Генерация карты
def generate_game():
    global dungeon, player_x, player_y, monster_count, MAP_HEIGHT, MAP_WIDTH
    dungeon = generate_dungeon()
    MAP_HEIGHT, MAP_WIDTH = len(dungeon), len(dungeon[0])  # Обновляем размеры карты
    player_x, player_y = 1, 1
    monster_count = 0  # Обнуляем счетчик монстров
    place_items(dungeon, GOLD, 3)  # Добавляем 3 золота
    place_items(dungeon, GOBLIN, 3)  # Добавляем 3 гоблинов

# Размеры подземелья
def get_map_dimensions(dungeon):
    """Получаем размеры карты."""
    return len(dungeon), len(dungeon[0])

MAP_HEIGHT, MAP_WIDTH = get_map_dimensions(generate_dungeon())

def print_dungeon(dungeon):
    """Вывод подземелья на экран."""
    for y, row in enumerate(dungeon):
        for x, cell in enumerate(row):
            if x == player_x and y == player_y:
                print(Fore.BLUE + PLAYER + Style.RESET_ALL, end='')  # Игрок
            elif cell == GOLD:
                print(Fore.YELLOW + cell + Style.RESET_ALL, end='')  # Золото
            elif cell == GOBLIN:
                print(Fore.RED + cell + Style.RESET_ALL, end='')  # Гоблин
            else:
                print(cell, end='')  # Пустое пространство или стена
        print()

def move_player(dx, dy, dungeon):
    """Перемещение игрока."""
    global player_x, player_y, monster_count
    new_x = player_x + dx
    new_y = player_y + dy

    # Убедимся, что новые координаты в пределах карты
    if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
        if dungeon[new_y][new_x] != WALL:
            player_x, player_y = new_x, new_y
            if dungeon[new_y][new_x] == GOLD:
                print(Fore.YELLOW + "Вы собрали золото!" + Style.RESET_ALL)
                dungeon[new_y][new_x] = EMPTY
            elif dungeon[new_y][new_x] == GOBLIN:
                print(Fore.RED + "Вы встретили гоблина!" + Style.RESET_ALL)
                dungeon[new_y][new_x] = EMPTY
                monster_count -= 1  # Уменьшаем количество монстров

def clear_screen():
    """Очистка экрана для Windows и UNIX-систем."""
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/macOS

def main():
    global dungeon  # Убедимся, что dungeon доступна
    generate_game()  # Инициализируем игру с новым подземельем

    while True:
        clear_screen()  # Очищаем экран
        print_dungeon(dungeon)
        print("\nИспользуйте W/A/S/D для перемещения.")
        print("Нажмите 'r' для рестарта.")
        if monster_count == 0:  # Если монстров больше нет
            print("Вы убили всех монстров! Переход на новый уровень...")
            dungeon = generate_dungeon()  # Переход на новый уровень (новую карту)
            MAP_HEIGHT, MAP_WIDTH = len(dungeon), len(dungeon[0])  # Обновляем размеры карты
            place_items(dungeon, GOLD, 3)  # Добавляем золото
            place_items(dungeon, GOBLIN, 3)  # Добавляем новых монстров

        move = input("Ваш ход: ").lower()
        if move == 'w':
            move_player(0, -1, dungeon)
        elif move == 'a':
            move_player(-1, 0, dungeon)
        elif move == 's':
            move_player(0, 1, dungeon)
        elif move == 'd':
            move_player(1, 0, dungeon)
        elif move == 'r':
            print("Игра перезапущена!")
            generate_game()  # Перезапуск игры
        elif move == 'q':
            print("Вы вышли из игры.")
            break

if __name__ == '__main__':
    main()
