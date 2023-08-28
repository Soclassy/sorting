import os
import shutil
import re
from main import Start


class Pred(Start.show_dialog, Start.show_dialog_2, Start.show_dialog_3):
    # создание папок
    file = open(f'{Start.show_dialog}', 'r')  # необходим текстовый файл с названием папок
    f = file.read()
    folder = f.split('\n')  # создаем список из названий папок
    for i in range(0, 40):
        os.mkdir(folder[i])  # создаем папки на основании списка названий

    # запись масок
    file = open(f'{Start.show_dialog_2()}', 'r')  # открываем текстовый файл с масками
    f_m = file.read()
    folder_mask = f_m.split('\n')  # разделяем маски в список

    # получаем названия файлов
    file_source = f'{Start.show_dialog_3}'  # указываем путь к имеющимся файлам
    get_files = os.listdir(file_source)  # получаем наименования файлов в списке

    for_folder_dict = {}  # создаю словарь, в который запишем нужные наименования файлов по папкам
    for i in range(0, 40):
        for_folder_dict[i] = None  # заполняю ключи в словаре

    # распределение названий файлов по ключам в словаре
    for i in range(0, 40):  # количество строк из текстового файла
        test_list = []  # вспомогательный список
        f = folder_mask[i].split("*")  # получаю список из двух слов маски, которые нужно подставлять в проверку
        pattern = re.compile(f"{f[0]}.*{f[1]}.*")  # создаю условие проверки
        for g in range(0, len(get_files)):  # количество файлов
            if re.fullmatch(pattern, get_files[g]) is not None:  # проверяю, есть ли два слова маски в целой строке наименования файлов
                test_list.append(get_files[g])  # записываю наименования во вспомогательный список, если название файла соответствует маске
        for_folder_dict[i] = test_list  # готовый список закидываю в словарь под каждый ключ

    # выведение словаря в текстовый файл для перепроверки
    '''file = open('test.txt', 'w')
    for key, value in for_folder_dict.items():
      file.write(f'{key}, {value}\n\n\n')
    file.close()'''

    # перемещение файлов по создавшимся папкам
    for i in range(0, 40):
        for g in for_folder_dict[i]:
            shutil.move(file_source + g, folder[i])

    main_folder_path = "C:/Users/cnxxd/PycharmProjects/practice/"
    # переименование в даты
    for c in range(0, len(folder)):
        name_list = []
        name_list.append(for_folder_dict[c])
        lol = name_list[0]
        for i in range(0, len(for_folder_dict[c])):
            if re.fullmatch(re.compile(f"{'AntifrodDBO'}.*"), lol[i]):
                if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][34:44]}"):
                    os.remove(f"{main_folder_path}{folder[c]}/{lol[i][34:44]}")
                os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}", f"{main_folder_path}{folder[c]}/{lol[i][34:44]}")
            elif re.fullmatch(re.compile(f"{'DBO'}.*"), lol[i]):
                if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][26:36]}"):
                    os.remove(f"{main_folder_path}{folder[c]}/{lol[i][26:36]}")
                os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}", f"{main_folder_path}{folder[c]}/{lol[i][26:36]}")
            elif re.fullmatch(re.compile(f"{'Plugin'}.*"), lol[i]):
                if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][29:39]}"):
                    os.remove(f"{main_folder_path}{folder[c]}/{lol[i][29:39]}")
                os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}", f"{main_folder_path}{folder[c]}/{lol[i][29:39]}")
            elif re.fullmatch(re.compile(f"{'SalesDBO'}.*"), lol[i]):
                if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][31:41]}"):
                    os.remove(f"{main_folder_path}{folder[c]}/{lol[i][31:41]}")
                os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}", f"{main_folder_path}{folder[c]}/{lol[i][31:41]}")
            elif re.fullmatch(re.compile(f"{'Siebel'}.*"), lol[i]):
                if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][29:39]}"):
                    os.remove(f"{main_folder_path}{folder[c]}/{lol[i][29:39]}")
                os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}", f"{main_folder_path}{folder[c]}/{lol[i][29:39]}")
