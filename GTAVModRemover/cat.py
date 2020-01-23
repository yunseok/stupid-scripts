# TODOS: UPDATE THIS SCRIPT AND ADD NEW FILES FROM THE NEW UPDATE...

import shutil
import ctypes
import zipfile
import sys
import os

gtaFolderPath = 'C:\\User\\Desktop\\TestGTA'
backUpFolderPath = 'C:\\User\\Desktop\\TestGTA\\_Backup'

gtaFoldersList = [
    gtaFolderPath + 'update',
    gtaFolderPath + 'x64',
]

gtaFilesList = [
    gtaFolderPath + 'bink2w64.dll',
    gtaFolderPath + 'common.rpf',
    gtaFolderPath + 'GTA5.exe',
    gtaFolderPath + 'GTAVLauncher.exe',
    gtaFolderPath + 'version.txt',
    gtaFolderPath + 'x64w.rpf'
]


def clearTerminal():
    os.system('cls')


def checkGtaVersion(gtaVersionFile):
    if os.path.exists(backUpFolderPath):
        f = open('gtaVersionFile', r)
        fileContent = f.read()
        print('GTA V - ' + fileContent)
        f.close()
        return True
    else:
        print('"version.txt" file missing!')
        return False


def confirmPrompt(question):
    valid = {
        "yea": True,
        "yeah": True,
        "yes": True,
        "y": True,
        "ye": True,
        "no": False,
        "nah": False,
        "nope": False,
        "nop": False,
        "na": False,
        "n": False
    }

    if valid is None:
        prompt = " [y/n] "
    elif valid == "yes":
        prompt = " [Y/n] "
    elif valid == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid answer: '%s'" % valid)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if valid is not None and choice == '':
            return valid[valid]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write(
                "Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def moveToBackupFolder(gtaFolderPath, mod, backup):
    if (os.path.exists(backUpFolderPath)) and (os.path.isdir(backUpFolderPath)):
        shutil.move(gtaFolderPath + mod, backup)
        print('Moving "' + mod + '" to the backup folder...')
    else:
        if confirmPrompt('The backup folder doesn\'t seem to exists, would like to create one?') == True:
            shutil.move(gtaFolderPath + mod, backup)
            print('Moving "' + mod + '" to the backup folder...')
        else:
            print('Aborting...')
            return False


def zipBackup(backUpFolderPath):
    shutil.make_archive('backup', 'zip', backUpFolderPath)
    return True


def verifyFiles(gtaFoldersList, gtaFilesList):
    for folder in gtaFoldersList:
        if (os.path.exists(folder)) and (os.path.isdir(folder)):
            print('FOLDERS: OK')
            for file in gtaFilesList:
                if (os.path.exists(file)):
                    print('FILES: OK')
                    return True
                else:
                    print('ERROR! Original files are missing')
                    return False
                    break
        else:
            print('ERROR! Original files are missing')
            return False
            break


while True:
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print('Permission denied! Make sure you are running this application as an administrator.')
        break
    else:
        clearTerminal()
        print('Checking GTA V Installation...')
        checkGtaVersion(gtaFolderPath + 'version.txt')
        if verifyFiles(gtaFoldersList, gtaFilesList) == True:
            print('Moving mods to the backup folder...')

            print('GTA V is online')
            break
        break
