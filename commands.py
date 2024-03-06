from globals import file_path,sheet_name,bot



def read_write(m_text, orders_df):
    from globals import message_g
    column = m_text[0]
    row = m_text[1]

    if len(m_text) == 2:
        status = orders_df.loc[orders_df[orders_df.columns[0]] == row, column].values
    else:
        input_info = m_text[2]
        if(not input_info.isdigit()):
            raise Exception("can be only number")

        status = orders_df.loc[orders_df[orders_df.columns[0]] == row, column] = input_info
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
    a = orders_df.loc[orders_df[orders_df.columns[0]] == row, column]
    b = orders_df.loc[orders_df[orders_df.columns[0]] == row2, column]
    
    if (not row in getattr(orders_df, orders_df.columns[0]).values or not row2 in getattr(orders_df, orders_df.columns[0]).values ):
        raise Exception(f"room not exist")
    if(a.values[0] == '0'):
       raise Exception(f"haven't {column} in the room")
    
   
    
    if(b.values[0] == "0"):
        orders_df.loc[orders_df[orders_df.columns[0]] == row2, column] = a.values[0]
    else:
        c = f", {a.values[0]}"
        orders_df.loc[orders_df[orders_df.columns[0]] == row2, column] = str(b.values[0])
        orders_df.loc[orders_df[orders_df.columns[0]] == row2, column] += c
    orders_df.loc[orders_df[orders_df.columns[0]] == row, column] = "0"

    orders_df.to_excel(file_path, sheet_name=sheet_name, index=False, engine="openpyxl")    

    see_full_table(orders_df)
    #bot.send_message(message_g.chat.id, f"fine")

def see_column(text, orders_df, min_number = 0):
    from globals import message_g
    column = text[1]
    output = ''

    #if(len(text) == 3): min_number = int(text[2])
    a = orders_df.loc[orders_df[column] != "0", [column, orders_df.columns[0]]]
    
    for i in range(0, a.shape[0]):
        output += str(a.room.values[i])
        output += ' ' * (4 - len(str(a.room.values[i])) + 3)
        output += str(getattr(a, column).values[i]) + '\n'

    bot.send_message(message_g.chat.id, F"`Room   {column} \n{output}`", parse_mode='MarkdownV2')
    

def see_full_table(orders_df):
    from globals import message_g
    output = ''
    for i in orders_df.columns:
        output += i + "   "
    output += '\n'
    for i in range(0, orders_df.shape[0]):

        for j in orders_df.columns:
            output += str(getattr(orders_df, j).values[i])
            spaces = len(str(j)) - len(str(getattr(orders_df, j).values[i])) + 3
            output += ' ' * spaces
        output += '\n'
    output += ''
    
    print(output)
    bot.send_message(message_g.chat.id, F"Full table:\n`{output}`", parse_mode='MarkdownV2')
