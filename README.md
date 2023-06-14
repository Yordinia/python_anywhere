# python_anywhere
This is a repository containing all on my pythonanywhere apps / telegram bots 

# to get bot
telebotcreator.com

Command --> /start


Codes --> text = """<b>⛔️ Must Join All Our Channel

✅  @testpostchnl

❇️ After Joining, Click On '🟢 Joined'</b>"""

is_invited = User.getData("is_invited")

u = str(u)
already = User.getData('bot_user')
if already != None:
    pass
else:
    User.saveData('balance', 0)
    User.saveData('ref_count', 0)
    User.saveData('withdrawn', 0)
    User.saveData('bot_user', True)
    if Bot.getData('total_users') == None:
        Bot.saveData('total_users', 1)
    else:
        t = int(Bot.getData('total_users'))+1
        Bot.saveData('total_users', t)

# bot.replyText(u, str(Bot.getData('total_users')))

keyboard = ReplyKeyboardMarkup(True)
keyboard.row('🟢 Joined')

refer = message.text.split(" ")

if message.text == "/start":
    if is_invited == None:
        User.saveData('is_invited', True)
    bot.replyText(
        chat_id=u,
        text=text,
        parse_mode="html",
        reply_markup=keyboard
    )
else:
    if str(u) == refer[1]:
        if is_invited == None:
            User.saveData("is_invited", True)
        bot.replyText(
            chat_id=u,
            text=text,
            parse_mode="html",
            reply_markup=keyboard
        )
    else:
        if is_invited == None:
            refer_balance = User.getData("balance", user=refer[1])
            count = User.getData('ref_count', user=refer[1])
            if refer_balance == None:
                bot.replyText(
                    chat_id=u,
                    text="<b>Invalid referral.</b>"
                )
            refer_balance = float(refer_balance)
            refer_balance += 1
            count = int(count)
            count += 1
            bot.replyText(
                chat_id=refer[1],
                text=f"<b>🎁 +1 For new Refer</b>",
                parse_mode="html"
            )
            User.saveData("ref_count", data=count, user=refer[1])
            User.saveData("balance", data=refer_balance, user=refer[1])
            bot.replyText(
                chat_id=u,
                text=f"<b>🎁 You are invited by {refer[1]}</b>",
                parse_mode="html"
            )
        refer_balance = User.getData("balance", user=refer[1])
        User.saveData("is_invited", True)
        bot.replyText(
            chat_id=u,
            text=text,
            parse_mode="html",
            reply_markup=keyboard
        )