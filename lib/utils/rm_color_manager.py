class RMColorManager(object):
	
	lila = '\033[95m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	end = '\033[0m'
	bold = '\033[1m'
	underline = '\033[4m'

	def __init__(self):
		pass

	@staticmethod
	def printWithColor(text, color):
		print(color + text + RMColorManager.end)

	@staticmethod
	def printError(text):
		print(RMColorManager.red + text + RMColorManager.end)
		
	@staticmethod
	def printBold(text):
		print(RMColorManager.bold + text + RMColorManager.end)
