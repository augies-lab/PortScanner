# 09/17: Began pseudocode for user input class.

# class UserInput:
	# string target
	# string (?) targetHostname
	# int minPort
	# int maxPort

	# # UserInput object will retain the state of
	# # the user's input.
	# def  __init__ (
		# int minPort,
		# int maxPort)

		# self.target = getTargetName()

		# # Note: Set defaults for minPort and
		# # maxPort if none entered.
		# self.minPort = minPort
		# self.maxPort = maxPort

		# (?) self.targetHostname = self.gethostname()

	# # Kick off:
	# method string getTargetName()
		# target = raw_input("Enter scan target: ")

	# method bool minPortIsNotEqualToMaxPort

	# method bool minPortIsLessThanMaxPort

	# method portNumberInTCPrange
		# # Checks if port number is in TCP
		# # range.