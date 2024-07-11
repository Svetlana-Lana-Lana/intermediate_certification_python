from datetime import datetime

def id_data():
    id = input("Введите номер заметки: ")
    return id

def title_data():
    title = input("Введите заголовок заметки: ")
    return title

def text_data():
    text = input("Введите текст заметки: ")
    return text

def date_data():
    date  = datetime.now()
    formatted_date = f"{date.day:02d}-{date.month:02d}-{date.year} {date.hour}:{date.minute}:{date.second}"
    # date = input("Введите дату написания заметки: ")
    return formatted_date