import csv
import emoji

# https://www.mindk.com/blog/how-to-develop-a-chat-bot/
API_KEY = '5031857976:AAEdpyxe46sxSSEL0TKpc_4jjdXnK2ffMVU'
time_zone = 'Asia/Tel_Aviv'

start_message = emoji.emojize('Hello and welcome to the Israel\'s rent apartment bot \U0001F1EE\U0001F1F1\U0001F1EE\U0001F1F1\U0001F1EE\U0001F1F1  \n' \
                'In this bot you will answer several question related to your' \
                'dream apartment \U0001F4B0 :shower: :evergreen_tree: \n'
                'Then u will get links to rent apartment that match your\n'
                'profile and your preferences :sunrise: :house_with_garden: :sunrise: \n' \
                'Write /help to see the commands that available in this bot \U00002694')


help_message = '1) /city - insert your city that you are interested living in \U0001F46A\n' \
               'If you add any issues contact me in the button bellow \U0001F680'

city_message = 'Choose an area you are interested to living in \U0001F3E0'

room_message = 'Please choose number of rooms \U0001F3E8'


# https://worldpopulationreview.com/countries/cities/israel
num_col = 3
population = 128500
yad2_url_start = 'https://www.yad2.co.il/realestate/rent?'
with open('city_pop.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    city_list = [[row[0], yad2_url_start + row[2]] for row in csv_reader if int(row[1]) > population]
    city_list[0][0] = 'Jerusalem'
    city_list = city_list[: int(len(city_list)/num_col)*num_col]

# city_list = ['Haifa', 'Tel-Aviv', 'Jerusalem', 'Ramat-Gan']
# print(start_message)