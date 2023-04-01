import telebot

# create a new bot with your bot token
bot = telebot.TeleBot("6161593477:AAEWyBCM4xiufEjc74PIxgWggnkOHpyRV4I")

# dictionary to store the names entered by the users
user_names = {}

# function to find the FLAMES combination
def find_flames(name1, name2):
    
    # create two lists with characters of names
    name1_list = list(name1.lower())
    name2_list = list(name2.lower())
    
    # loop through the characters of first name
    for i in name1_list:
    	if i in name2_list:
                name1_list.remove(i)
                name2_list.remove(i)
    print(name1_list, name2_list)
    
    # concatenate the remaining characters of both names
    remaining_chars = name1_list + name2_list
    
    # count the number of remaining characters
    count = len(name1_list)
#    print(count)
    # list to store the meanings of FLAMES letters
    flames_list = ['Friends', 'Lovers', 'Anger', 'Marriage', 'Enemies', 'Siblings']
    
    # loop through the letters of FLAMES
    while len(flames_list) > 1:
            index = count%len(flames_list)
            # remove the item from the list if the count is less than or equal to the index
            if index >= 0:
            	right = flames_list[index+1:]
            	left = flames_list[:index]
            	flames_list = right + left
            else:
            	flames_list = flames_list[:len(flames_list)]
    
    # return the only remaining item in the list
    return flames_list

# function to handle the start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Please enter your name.')

# Author  
@bot.message_handler(commands=['author'])
def send_hello(message):
    bot.send_message(message.chat.id, "Instagram: https://instagram.com/response.200")
    bot.send_message(message.chat.id, "Website: https://lone1177.blogspot.com/")
    bot.send_message(message.chat.id, "Telegram Group: https://t.me/lonemods")
    
# function to handle the text messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # check if the message is a name
    if message.text.isalpha():
        # check if the user has already entered their name
        if message.chat.id not in user_names:
            # add the name to the dictionary
            user_names[message.chat.id] = message.text
            # ask the user to enter the second name
            bot.reply_to(message, 'Please enter the name of the other person.')
        else:
            flames_result = find_flames(user_names[message.chat.id], message.text.replace('_', ''))
            # find the FLAMES combination
            flames_result = find_flames(user_names[message.chat.id], message.text)
            # send the result to the user
            bot.reply_to(message, f'The FLAMES result is: {flames_result}')
            # remove the name from the dictionary
            del user_names[message.chat.id]
    else:
        # ask the user to enter their name
        bot.reply_to(message, 'Enter the name without using underscore and space')

# start the bot
print("STARTED!")
bot.polling(none_stop=True)
