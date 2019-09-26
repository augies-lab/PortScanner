# 09/18: Began pseudocode for socket handling class.
# import socket

# class SocketHandling
	# # By default, the current port is the min port.
	# int currentPort = UserInput.minPort
	# socket openSocket

	# # SocketHandling object will retain the state of
	# # the current port, etc. [ADD]
	# def __init__ ()
		# self.currentPort = portIndex()
		# openSocket = socket.socket(socket.AF_INET, 
			# socket.SOCK_STREAM)

	# static method int portIndex()
		# try:
			# # Update currentPort?
			# for (?) port in range(UserInput.minPort,
				# UserInput.maxPort)

				# sock = socket.socket(socket.AF_INET,
					# socket.SOCK_STREAM)

				# targetIP = socket.gethostbyname(
					# UserInput.targetStrName)

				# result = sock.connect_ex(UserInput.targetStrName,
					# port)

				# if result == 0:
					# print "Port {}: Open".format(port)

				# sock.close()