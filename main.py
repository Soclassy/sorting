from PyQt6.QtWidgets import QFileDialog, QWidget, QVBoxLayout, QLabel, QMainWindow, QApplication, QPushButton
import sys
from PyQt6.QtCore import QFileInfo
from pathlib import Path
import re
import os
import shutil

class Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practice")
        self.label1 = QLabel()
        self.label1.setText("Файл с названиями папок: ")
        self.label1_1 = QLabel()

        self.label2 = QLabel()
        self.label2.setText("Файл с названиями масок: ")
        self.label2_2 = QLabel()

        self.label3 = QLabel()
        self.label3.setText("Выберите любой файл из папки со всеми файлами типа .time: ")
        self.label3_3 = QLabel()

        self.but_1 = QPushButton("Поиск")
        self.but_1.clicked.connect(self.show_dialog)

        self.but_2 = QPushButton("Поиск")
        self.but_2.clicked.connect(self.show_dialog_2)

        self.but_3 = QPushButton("Поиск")
        self.but_3.clicked.connect(self.show_dialog_3)

        self.but_start = QPushButton("Начать")
        self.but_start.clicked.connect(self.nach)

        layout1 = QVBoxLayout()
        layout1.addWidget(self.label1)
        layout1.addWidget(self.label1_1)
        layout1.addWidget(self.but_1)
        layout1.addWidget(self.label2)
        layout1.addWidget(self.label2_2)
        layout1.addWidget(self.but_2)
        layout1.addWidget(self.label3)
        layout1.addWidget(self.label3_3)
        layout1.addWidget(self.but_3)
        layout1.addWidget(self.but_start)

        container = QWidget()
        container.setLayout(layout1)

        self.setCentralWidget(container)

    def show_dialog(self):
        home_dir = str(Path.home())
        self.fname1 = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        self.label1_1.setText(f"{self.fname1[0]}")
        return self.fname1

    def show_dialog_2(self):
        home_dir = str(Path.home())
        self.fname2 = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        self.label2_2.setText(f"{self.fname2[0]}")
        return self.fname2

    def show_dialog_3(self):
        home_dir = str(Path.home())
        self.fname3 = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        self.fpath = QFileInfo(self.fname3[0]).absolutePath()
        print(type(self.fpath))
        self.label3_3.setText(f"{self.fpath}")
        return self.fpath

    def nach(self):
        # создание папок
        print(self.label1_1.text())
        file = open(f'{self.label1_1.text()}', 'r')  # необходим текстовый файл с названием папок
        f = file.read()
        folder = f.split('\n')  # создаем список из названий папок
        print(folder)
        for i in range(0, 40):
            os.mkdir(folder[i])  # создаем папки на основании списка названий

        # запись масок
        file = open(f'{self.label2_2.text()}', 'r')  # открываем текстовый файл с масками
        f_m = file.read()
        folder_mask = f_m.split('\n')  # разделяем маски в список

        # получаем названия файлов
        file_source = f'{self.label3_3.text()}/'  # указываем путь к имеющимся файлам
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

        main_folder_path_1 = f'{os.getcwd()}'
        main_folder_path_2 = main_folder_path_1.replace("\\", "/")
        main_folder_path = main_folder_path_2 + "/"
        print(main_folder_path)
        # переименование в даты
        for c in range(0, len(folder)):
            name_list = []
            name_list.append(for_folder_dict[c])
            lol = name_list[0]
            for i in range(0, len(for_folder_dict[c])):
                if re.fullmatch(re.compile(f"{'AntifrodDBO'}.*"), lol[i]):
                    if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][34:44]}"):
                        os.remove(f"{main_folder_path}{folder[c]}/{lol[i][34:44]}")
                    os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}",
                              f"{main_folder_path}{folder[c]}/{lol[i][34:44]}")
                elif re.fullmatch(re.compile(f"{'DBO'}.*"), lol[i]):
                    if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][26:36]}"):
                        os.remove(f"{main_folder_path}{folder[c]}/{lol[i][26:36]}")
                    os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}",
                              f"{main_folder_path}{folder[c]}/{lol[i][26:36]}")
                elif re.fullmatch(re.compile(f"{'Plugin'}.*"), lol[i]):
                    if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][29:39]}"):
                        os.remove(f"{main_folder_path}{folder[c]}/{lol[i][29:39]}")
                    os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}",
                              f"{main_folder_path}{folder[c]}/{lol[i][29:39]}")
                elif re.fullmatch(re.compile(f"{'SalesDBO'}.*"), lol[i]):
                    if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][31:41]}"):
                        os.remove(f"{main_folder_path}{folder[c]}/{lol[i][31:41]}")
                    os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}",
                              f"{main_folder_path}{folder[c]}/{lol[i][31:41]}")
                elif re.fullmatch(re.compile(f"{'Siebel'}.*"), lol[i]):
                    if os.path.exists(f"{main_folder_path}{folder[c]}/{lol[i][29:39]}"):
                        os.remove(f"{main_folder_path}{folder[c]}/{lol[i][29:39]}")
                    os.rename(f"{main_folder_path}{folder[c]}/{lol[i]}",
                              f"{main_folder_path}{folder[c]}/{lol[i][29:39]}")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Start()
    window.show()
    app.exec()

