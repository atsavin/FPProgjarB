import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
sock.bind(server_address)
sock.listen(10)
print >>sys.stderr, 'starting up on %s port %s' % server_address

while True:
    
    	print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
    	print >>sys.stderr, 'connection from', client_address
    
        data = connection.recv(2048)
	print data
	direktori = data.split()
	dir1=direktori[1]
	if direktori[1][0]=='/' :
		try :
			fopen=open(direktori[1][1:] + ".jpg")
			gambar = fopen.read()
			respon ="\HTTP/1.1 200 OK \n\n%s"%gambar
			fopen.close()
		except :
			respon = "\HTTP/1.1 200 OK \n\ngambar tidak ada"
	print direktori[1][1:]  	
	#respon = "Sukses Menyambung ke Web Server"
	
	connection.send(respon)
	connection.close()
