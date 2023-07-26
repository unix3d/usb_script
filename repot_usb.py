import winreg, os, socket, datetime
from smb.SMBConnection import SMBConnection
#########################################################################
def searching_in_regedit(fKey,subKey):
    try:
        for index in range(10000):
            name_dev.append(os.path.join(r"SYSTEM\CurrentControlSet\Enum\USBSTOR", str(winreg.EnumKey(subKey, index))))
    except WindowsError:
        pass
    for i in name_dev:
        id = winreg.EnumKey((winreg.OpenKey(fKey, i, 0, winreg.KEY_ALL_ACCESS)), 0)
        if id not in permitted_dev.keys():
            usb[i[i.find('_') + 1::]] = id
        #if id in permitted_dev.keys():
            #usb[i[i.find('_') + 1::]] = permitted_dev[id]
    return(usb)
#########################################################################
def sending_smb( name):
    userID = 'usb'
    password = '45920de1f6'
    client_machine_name = socket.gethostname()
    server_name = 'SmbSrv'
    conn = SMBConnection(userID, password, client_machine_name, server_name, use_ntlm_v2=True)
    fullName = str(name + '.txt')
    file = open((fileName), "rb")
    try:
        assert conn.connect('172.21.10.158', 139)
        conn.storeFile('usb_control', fullName, file, timeout=30)
    except:
        fileLog = os.path.join(r"C:\Users\All Users", (user + '_' + '_log.txt'))
        Log = open((fileLog), "a")
        Log.write("\nSENDING ERROR" + " --- " + str(date) + "\n")
        writing_to_file(searching_in_regedit(aReg, aKey), Log)
        Log.write("----------------------------------------------------------------\n")
        Log.close()
    conn.close()
    file.close()
def writing_to_file(list, file):
    for device in list:
        file.write("device:" + device + " ---- " + "id:" + usb[device] + "\n")
###########################################################################
name_dev = []
usb = {}
permitted_dev = {'4CEDFB74A418E37029C201F2&0': 'USB_Aseev_A.S.', '60A44C3FB1A2F3317922024E&0': 'USB_Kirillova_N.A',
            'E0D55EA574F1E3C0D90101DE&0': 'USB_Tsirulnik_E.A.', 'NA03JV71&0': 'RHDD_Shikov_L.L.', 'DA704984&0':
            'USB_Shikov_L.L.', '10080421E6A80D00D5980322&0': 'USB_Butmalay_L.V.',
            '201206SP0048070F26F824330C13&0': 'USB_Andreev_K.V.', '60A44C3FAF75E311491B001B&0': 'USB_Plyuskova_M.V.',
            'C70F803FACFD&0': 'Camera_Agro', '03BSK3GW2WWVJL7T&0': 'USB_Stadnikova_E.I.', '5B70C2D4&0':
            'USB_Kovalev_V.V.', '029INMU6YZVP6J&0': 'USB_Khvatov_O.V.','MSFT3021008659211000000001&0':
            'RHDD_Andreev_K.V.', '13803145217900C6&0': 'USB_Konik'}
date = datetime.date.today()
aReg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
aKey = winreg.OpenKey(aReg, r"SYSTEM\CurrentControlSet\Enum\USBSTOR", 0, winreg.KEY_ALL_ACCESS)
user = socket.gethostname()
fileName = os.path.join(r"C:\Users\All Users", (user + '.txt'))
repot = open((fileName), "w+")

#_________________________________Main______________________________________#
writing_to_file(searching_in_regedit(aReg, aKey), repot)
repot.close()
sending_smb(user)
winreg.CloseKey(aKey)
