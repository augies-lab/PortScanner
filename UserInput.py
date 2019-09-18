# 09/17: Began pseudocode for user input class.

# class UserInput
	# string target
	# string (?) targetHostname
	# int minPort
	# int maxPort

	# # UserInput object will retain the state of
	# # the user's input.
	# class instance UserInput(
		# string target, 
		# int minPort,
		# int maxPort)

		# self.target = target

		# # Note: Set defaults for minPort and
		# # maxPort if none entered.
		# self.minPort = minPort
		# self.maxPort = maxPort

		# (?) self.targetHostname = self.gethostname()

	# method IP (?) getHostName()
		# # Method will call Socket Handling
		# # class 

	# method bool minPortIsNotEqualToMaxPort

	# method bool minPortIsLessThanMaxPort

	# method portNumberInTCPrange
		# # Checks if port number is in TCP
		# # range.