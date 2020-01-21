import shutil
import ctypes
import os

gtaFolder = 'C:\\Program Files\\Rockstar Games\\Grand Theft Auto V\\'
backUpFolder = 'C:\\Program Files\\Rockstar Games\\Grand Theft Auto V\\__BACKUP'

foldersList = [
	gtaFolder + 'ReadMe',
	gtaFolder + 'update',
	gtaFolder + 'x64'
]

filesList = [
	gtaFolder + 'bink2w64.dll',
	gtaFolder + 'common.rpf',
	gtaFolder + 'd3dcompiler_46.dll',
	gtaFolder + 'd3dcsx_46.dll',
	gtaFolder + 'GFSDK_ShadowLib.win64.dll',
	gtaFolder + 'GFSDK_TXAA.win64.dll',
	gtaFolder + 'GFSDK_TXAA_AlphaResolve.win64.dll',
	gtaFolder + 'GPUPerfAPIDX11-x64.dll',
	gtaFolder + 'GTA5.exe',
	gtaFolder + 'GTAVLanguageSelect.exe',
	gtaFolder + 'GTAVLauncher.exe',
	gtaFolder + 'NvPmApi.Core.win64.dll',
	gtaFolder + 'PlayGTAV.exe',
	gtaFolder + 'version.txt',
	gtaFolder + 'x64a.rpf',
	gtaFolder + 'x64b.rpf',
	gtaFolder + 'x64c.rpf',
	gtaFolder + 'x64d.rpf',
	gtaFolder + 'x64e.rpf',
	gtaFolder + 'x64f.rpf',
	gtaFolder + 'x64g.rpf',
	gtaFolder + 'x64h.rpf',
	gtaFolder + 'x64i.rpf',
	gtaFolder + 'x64j.rpf',
	gtaFolder + 'x64k.rpf',
	gtaFolder + 'x64l.rpf',
	gtaFolder + 'x64m.rpf',
	gtaFolder + 'x64n.rpf',
	gtaFolder + 'x64o.rpf',
	gtaFolder + 'x64p.rpf',
	gtaFolder + 'x64q.rpf',
	gtaFolder + 'x64r.rpf',
	gtaFolder + 'x64s.rpf',
	gtaFolder + 'x64t.rpf',
	gtaFolder + 'x64u.rpf',
	gtaFolder + 'x64v.rpf',
	gtaFolder + 'x64w.rpf'
]

def clearTerminal():
	os.system('cls')

def move(gtaFolder, src, backup):
	shutil.move(gtaFolder + src, backup)
	print('Moving "' + src + '" to the backup folder...')

def check(gtaFolder, gtaFoldersG, gtaFiles):
	while True:
		stupidFolders = []
		stupidFiles = []

		for gtaFoldee in gtaFoldersG:
			print(gtaFoldee + '...')
			stupidFolders.append(os.path.exists(gtaFolder + gtaFoldee))

		for gtaFile in gtaFiles:
			print(gtaFile + '...')
			stupidFiles.append(os.path.isfile(gtaFolder + gtaFile))

		if all(stupidFiles):
			print('GTA V folder is corrupted!')
			if all(stupidFolders):
				return False
				break
		else:
			return True
			break

while True:
	if ctypes.windll.shell32.IsUserAnAdmin() == 0:
		print('Permission denied! Make sure you are admin')
		break
	else:
		clearTerminal()
		print('Removing mods...')
		move(gtaFolder, 'mods', backUpFolder)
		move(gtaFolder, 'asiloader.log', backUpFolder)
		move(gtaFolder, 'dinput8.dll', backUpFolder)
		move(gtaFolder, 'NativeTrainer.asi', backUpFolder)
		move(gtaFolder, 'openCameraV.asi', backUpFolder)
		move(gtaFolder, 'openCameraV.log', backUpFolder)
		move(gtaFolder, 'OpenInteriors.asi', backUpFolder)
		move(gtaFolder, 'OpenInteriors.ini', backUpFolder)
		move(gtaFolder, 'OpenIV.asi', backUpFolder)
		move(gtaFolder, 'OpenIV.log', backUpFolder)
		move(gtaFolder, 'ScriptHookV.dll', backUpFolder)
		move(gtaFolder, 'ScriptHookV.log', backUpFolder)
		print('Checking GTA V...')
		if check(gtaFolder, foldersList, filesList) == True:
			print('GTA V is online')
			break
		break
		
## TO CONTINUE
import shutil
import ctypes
import sys
import os

gtaFolderPath = 'C:\\Program Files\\Rockstar Games\\Grand Theft Auto V\\'
backUpFolderPath = 'C:\\Program Files\\Rockstar Games\\Grand Theft Auto V\\__BACKUP'

gtaFoldersList = [
	gtaFolderPath + 'update',
	gtaFolderPath + 'x64',
]

gtaFilesList = [
	gtaFolderPath + 'bink2w64.dll',
	gtaFolderPath + 'common.rpf',
	gtaFolderPath + 'd3dcompiler_46.dll',
	gtaFolderPath + 'd3dcsx_46.dll',
	gtaFolderPath + 'GFSDK_ShadowLib.win64.dll',
	gtaFolderPath + 'GFSDK_TXAA.win64.dll',
	gtaFolderPath + 'GFSDK_TXAA_AlphaResolve.win64.dll',
	gtaFolderPath + 'GPUPerfAPIDX11-x64.dll',
	gtaFolderPath + 'GTA5.exe',
	gtaFolderPath + 'GTAVLanguageSelect.exe',
	gtaFolderPath + 'GTAVLauncher.exe',
	gtaFolderPath + 'NvPmApi.Core.win64.dll',
	gtaFolderPath + 'PlayGTAV.exe',
	gtaFolderPath + 'index.bin',
	gtaFolderPath + 'version.txt',
	gtaFolderPath + 'x64a.rpf',
	gtaFolderPath + 'x64b.rpf',
	gtaFolderPath + 'x64c.rpf',
	gtaFolderPath + 'x64d.rpf',
	gtaFolderPath + 'x64e.rpf',
	gtaFolderPath + 'x64f.rpf',
	gtaFolderPath + 'x64g.rpf',
	gtaFolderPath + 'x64h.rpf',
	gtaFolderPath + 'x64i.rpf',
	gtaFolderPath + 'x64j.rpf',
	gtaFolderPath + 'x64k.rpf',
	gtaFolderPath + 'x64l.rpf',
	gtaFolderPath + 'x64m.rpf',
	gtaFolderPath + 'x64n.rpf',
	gtaFolderPath + 'x64o.rpf',
	gtaFolderPath + 'x64p.rpf',
	gtaFolderPath + 'x64q.rpf',
	gtaFolderPath + 'x64r.rpf',
	gtaFolderPath + 'x64s.rpf',
	gtaFolderPath + 'x64t.rpf',
	gtaFolderPath + 'x64u.rpf',
	gtaFolderPath + 'x64v.rpf',
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
		"yes": True, 
		"y": True, 
		"ye": True,
		"no": False, 
		"n": False
	}
	
	if default is None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:
		sys.stdout.write(question + prompt)
		choice = raw_input().lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

def moveToBackupFolder(gtaFolderPath, mod, backup):
	if (os.path.exists(backUpFolderPath)) and (os.path.isdir(backUpFolderPath)):
		shutil.move(gtaFolderPath + mod, backup)
		print('Moving "' + mod + '" to the backup folder...')
	else:
		if yesNo('The backup folder doesn\'t seem to exists, would like to create one?') == True:
			shutil.move(gtaFolderPath + mod, backup)
			print('Moving "' + mod + '" to the backup folder...')
		else:
			print('Aborting...')
			return False

#TODO: CHECK FOR GTA V VERSION
#TODO: ADD NEW FOLDERS/FILES
#TODO: IGNORE REDIS/README
#TODO: COMPRESS IN ZIP FILE
#TODO: UPLOAD IT IN THE CLOUD

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
