# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Player vs player

import random

greeting = 'Welcome to the game "Take all the sweets"!'
messages = 'Your turn'


# def play_game(n, m, players, messages):
#     count = 0
#     while n > 0:
#         print(f'{players[count%2]}, {messages}')
#         move = int(input())
#         if move > n or move > m:
#             print(
#                 f'Too many sweets! Take {m} sweets, there are only {n} sweets on the table')
#             attempt = 3
#             while attempt > 0:
#                 if n >= move <= m:
#                     break
#                 print(f'Try again, you only got {attempt} attempts')
#                 move = int(input())
#                 attempt -= 1
#             else:
#                 return print(f'You have no attempts left. Game over!')
#         n = n - move
#         if n > 0:
#             print(f'{n} sweets left')
#         else:
#             print('All sweets are taken.')
#         count += 1
#     return players[not count % 2]


# print(greeting)

# player1 = input('Player 1, enter your name:\n')
# player2 = input('Player 2, enter your name:\n')
# players = [player1, player2]

# n = int(input('How many sweets do we use to play?\n '))
# m = int(input('What a limit in sweets do we have per turn?\n '))

# winner = play_game(n, m, players, messages)
# if not winner:
#     print('There is no winner in this game')
# else:
#     print(f'Congrats, {winner}! You have won!')


# player vs ai


def introduce_players():
    player1 = input('Welcome, player. Enter your name, please:\n')
    player2 = 'Sweetlover'
    return [player1, player2]


def get_rules(players):
    n = int(input('How many sweets do we use to play?\n '))
    m = int(input('What a limit in sweets do we have per turn?\n '))
    first = int(input(
        f'{players[0]}, enter number 1 if you want to play first turn, otherwise, enter any other number\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % rules[1] + 1
            print(f'Sweetlover takes {move}')
        else:
            print(f'{players[0]}, {(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Too many sweets! You can take less then {rules[1]} sweets, there are only {rules[0]} sweets on the table')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Try again, you only got {attempt} attempts')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'You have no attempts left. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'{rules[0]} sweets left')
        else:
            print('All sweets are taken')
        count += 1
    return players[count % 2]


print(greeting)

players = introduce_players()
rules = get_rules(players)

winner = play_game(rules, players, messages)
if not winner:
    print('There is no winner in this game.')
else:
    print(
        f'Congrats, {winner}! You have won!')
