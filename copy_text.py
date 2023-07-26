import smtplib, datetime, os                                    # Импортируем библиотеку по работе с SMTP
import mimetypes                                            # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders                                  # Импортируем энкодер
from email.contentmanager import subtype
from email.mime.base import MIMEBase                        # Общий тип
from email.mime.text import MIMEText                        # Текст/HTML
from email.mime.image import MIMEImage                      # Изображения
from email.mime.audio import MIMEAudio                      # Аудио
from email.mime.multipart import MIMEMultipart
#######################################################################
def sending_email (fname):
    msg = MIMEMultipart()
    message = "Отчет по использованию USB за " + str(month_name(month))
    password = "jndpfxqnibqzlixz"
    msg['From'] = "kat01xyx12@gmail.com"
    msg['To'] = "konik.at@smart74.ru"
    msg['Subject'] = "Отчет по использованиб USB за " + str(month_name(month))
    msg.attach(MIMEText(message, 'plain'))
    name = str('Отчет')
    with open(fname) as f:
        file = MIMEText(f.read(), _subtype=subtype)
    file.add_header('Content-Disposition', 'attachment', filename=name)
    msg.attach(file)
    # msg.attach(MIMEImage(file("C:\Users\Andrei\Desktop\ltp-konik.txt").read()))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    f.close()
    server.quit()
########################################################################
def month_name (number):
    if number == '01':
        return "Январь"
    elif number == '02':
        return "Февраль"
    elif number == '03':
        return "Март"
    elif number == '04':
        return "Апрель"
    elif number == '05':
        return "Май"
    elif number == '06':
        return "Июнь"
    elif number == '07':
        return "Июль"
    elif number == '08':
        return "Август"
    elif number == '09':
        return "Сентябрь"
    elif number == '10':
        return "Октябрь"
    elif number == '11':
        return "Ноябрь"
    elif number == '12':
        return "Декабрь"
#####################################################################
def writting_to_file (txt,dir):
    for root, dirs, files in os.walk(dir):
        for i in files:
            if (str(i[:(i.find('.'))])) in users.keys():
                txt.write(users[str(i[:(i.find('.'))])] + '\n')
            else:
                txt.write((str(i[:(i.find('.'))])) + '\n')
            txt.write('_________________\n')
            file = open((os.path.join(root, i)), 'r', encoding='utf_8')
            for line in file:

                for key, val in Device.items():
                    for i in val:
                        if str(i) in line:
                            txt.write(key + (str(line[line.find(':'):])) + '\n')

                            break

            txt.write('---------------------------------------------------------------------------------\n')
    txt.close()
#####################################################################
users = {'ltp-konik': 'Коник А.Т.', 'pc-shikov': 'Шиков Л.Л.', 'ltp-hvatov': 'Хватов О.В.',
         'ltp-aseev': 'Асеев А.В.', 'pc-lab': 'хим. лаб.', 'pc-stadnikova': 'Стадникова Е.И.',
         'ltp-sein': 'Сеин А.С.', 'ltp-kovalev': 'Ковалев В.В.', 'ltp-anpilov': 'Анпилов В.В.', 'ltp-shulginov':
         'Шульгинов А.В.', 'ltp-efremov': 'Ефремов А.В.', 'ltp-boldyrev': 'Болдырев А.И.',
         'ltp-yurev': 'Юрьев С.Ю.', 'ltp-kokaykin': 'Кокайкин С.В.', 'ltp-abdurakhmanov': 'Абдурахманов Р.А.',
         'ltp-khripkov': 'Хрипков А.В.', 'ltp-marin': 'Марьин М.А.', 'ltp-tsirulnik': 'Цирульник Е.Ю.', 'ltp-korotya':
         'Коротя И.Н.','ltp-filippov': 'Филиппов А.В.', 'PC-LAKTIONOV': 'Лактионов А.А.', 'ltp-andreev':
         'Андреев К.В.', 'ltp-kirillova': 'Кириллова Н.А.', 'ltp-master': 'Мастер ЦЕХ', 'pc-plyuskova': 'Плюскова М.В.',
         'pc-zharikova': 'Жарикова Н.А.', 'ltp-vorobev': 'Воробьев А.А.', 'ltp-shurakov': 'Шураков А.А.',
         'ltp-yaroshenko': 'Ярошенко Д.С.', 'ltp-shostak': 'Шостак Ю.В.', 'ltp-efimov': 'Ефимов Ю.А.',
         'ltp-petrenko': 'Петренко В.В.', 'ltp-kanyavskiy': 'Канявский Г.Я.', 'ltp-novikov': 'Новиков Р.V.',
         'TEXOTDEL': 'ПК-техотдел', 'BELAYAGLINAGLAV': 'ПК-касса'}
Flash = ['Generic', 'JetFlash', 'Transcend', 'Kingston', 'DataTraveler', 'Silicon-Power',
        'Prod_USB_DISK', 'USB_Flash_Disk']
RmDisk = ['SSD', 'ST', 'STORE']
Smartfon = ['LG', 'MI', 'Nokia', 'NOKIA', 'HUAWEI', 'Samsung', 'SAMSUNG', 'HONOR', 'Honor', 'xiaomi',
            'Xiaomi', 'XIAOMI', 'iphone', 'Iphone', 'IPHONE', 'Linux']
Device = dict(Флешка=set(Flash), Сьемный_диск=set(RmDisk), Смартфон=set(Smartfon))
date = str(datetime.date.today())
month = date[(date.find('-'))+1:(date.rfind('-'))]
path = os.path.join(r"C:\Users\Andrei\Desktop", 'txt')
filename = os.path.join(r"C:\Users\Andrei\Desktop\123", ('result' + str(date) + '.txt'))
result = open(filename, 'a')

#_______________________________Main________________________________#
writting_to_file(result, path)
sending_email(filename)

