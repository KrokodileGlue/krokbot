import socket
import ssl
import sys

class Connection:
	con = socket.socket()

	def __init__(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.con = ssl.wrap_socket(sock)

	def send(self, chan, msg):
		self.con.send("PRIVMSG " + chan + " " + msg + "\n")

	def connect(self, server, port, nick):
		self.con.connect((server, port))
		self.con.send("USER " + nick + " " + nick + " " + nick + " :realname\n")
		self.con.send("NICK " + nick + "\n")

	def join(self, channel):
		self.con.send("JOIN " + channel + "\n")

	def part(self, channel):
		self.con.send("PART " + channel + " :Leaving\n")

	def get_text(self):
		text = self.con.recv(2040) # receive some bytes

		if text.find('PING') != -1:
			self.con.send('PONG ' + text.split() [1] + '\r\n')

		return text
