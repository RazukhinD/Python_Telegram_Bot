from bot_config import dp, bot
from aiogram import types
import random
total = 150

@dp.message_handler(commands=['start'])
async def start_bot(message:types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', игра началась сейчас у нас осталось {total} конфет.'
                                                      f' Если не знаешь правила игры, напиши /rules ')
    print(f'{message.from_user.id}-{message.from_user.username}')
    # await bot.send_message(1894873465, text=f'{message.from_user.username}')

@dp.message_handler(commands=['rules'])
async def write_rules(message:types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.username}'
                                                      f' На столе лежит {total} конфет.'
                                                      f'Ты играешь против компьютера. Первый ход определяется жеребьёвкой.'
                                                      f' За один ход можно забрать не более чем 28 конфет.'
                                                      f' Все конфеты оппонента достаются сделавшему последний ход. Начинаем игру? Если да пиши /start_game')


@dp.message_handler(commands=['start_game'])
async def start_game_bot(message:types.Message):
    total=150
    who_do_turn = random.randint(0, 2)
    if who_do_turn==0:
        await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                          f', игра началась сейчас у нас осталось {total} конфет.'
                                                          f' Ты ходишь первым. Выбирай количество конфет, которые хочешь забрать.')
    else:
        computer_turn=random.randint(1,28)
        total -= computer_turn
        await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                          f', игра началась сейчас у нас осталось {total} конфет.'
                                                          f'  Потому что первый ход за компьютером и он забрал {computer_turn} конфет.'
                                                          f' Теперь твой ход')
@dp.message_handler()
async def game(message:types.Message):
    global total
    if message.text.isdigit():
        if 0<int(message.text)<29:
            total -= int(message.text)
            if total==0:
                await bot.send_message(message.from_user.id, text=f'{message.from_user.username}'
                                                                  f' Ну ничего себе ты красава! Ты победил')
            else:
                await bot.send_message(message.from_user.id, text=f'{message.from_user.username}'
                                                                  f' Ты взял {message.text} конфет, на столе осталось {total} конфет. Ход за компьютером')

        else:
            await bot.send_message(message.from_user.id, text=f'{message.from_user.username}'
                                                              f' ну нормально же общались, играли, зачем такой жадный стал')
    else:
        await bot.send_message(message.from_user.id, text=f'{message.from_user.username}'
                                                          f' ты чего? самый умный? буквами убирать конфеты будешь??')
    if 0<total<28:
        await bot.send_message(message.from_user.id, text=f'{message.from_user.username}'
                                                          f' Ну ты и лох, на столе осталось {total} конфет. И их забрал компьютер! Он победил'
                                                          f' А ты лох')
    else:
        computer_turn = random.randint(1, 28)
        total -= computer_turn
        await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                          f', У нас осталось {total} конфет.'
                                                          f'  компьютер сходил и он забрал {computer_turn} конфет.'
                                                          f' Теперь твой ход')

