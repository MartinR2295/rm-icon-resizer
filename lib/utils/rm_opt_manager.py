import sys
from lib.utils.rm_color_manager import *
import getopt

class RMOptManager(object):
	options = []
	argRequired = 0
	opts = None
	scriptName = ""
	
	def __init__(self, options):
		self.options = options
		
	def checkArguments(self):
		argv = sys.argv
		if len(argv) < 1+self.argRequired:
			self.usage()
			sys.exit()
		argv = argv[1:]
		
		try:
			shortOptString = ""
			longOptStringArray = []
			for option in self.options:
				shortOptString += option.shortIdentifier
				if option.valueRequired:
					shortOptString += ":"
					longOptStringArray.append(option.longIdentifier+"=")
				else:
					longOptStringArray.append(option.longIdentifier)
			
			opts, args = getopt.getopt(argv, shortOptString, longOptStringArray)
		except getopt.GetoptError:
			self.usage()
			sys.exit(2)
	
		self.opts = opts
	
	def argumentExist(self, option):
		for opt, arg in self.opts:
			if opt in ("-"+option.shortIdentifier, "--"+option.longIdentifier):
				return True
		return False
	
	def getArgument(self, option):
		for opt, arg in self.opts:
			if opt in ("-"+option.shortIdentifier, "--"+option.longIdentifier):
				return arg
		return None
	
	def usage(self):
		print("")
		RMColorManager.printBold("Usage of the "+self.scriptName+" Script")
		print("")
		for option in self.options:
			print("-"+option.shortIdentifier+", --"+option.longIdentifier+(" {arg}" if option.valueRequired else "")+":	"+option.description)
		print("")
	
class RMOption(object):
	
	shortIdentifier = ""
	longIdentifier = ""
	description = ""
	valueRequired = False
	
	def __init__(self, shortIdentifier, longIdentifier, valueRequired, description):
		self.shortIdentifier = shortIdentifier
		self.longIdentifier = longIdentifier
		self.valueRequired = valueRequired
		self.description = description
		pass