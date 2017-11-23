import os

class AndroidProperty(object):
	size = 0, 0
	folderName = ""
	fileName = "ic_launcher.png"
	
	def __init__(self, size, folderName):
		self.size = size
		self.folderName = folderName

class AndroidProperties(object):

	#Android Icon Design Guidelines: https://developer.android.com/guide/practices/ui_guidelines/icon_design.html
	ldpi = AndroidProperty((36, 36), "mipmap-ldpi")
	mdpi = AndroidProperty((48, 48), "mipmap-mdpi")
	hdpi = AndroidProperty((72, 72), "mipmap-hdpi")
	xhdpi = AndroidProperty((96, 96), "mipmap-xhdpi")
	xxhdpi = AndroidProperty((144, 144), "mipmap-xxhdpi")
	xxxhdpi = AndroidProperty((192, 192), "mipmap-xxxhdpi")
	
	allProperties = [ldpi, mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi]

	def __init__(self):
		pass

	@staticmethod
	def createFolders(parentFolder):
		for property in AndroidProperties.allProperties:
			os.makedirs(parentFolder+"/"+property.folderName)