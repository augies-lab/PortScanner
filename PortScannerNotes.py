# A Port Scanner determines which ports are listening and
# accepting connections on a target system. Services running
# on standard ports can be detected.

# A simple port scanner utlizes a brute force method. The
# scanner tries to open connections to every possible
# port on the target system.

# It's important to note this technique will be detected 
# by the target system. Each connection attempt will be
# logged. This scanner will focus on TCP ports.

# A TCP connection scanner uses TCP's three-way handshake
# protocol to connect to ports on the target system.

# A basic TCP connection scanner is made of the following parts:

# 