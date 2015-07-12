import socket
import socks
import httplib
import requests

def connectTor():
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
	socket.socket = socks.socksocket

def main():
	connectTor()
	
	print "Connected to Tor"

	#conn = httplib.HTTPConnection("why-did-she-leave-me.com")
	#conn.request("GET", "/")
	#response = conn.getresponse()
	response = requests.get("http://my-ip.herokuapp.com/")


	print response.text

if __name__ == '__main__':
	for i in range(3):
		main()
