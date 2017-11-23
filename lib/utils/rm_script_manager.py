import sys
from lib.utils.rm_color_manager import *

class RMScriptManager(object):

	def __init__(self):
		pass
	
	@staticmethod
	def checkVersion(version, errorMessage): #must be a Tuple (example: (3,6))
		if sys.version_info < version:
			RMColorManager.printError(errorMessage)
			sys.exit()

	@staticmethod
	def exitWithErrorAndUsage(message):
		RMColorManager.printError(message)
		sys.exit()
	
	@staticmethod
	def exitWithError(message):
		RMColorManager.printError(message)
		sys.exit()
	
		#try:
	#	import requests
	#except ImportError:
	#	RMColorManager.printError("Please install the python 'requests' module! (pip3 install requests)")
	#	sys.exit()