import pandas as pd
from commands import moved,see_column, see_full_table
import globals, utils
from globals import bot, sheet_name, file_path

def load_orders():
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df['room'] = df['room'].astype(str)
    return df


def input_handler():

    orders_df = load_orders()
    m_text = utils.msg_to_standart()

    if(len(m_text) <= 1):
        raise Exception("to low amount of agruments")
    
    if('room' in m_text[1]):
        raise Exception("first column can't be changet")
    
    #if(m_text[1] not in orders_df.columns and m_text[0] not in orders_df.columns):
    #    raise Exception("can't find column")
    
    if(m_text[0] == "moved" or m_text[0] == "move"):
        moved(m_text, orders_df)
    elif(m_text[0] == "see"):
        see_column(m_text, orders_df)


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):

    bot.send_message(message.chat.id, "\"see\", items substring: to see the items\n\n\"moved\", item name, value, (extra info = Nan): to set value\n\n /info to see FULL table")

@bot.message_handler(commands=['info'])
def handle_info(message):
    globals.message_g = message
    see_full_table(load_orders())

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(1285348392, "started")
    globals.message_g = message
    try:
        input_handler()      
    except Exception as e:    
        f = open('logs.txt', 'a')
        f.write(str(e)+ '\n')
        f.close
        if(message.chat.type == 'private'):
            bot.send_message(message.chat.id, text=f"E:{str(e)}")

bot.polling()
