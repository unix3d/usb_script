#!/usr/bin/env python3
import os, datetime
users = {'ltp-konik': 'Коник А.Т.', 'pc-shikov': 'Шиков Л.Л.', 'ltp-hvatov': 'Хватов О.В.',
         'ltp-aseev': 'Асеев А.В.', 'pc-lab': 'хим. лаб.', 'pc-stadnikova': 'Стадникова Е.И.',
         'ltp-sein': 'Сеин А.С.', 'ltp-kovalev': 'Ковалев В.В.', 'ltp-anpilov': 'Анпилов В.В.', 'ltp-shulginov':
         'Шульгинов А.В.', 'ltp-efremov': 'Ефремов А.В.', 'ltp-boldyrev': 'Болдырев А.И.',
         'ltp-yurev': 'Юрьев С.Ю.', 'ltp-kokaykin': 'Кокайкин С.В.', 'ltp-abdurakhmanov': 'Абдурахманов Р.А.',
         'ltp-khripkov': 'Хрипков А.В.', 'ltp-marin': 'Марьин М.А.', 'ltp-tsirulnik': 'Цирульник Е.Ю.', 'ltp-korotya':
         'Коротя И.Н.','ltp-filippov': 'Филиппов А.В.', 'ltp-laktionov': 'Лактионов А.А.', 'ltp-andreev':
         'Андреев К.В.', 'ltp-kirillova': 'Кириллова Н.А.', 'ltp-master': 'Мастер ЦЕХ', 'pc-plyuskova': 'Плюскова М.В.',
         'pc-zharikova': 'Жарикова Н.А.', 'ltp-vorobev': 'Воробьев А.А.', 'ltp-shurakov': 'Шураков А.А.',
         'ltp-yaroshenko': 'Ярошенко Д.С.', 'ltp-shostak': 'Шостак Ю.В.', 'ltp-efimov': 'Ефимов Ю.А.',
         'ltp-petrenko': 'Петренко В.В.', 'ltp-kanyavskiy': 'Канявский Г.Я.', 'ltp-novikov': 'Новиков Р.V.',
         'TEXOTDEL': 'ПК-техотдел', 'BELAYAGLINAGLAV': 'ПК-касса'}
Flash = ['Generic', 'JetFlash', 'Transcend', 'Kingston', 'DataTraveler', 'Silicon-Power', 'USB_DISK',
       'USB']
RmDisk = ['SSD', 'ST', 'STORE']
SmartF = ['HUAWEI', 'LG', 'LINUX', 'Nokia', 'MI', 'Samsung']
date = datetime.date.today()
path = os.path.join(r"C:\Users\Andrei\Desktop", 'txt')
filename = os.path.join(r"C:\Users\Andrei\Desktop\123", ('result' + str(date) + '.txt'))
result = open(filename, 'a')
for root, dirs, files in os.walk(path):
    for i in files:
        if (str(i[:(i.find('.'))])) in users.keys():
            result.write(users[str(i[:(i.find('.'))])] + '\n')
        else:
            result.write((str(i[:(i.find('.'))])) + '\n')
        file = open((os.path.join(root, i)), 'r', encoding='utf_8')
        for line in file:
            result.write(line + '\n')
        result.write('---------------------------------------------------------------------------------\n')
