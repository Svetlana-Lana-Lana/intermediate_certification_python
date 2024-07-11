from data_create import id_data, title_data, text_data, date_data



def input_data():

    id = id_data()
    title = title_data()
    text = text_data()
    date = date_data()
    with open('data_notes.csv', 'a', encoding='utf-8') as f:
        f.write(f"{id}\n{title}\n{text}\n{date}\n\n")


def print_data():

    var = int(input(f"Доступно 3 способа вывода заметок: \n \n"
    f"1 Вариант: вывод всех заметок в порядке добавления. \n"
    f"2 Вариант: поиск заметки по номеру. \n"
    f"3 Вариант: вывод всех заметок с сортировкой по дате. \n"
    f"Выберите вариант: "))
    while var != 1 and var != 2 and var != 3:
        print("Неправильный ввод")
        var = int(input("Введите число "))

    if var == 1:
        print('Вывод всех заметок: \n')
        with open('data_notes.csv', 'r', encoding='utf-8') as f:
            data_notes = f.readlines()
            data_notes_list = []
            j = 0
            for i in range(len(data_notes)):
                if data_notes[i] == '\n' or i == len(data_notes)-1:
                    data_notes_list.append(''.join(data_notes[j:i+1]))
                    j = i
            print(''.join(data_notes_list))
    if var == 2:
        num = int(input("Введите номер заметки, которую хотите увидеть: "))
        with open('data_notes.csv', 'r', encoding='utf-8') as f:
            data_notes = f.readlines()
            data_notes_list = []
            count = 1             
            for i in range(len(data_notes)):
                if data_notes[i] == '\n' or i == len(data_notes)-1:
                    if count == num:
                        data_notes_list.append(''.join(data_notes[i-4:i]))
                    count += 1
            print(''.join(data_notes_list))
            if num > len(data_notes_list):
                print('Записи с таким номером не существует, повторите попытку')
    if var == 3:
        print('Вывод всех заметок с сортировкой по дате: \n')
        with open('data_notes.csv', 'r', encoding='utf-8') as f:
            data_notes = f.readlines()
            data_notes_list = [line.rstrip() for line in data_notes]
            data_notes_list = [i for i in data_notes_list if i]
            data_notes_dict = {}  
            for i in range(3, len(data_notes_list), 4):
                data_notes_dict[data_notes_list[i]] = data_notes_list[i-3:i]    
            sorted_notes = dict(sorted(data_notes_dict.items()))
            pairs = list(sorted_notes.items())
            print('\n'.join(str(value) for value in pairs))
            


def change_data():

    num = int(input("Введите номер заметки, которую хотите изменить: ")) 
    print("Далее внесите изменения в поля выбранной заметки")
    with open('data_notes.csv', 'r', encoding='utf-8') as f:
        data_notes = f.readlines()
        data_notes_new_list = []
        count = 1
        j = 0               
        for i in range(len(data_notes)):
            if data_notes[i] == '\n' or i == len(data_notes)-1:
                if count != num:
                    data_notes_new_list.append(''.join(data_notes[j:i+1]))
                else:
                    temp = []
                    temp.append(id_data())
                    temp.append(title_data())
                    temp.append(text_data())
                    temp.append(date_data())
                    data_notes_new_list.append('\n'.join(temp))
                j = i
                count += 1
        if num > len(data_notes_new_list):
            print('Записи с таким номером не существует, повторите попытку')
        else:
            with open('data_notes.csv', 'w', encoding='utf-8') as f:
                f.write('')
            for i in range(len(data_notes_new_list)):
                with open('data_notes.csv', 'a', encoding='utf-8') as f:
                    new_list = data_notes_new_list[i].split('\n')
                    for k in range(len(new_list)):
                        if new_list[k] != '':
                            f.write(f"{new_list[k]}\n")
                    f.write('\n')


def delete_data():

    num = int(input("Введите порядковый номер записи, которую хотите удалить "))
    with open('data_notes.csv', 'r', encoding='utf-8') as f:
        data_notes = f.readlines()
        data_notes_new_list = []
        count = 1
        j = 0
        for i in range(len(data_notes)):
            if data_notes[i] == '\n' or i == len(data_notes)-1:
                if count != num:
                    data_notes_new_list.append(''.join(data_notes[j:i+1]))
                j = i
                count += 1
        if num > len(data_notes_new_list)+1:
           print('Записи с таким номером не существует, повторите попытку')
        else:
            with open('data_notes.csv', 'w', encoding='utf-8') as f:
                f.write('')
            for i in range(len(data_notes_new_list)):
                with open('data_notes.csv', 'a', encoding='utf-8') as f:
                    new_list = data_notes_new_list[i].split('\n')
                    for k in range(len(new_list)):
                        if new_list[k] != '':
                            f.write(f"{new_list[k]}\n")
                    f.write('\n')
            print("Запись удалена")

    
