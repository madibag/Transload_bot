from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from transload import trans


from telegram import ParseMode

def start(update,context):
    name = update.message.chat.first_name
    chat_id = update.message.chat.id

    welcome_board = [[InlineKeyboardButton(text="Project Channel",url="https://t.me/Python_For_ET"),InlineKeyboardButton(text="Source Code",url="https://github.com/madibag/Transload_bot")],
    [InlineKeyboardButton(text="close",callback_data="close"),InlineKeyboardButton(text="Help",callback_data="help")]]

    context.bot.send_message(chat_id = chat_id,
                            text = f'HI {name} This is File Transloader\nType /help To get more Info.\nMade in 🇪🇹',
                                      parse_mode=ParseMode.HTML,reply_markup=InlineKeyboardMarkup(welcome_board))
def help(u,c):
    help_bord = [
        [
            InlineKeyboardButton(text="Project Channel",url="https://t.me/Python_For_ET"),
            InlineKeyboardButton(text="Source Code",url="https://github.com/madibag/Transload_bot")
        ],
        [
            InlineKeyboardButton(text="close",callback_data="close")
        ]
    ]

    chat_id = u.callback_query.message.chat.id


    #print(u)
    c.bot.send_message(chat_id = chat_id,text = "Just send the Url you want To be transloaded",reply_markup=InlineKeyboardMarkup(help_bord))

def dl(update, context):
    """Echo the user message."""
    c_id = update.message.chat.id

    url = update.message.text
    if url.startswith('http'):
        The_link =  trans(url)

    if The_link == "THE_ERROR":
        context.bot.send_message(chat_id=c_id,
            text ="An Error occured")
        return
    context.bot.send_message(chat_id=c_id,
            text =The_link )

def close(u,c):
    chat_id = u.callback_query.message.chat.id
    message_id = u.callback_query.message.message_id

    c.bot.delete_message(chat_id,message_id)



