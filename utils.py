import globals

def msg_to_standart(_message = globals.message_g):
    text = globals.message_g.text.replace(' ', '')
    text = text.lower()
    text = text.replace('.', ',')
    text = text.split(",")
    return text

