from globals import file_path,sheet_name,bot

def moved(m_text, orders_df):
    from globals import message_g
    row = m_text[1]
    input_info = m_text[2]
    if (len(m_text) == 4):
        extra_info = m_text[3]
        orders_df.loc[orders_df[orders_df.columns[0]].str.lower() == row, orders_df.columns[2]] = extra_info

    a = orders_df.loc[orders_df[orders_df.columns[0]].str.lower() == row, orders_df.columns[1]]= input_info

    orders_df.to_excel(file_path, sheet_name=sheet_name, index=False, engine="openpyxl")
    see_full_table(orders_df)
    bot.send_message(message_g.chat.id, f"Now {row} in {a}")

def see_column(text, orders_df):
    from globals import message_g
    item_name = text[1]
    output = '' 
    a = orders_df.loc[orders_df[orders_df.columns[0]].str.lower().str.contains(item_name)]
    for i in a.columns:
        output += i + "    "
    output += '\n'
    for i in range(0, a.shape[0]):

        for j in a.columns:
            output += str(getattr(a, j).values[i])
            spaces = len(str(j)) - len(str(getattr(a, j).values[i])) + 4
            output += ' ' * spaces
        output += '\n'
    output += ''
    bot.send_message(message_g.chat.id, F"`{output}`", parse_mode='MarkdownV2')
    

def see_full_table(orders_df):
    from globals import message_g
    output = ''
    for i in orders_df.columns:
        output += i + "    "
    output += '\n'
    for i in range(0, orders_df.shape[0]):

        for j in orders_df.columns:
            output += str(getattr(orders_df, j).values[i])
            spaces = len(str(j)) - len(str(getattr(orders_df, j).values[i])) + 4
            output += ' ' * spaces
        output += '\n'
    output += ''
    
    print(output)
    bot.send_message(message_g.chat.id, F"Full table:\n`{output}`", parse_mode='MarkdownV2')
