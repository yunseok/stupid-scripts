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