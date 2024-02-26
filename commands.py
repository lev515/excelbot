from globals import file_path,sheet_name,bot



def read_write(m_text, orders_df):
    from globals import message_g
    column = m_text[0]
    row = m_text[1]

    if len(m_text) == 2:
        status = orders_df.loc[orders_df['room'] == row, column].values
    else:
        input_info = m_text[2]
        if(not input_info.isdigit()):
            raise Exception("can be only number")

        status = orders_df.loc[orders_df['room'] == row, column] = input_info
        orders_df.to_excel(file_path, sheet_name=sheet_name, index=False, engine="openpyxl")
            
    if len(status) > 0:
        bot.send_message(message_g.chat.id, f"Now {column}{row}: {status[0]}")
    else:
        bot.send_message(message_g.chat.id, f"cant find {column}{row} cell")

def moved(m_text, orders_df):
    from globals import message_g
    column = m_text[1]
    row = m_text[2]
    row2 = m_text[3]

  #  if(orders_df.loc[row, column].values == 0):
   #     raise Exception(f"haven't {column} in the room")
    orders_df.loc[orders_df['room'] == row, column] -=1
    orders_df.loc[orders_df['room'] == row2, column] += 1
    status = orders_df.loc[orders_df['room'] == row2, column]
    orders_df.to_excel(file_path, sheet_name=sheet_name, index=False)

    if len(status) > 0:
        bot.send_message(message_g.chat.id, f"fine")
    else:
        bot.send_message(message_g.chat.id, f"Заказ с номером {row} не найден.")

def see_column(text, orders_df):
    from globals import message_g
    column = text[1]
    output = ''
    a = orders_df.loc[orders_df[column] > 0, [column, 'room']]
    for i in range(0, a.room.values.size):
        output += str(a.room.values[i]) + '  ' + str(getattr(a, column).values[i]) + '\n'

    bot.send_message(message_g.chat.id, F"Room   {column} \n{output}")
 

