import telebot
import time

# from telebot import types
#  'YOUR_TOKEN'
token = '6282117339:AAGxTAt4n7Twzzbg9lN7eReZUs025ZApTIs'

# Create a new bot instance
bot = telebot.TeleBot(token)

welcome_question = {
  "question":
  "Welcome 😝 Do you want to play a game?",
  "markup":
  telebot.types.InlineKeyboardMarkup().row(
    telebot.types.InlineKeyboardButton('YeS', callback_data='game_yes'),
    telebot.types.InlineKeyboardButton('N0', callback_data='game_no'))
}

markup_third = telebot.types.InlineKeyboardMarkup()
markup_third.row(
  telebot.types.InlineKeyboardButton('A. 2% not important at all',
                                     callback_data='game_wrong'))
markup_third.row(
  telebot.types.InlineKeyboardButton('B. 15% it\'s not that important',
                                     callback_data='game_wrong'))
markup_third.row(
  telebot.types.InlineKeyboardButton('C. 50% it is half as important',
                                     callback_data='game_wrong'))
markup_third.row(
  telebot.types.InlineKeyboardButton(
    'D. 88% it is extremely important to put 🤚 all over the place and 💋 her almost everywhere!',
    callback_data='game_correct'))

questions = [{
  "question":
  "ሄዶ ሄዶ መግቢያው ጭራሮ is this correct (lek new)?",
  "markup":
  telebot.types.InlineKeyboardMarkup().row(
    telebot.types.InlineKeyboardButton('YeS', callback_data='game_correct'),
    telebot.types.InlineKeyboardButton('N0', callback_data='game_wrong')),
  "game-wrong":
  "The correct answer was YES! \U0001F92A stupid! \U0001F418",
}, {
  "question":
  " How many orgazms do you think i had in our time bafew night?",
  "markup":
  telebot.types.InlineKeyboardMarkup().row(
    telebot.types.InlineKeyboardButton('5', callback_data='game_wrong'),
    telebot.types.InlineKeyboardButton('6', callback_data='game_wrong'),
    telebot.types.InlineKeyboardButton('7', callback_data='game_correct'),
    telebot.types.InlineKeyboardButton('0', callback_data='game_wrong')),
  "game-wrong":
  "Yarr it was 7 !"
}, {
  "question":
  "How important do you think your hands ARE during our sessions?",
  "markup":
  markup_third,
  "game-wrong":
  "Yarr it was D. \n You need to put 🤚 your hands all over the place and 💋 her almost everywhere! \n like they do in the movies lol"
}, {
  "question":
  "Do you wanna meet up again ?",
  "markup":
  telebot.types.InlineKeyboardMarkup().row(
    telebot.types.InlineKeyboardButton('🟥', callback_data='game_correct'),
    telebot.types.InlineKeyboardButton('🔵', callback_data='game_correct'),
    telebot.types.InlineKeyboardButton('🟩', callback_data='game_correct')),
  "game-wrong":
  "yup"
}]


def numbers(x):
  exten = ['st', 'nd', 'rd', 'th']
  if (x < 3): return exten[x]
  else: return exten[3]


# Define a dictionary to store user progress
user_progress = {}


# Handle /start command
@bot.message_handler(commands=['start'])
def handle_start(message, chatID=None):
  chat_id = message.chat.id if message is not None else chatID
  print('--- Start Message ---')
  print('chatID:', chat_id)
  user_progress[chat_id] = 0
  bot.send_message(chat_id,
                   welcome_question["question"],
                   reply_markup=welcome_question["markup"])


# Handle incoming updates
@bot.message_handler(func=lambda message: True)
def handle_message(message):
  chat_id = message.chat.id
  first_name = message.from_user.first_name
  last_name = message.from_user.last_name
  text = f"Did u just say - {message.text}? \n Just play the game okey {first_name} {last_name} !"
  bot.send_message(chat_id, text)
  handle_start(message)


# Handle callback queries
@bot.callback_query_handler(func=lambda query: True)
def handle_callback_query(query):
  chat_id = query.message.chat.id
  data = query.data
  bot.answer_callback_query(query.id, text='You selected: ' + query.data)

  if data == 'game_yes':
    bot.send_message(chat_id, 'Yayyyy! Okay, here we go...')
    ask_questions(chat_id)

  elif data == 'game_no':
    bot.send_message(chat_id, 'Oweee... ur a bummer :(')
    time.sleep(4)
    bot.send_message(chat_id, 'R U SURE u dont wanna play?')
    handle_start(query.message)

  elif data == 'game_correct':
    bot.send_message(chat_id,
                     'Bam! ur damn right ✨✨✨✨🎆🎆🎆🎆 \n it is correct beb!')
    ask_questions(chat_id)

  elif data == 'game_wrong':
    correct_wrong(chat_id)
    ask_questions(chat_id)


def ask_questions(chatID):
  index = user_progress[chatID]
  time.sleep(1)
  if index < len(questions):
    question = questions[index]
    bot.send_message(chatID, f"Here's your {index+1}{numbers(index)} question")
    time.sleep(2)
    bot.send_message(chatID,
                     question["question"],
                     reply_markup=question["markup"])
    user_progress[chatID] += 1
  else:
    bot.send_message(
      chatID,
      'FINISHED all the questions. Godd 100%! \n \U0001F449 \U0001F449 Wanna try again ?'
    )
    time.sleep(2)
    handle_start(None, chatID)


def correct_wrong(chatID):
  index = user_progress[chatID] - 1
  print(index, questions[index])
  question = questions[index]
  bot.send_message(chatID, "NOP ! the answer wasn't correct.")
  bot.send_message(chatID, f"{question['game-wrong']}")


print('bot runnig')
# Start the bot
bot.polling()
