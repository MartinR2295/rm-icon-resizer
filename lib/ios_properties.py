class IOSField(object):
	size = 0, 0
	scaledSize = 0, 0
	idiom = "iphone"
	filename = ""
	scale = 1
	
	def __init__(self, size, idiom, filename, scale):
		self.size = size
		self.idiom = idiom
		self.filename = filename
		self.scale = scale
		
		self.scaledSize = (int(round(size[0]*scale)), int(round(size[1]*scale)))
		
	def getJson(self):
		jsonString = "		{\n"
		jsonString += "			\"size\" : \""+str(self.size[0])+"x"+str(self.size[1])+"\",\n"
		jsonString += "			\"idiom\" : \""+self.idiom+"\",\n"
		jsonString += "			\"filename\" : \""+self.filename+"\",\n"
		jsonString += "			\"scale\" : \""+str(self.scale)+"x\"\n"
		jsonString += "		}"
		return jsonString

class IOSProperties(object):
	#this template is for universal applications
	#iOS Icon Design Guidelines: https://developer.apple.com/ios/human-interface-guidelines/icons-and-images/app-icon/#app-icon-sizes
	
	#ipad
	ipad20x1 = IOSField((20, 20), "ipad", "Pad-Icon-20@1x.png", 1)
	ipad20x2 = IOSField((20, 20), "ipad", "Pad-Icon-20@2x.png", 2)
	ipad76x1 = IOSField((76, 76), "ipad", "Pad-Icon-76.png", 1)
	ipad76x2 = IOSField((76, 76), "ipad", "Pad-Icon-76@2x.png", 2)
	ipad83x2 = IOSField((83.5, 83.5), "ipad", "Pad-Icon-83.5@2x.png", 2)
	ipad29x1 = IOSField((29, 29), "ipad", "Pad-Icon-Small.png", 1)
	ipad29x2 = IOSField((29, 29), "ipad", "Pad-Icon-Small@2x.png", 2)
	ipad40x1 = IOSField((40, 40), "ipad", "Pad-Icon-Small-40@1x.png", 1)
	ipad40x2 = IOSField((40, 40), "ipad", "Pad-Icon-Small-40@2x.png", 2)
	
	#iphone
	i20x2 = IOSField((20, 20), "iphone", "Icon-20@2x.png", 2)
	i20x3 = IOSField((20, 20), "iphone", "Icon-20@3x.png", 3)
	i60x2 = IOSField((60, 60), "iphone", "Icon-60@2x.png", 2)
	i60x3 = IOSField((60, 60), "iphone", "Icon-60@3x.png", 3)
	i40x2 = IOSField((40, 40), "iphone", "Icon-Small-40@2x.png", 2)
	i40x3 = IOSField((40, 40), "iphone", "Icon-Small-40@3x.png", 3)
	i29x1 = IOSField((29, 29), "iphone", "Icon-Small.png", 1)
	i29x2 = IOSField((29, 29), "iphone", "Icon-Small@2x.png", 2)
	i29x3 = IOSField((29, 29), "iphone", "Icon-Small@3x.png", 3)
	appStore = IOSField((1024, 1024), "ios-marketing", "Icon-AppStore.png", 1)

	allProperties = [i20x2, i20x3, i60x2, i60x3, i40x2, i40x3, i29x1, i29x2, i29x3, ipad20x1, ipad20x2, ipad76x1, 
					ipad76x2, ipad83x2, ipad29x1, ipad29x2, ipad40x1, ipad40x2, appStore]

	folderName = "AppIcon.appiconset"
	jsonFileName = "Contents.json"
	version = 1
	author = "xcode"

	def __init__(self):
		pass
	
	@staticmethod
	def getContentsJson():
		jsonString = "{\n"
		jsonString += "	\"images\" : [\n"
		
		for i in range(0, len(IOSProperties.allProperties)):
			property = IOSProperties.allProperties[i]
			jsonString += property.getJson()
			if(i < len(IOSProperties.allProperties)-1):
				jsonString += ","
			jsonString += "\n"
			
		jsonString += "	],\n"
		jsonString += "	\"info\" : {\n"
		jsonString += "		\"version\" : "+str(IOSProperties.version)+",\n"
		jsonString += "		\"author\" : \""+IOSProperties.author+"\"\n"
		jsonString += "	}\n"
		jsonString += "}"
		
		return jsonString
	
	@staticmethod
	def createContentsJson(folderName):
		contentsJson = open(folderName+"/"+IOSProperties.jsonFileName, "w")
		contentsJson.write(IOSProperties.getContentsJson())
		contentsJson.close()