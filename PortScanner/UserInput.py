# 09/25: Port concerns (ranges) should to be handled
# by specialized class.

class UserInput:

	def __init__(self, targetStrName):
		self.targetStrName = targetStrName

	def printTargetStrName(self):
		print(self.targetStrName)

	# #Overload constructor
	# def __init__(self, targetStrName, minPort, maxPort):
	# 	self.targetStrName = targetStrName
	# 	self.minPort = minPort
	# 	self.maxPort = maxPort

u = UserInput('str')
print(u)
u.printTargetStrName()

# i = UserInput('str', 'max', 'min')
# print(i)

	# string target
	# string (?) targetHostname
	# int minPort
	# int maxPort

	# # UserInput object will retain the state of
	# # the user's input.
	# def  __init__ (
		# int minPort,
		# int maxPort):

		# self.target = getTargetName()

		# # Note: Set defaults for minPort and
		# # maxPort if none entered.
		# self.minPort = minPort
		# self.maxPort = maxPort

		# (?) self.targetHostname = self.gethostname()

	# # Kick off:
	# # targetStrName will be converted to address
	# # in SocketHandling
	# method string getTargetName()

	# method bool minPortIsNotEqualToMaxPort

	# method bool minPortIsLessThanMaxPort

	# method portNumberInTCPrange
		# # Checks if port number is in TCP
		# # range.