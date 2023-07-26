import smtplib, datetime, os                                    # Импортируем библиотеку по работе с SMTP
import mimetypes          # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
#import ssl
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
    #password = "jndpfxqnibqzlixz"
    password = "G2#7@8hSw3"
    #msg['From'] = "kat01xyx12@gmail.com"
    msg['From'] = "konik.at@smart74.ru"
    msg['To'] = "konik.at@smart74.ru"
    msg['Subject'] = "Отчет по использованиб USB за " + str(month_name(month))
    msg.attach(MIMEText(message, 'plain'))
    name = str('Отчет')
    with open(fname) as f:
        file = MIMEText(f.read(), _subtype=subtype)
    file.add_header('Content-Disposition', 'attachment', filename=name)
    msg.attach(file)
    # msg.attach(MIMEImage(file("C:\Users\Andrei\Desktop\ltp-konik.txt").read()))
    server = smtplib.SMTP_SSL('172.18.110.12: 465')
    #server.starttls()
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
def writting_to_file (report_txt, dir):
    for root, dirs, files in os.walk(dir):
        for name_file in files:
            x = 0
            if os.stat(os.path.join(dir, name_file)).st_size == 0:
                continue
            file = open((os.path.join(root, name_file)), 'r', encoding= 'utf-8')
            for line in file:
                k = 0
                for id in permitted_dev.keys():
                    if str(id) in line:
                        print(id)
                        k = 1
                        break
                if k == 1:
                    continue
                if x == 0:
                    if (str(name_file[:(name_file.find('.'))])) in users.keys():
                        report_txt.write(users[str(name_file[:(name_file.find('.'))])] + '\n')
                    else:
                        report_txt.write((str(name_file[:(name_file.find('.'))])) + '\n')
                    report_txt.write('_' * 20 + '\n' + '\n')
                    x = 1
                for key, val in Device.items():
                   for i in val:
                       if str(i) in line:
                           report_txt.write(' ' + '-' + ' ' + key + (str(line[line.find(':'):])) + '\n')
                           k = 1
                           break
                   else:
                         report_txt.write(' ' + '-' + ' ' + line + '\n')
                         break
                   if k == 1:
                      break
            report_txt.write('-' * 100 + '\n')
    report_txt.close()

#####################################################################
users = {'ltp-konik': 'Коник А.Т.', 'pc-shikov': 'Шиков Л.Л.', 'ltp-hvatov': 'Хватов О.В.',
         'ltp-aseev': 'Асеев А.В.', 'pc-lab': 'хим. лаб.', 'pc-stadnikova': 'Стадникова Е.И.',
         'ltp-sein': 'Сеин А.С.', 'ltp-kovalev': 'Ковалев В.В.', 'ltp-anpilov': 'Анпилов В.В.', 'ltp-shulginov':
         'Шульгинов А.В.', 'ltp-efremov': 'Ефремов А.В.', 'ltp-boldyrev': 'Болдырев А.И.',
         'ltp-yurev': 'Юрьев С.Ю.', 'ltp-kokaykin': 'Кокайкин С.В.', 'ltp-abdurakhmanov': 'Абдурахманов Р.А.',
         'ltp-khripkov': 'Хрипков А.В.', 'ltp-marin': 'Марьин М.А.', 'ltp-tsirulnik': 'Цирульник Е.Ю.', 'ltp-korotya':
         'Коротя И.Н.', 'ltp-filippov': 'Филиппов А.В.', 'PC-LAKTIONOV': 'Лактионов А.А.', 'ltp-andreev':
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

permitted_dev = {'4CEDFB74A3ADB47021599815&0': 'Windows_10_set_up', '4CEDFB74A418E37029C201F2&0': 'USB_Aseev_A.S.',
            '60A44C3FB1A2F3317922024E&0': 'USB_Kirillova_N.A',
            'E0D55EA574F1E3C0D90101DE&0': 'USB_Tsirulnik_E.A.', 'NA03JV71&0': 'RHDD_Shikov_L.L.', 'DA704984&0':
            'USB_Shikov_L.L.', '10080421E6A80D00D5980322&0': 'USB_Butmalay_L.V.',
            '201206SP0048070F26F824330C13&0': 'USB_Andreev_K.V.', '60A44C3FAF75E311491B001B&0': 'USB_Plyuskova_M.V.',
            'C70F803FACFD&0': 'Camera_Agro', '03BSK3GW2WWVJL7T&0': 'USB_Stadnikova_E.I.', '5B70C2D4&0':
            'USB_Kovalev_V.V.', '029INMU6YZVP6J&0': 'USB_Khvatov_O.V.', 'MSFT3021008659211000000001&0':
            'RHDD_Andreev_K.V.', '13803145217900C6&0': 'USB_Konik'}

date = str(datetime.date.today())
month = date[(date.find('-'))+1:(date.rfind('-'))]
path = os.path.join(r"C:\Users\Andrei\Desktop", '123')
filename = os.path.join(r"C:\Users\Andrei\Desktop\txt", ('report' + str(date) + '.txt'))
result = open(filename, 'a')

#_______________________________Main________________________________#
writting_to_file(result, path)
sending_email(filename)

