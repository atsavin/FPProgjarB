import sys
import socket

server_list = []
nserver=5 
i=0

def getList() :
	server_list.append("10.151.40.60:9999/\r\n\r\n")
	server_list.append("10.151.40.60:9998/\r\n\r\n")
	server_list.append("10.151.40.100:9997/\r\n\r\n")
	server_list.append("10.151.40.193:9996/\r\n\r\n")
	server_list.append("10.151.40.193:9995/\r\n\r\n")


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('10.151.40.162', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
getList()
# Listen for incoming connections
sock.listen(1)

while True:
    	# Wait for a connection
    	#print >>sys.stderr, 'waiting for a connection'
    	#connection, client_address = sock.accept()
    	#print >>sys.stderr, 'connection from', client_address
    	# Receive the data in small chunks and retransmit it
    	#while True:
		connection, client_address = sock.accept()
        	data = connection.recv(1000)
        	header = data
		
		if (header.startswith("GET / HTTP/1")) :
			
		    	if data:
				if i == nserver :
					i = 0
					#connection.close()
				loc = """HTTP/1.1 302 Found\r\nLocation: http://"""
				locate = loc + server_list[i]

				connection.send(locate)
				print locate				
				connection.close()
				if i != nserver :
					i = i+1

		    	else:
		        	print >>sys.stderr, 'no more data from', client_address
		        	break
