import sys
import socket

server_list = []
nserver=5 
i=0

def getList() :
	server_list.append("localhost:9999")
	server_list.append("localhost:9998")
	server_list.append("localhost:9997")
	server_list.append("localhost:9996")
	server_list.append("localhost:9995")


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
getList()
# Listen for incoming connections
sock.listen(1)

while True:
    	# Wait for a connection
    	print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
    	print >>sys.stderr, 'connection from', client_address
    	# Receive the data in small chunks and retransmit it
    	while True:
        	data = connection.recv(1000)
        	header = data
		
		if (header.startswith("GET / HTTP/1.1")) :
			print 'okeoke'
		    	if data:
				if i == nserver :
					index = 0
					i = 0
				else :
					index = i+1


				loc = """HTTP/1.1 302 Found Location: http://"""
				locate = loc + server_list[index] + "/"
				print locate
				connection.send(locate)	
				i = i + 1

		    	else:
		        	print >>sys.stderr, 'no more data from', client_address
		        	break
        # Clean up the connection
	connection.close()
