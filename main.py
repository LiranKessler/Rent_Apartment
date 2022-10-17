import telebot
from datetime import datetime
import pytz
import message_dict as md

print('This bot is running...')
print('Hello world')

bot = telebot.TeleBot(md.API_KEY, parse_mode=None)
date_in_telaviv = datetime.now(tz=pytz.timezone(md.time_zone))
date_in_telaviv = date_in_telaviv.strftime("%m/%d/%Y, %H:%M:%S")

def main():

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, md.start_message)

    @bot.message_handler(commands=['help'])
    def help_command(message):
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton('Message the developer', url = 'telegram.me/lirankessler'))
        bot.send_message(message.chat.id, md.help_message, reply_markup=keyboard)

    @bot.message_handler(commands=['city'])
    def exchange_command(message):
        keyboard = telebot.types.InlineKeyboardMarkup()

        city = md.city_list
        for i in range(0, len(city), md.num_col):
            lst_help = [str('City_of_' + '_'.join(city[i][0].split())), str('City_of_' + '_'.join(city[i+1][0].split())),
                        str('City_of_' + '_'.join(city[i+2][0].split()))]

            keyboard.row(telebot.types.InlineKeyboardButton(city[i][0], callback_data=lst_help[0]),
                         telebot.types.InlineKeyboardButton(city[i+1][0], callback_data=lst_help[1]),
                         telebot.types.InlineKeyboardButton(city[i+2][0], callback_data=lst_help[2]))
                         # telebot.types.InlineKeyboardButton(city[i+3], callback_data=city[i+3]),
                         # telebot.types.InlineKeyboardButton(city[i+4], callback_data=city[i+4]))

        bot.send_message(message.chat.id, md.city_message, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('City_of_'))
    def callback_query_city(call):
        url_print = [lst[1] for lst in md.city_list if ' '.join(call.data[8:].split('_')) == lst[0]]
        print(url_print)
        user_data = [date_in_telaviv, call.from_user.id, call.from_user.first_name,
                     call.from_user.last_name, call.from_user.username, call.data]
        write_to_f(user_data)
        keyboard = building_keyboard(url_print[0])
        bot.send_message(call.message.chat.id, md.city_message, reply_markup=keyboard)
        # bot.send_message(call.message.chat.id, url_print)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('https:'))
    def callback_query_room(call):
        user_data = [date_in_telaviv, call.from_user.id, call.from_user.first_name,
                     call.from_user.last_name, call.from_user.username, 'Num_of_' + call.data[49:]]
        write_to_f(user_data)
        bot.send_message(call.message.chat.id, call.data)

    def building_keyboard(url_print):
        keyboard = telebot.types.InlineKeyboardMarkup()
        num_room = ['1-2.5', '2.5-3.5', '3.5-4.5', '4.5-more', 'Doesn\'t matter']
        for i in range(len(num_room)):
            temp = url_print
            if len(num_room[i].split('-')) < 2:
                pass
            elif (len(num_room[i].split('-')) == 2) & ('more' in num_room[i].split('-')):
                temp = temp + '&rooms=4.5-12'
            else:
                temp = temp + '&rooms=' + str(num_room[i])
            keyboard.row(telebot.types.InlineKeyboardButton(num_room[i], callback_data=temp))
        return keyboard

    def write_to_f(user_data):
        with open('data_from_bot_users.txt', 'a') as f:
            for element in user_data:
                f.write(str(element) + ' ')
            f.write('\n')

    bot.infinity_polling()

main()