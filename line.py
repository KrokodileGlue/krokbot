from connection import *
import random
import re

nick_regex = "[\w\-]*"

class Message:
	def __init__(self, line):
		self.line      = line
                self.valid = False
		if self.is_message():
                        self.valid = True
			self.nick      = self.get_nick()
			self.channel   = self.get_channel()
			self.message   = self.get_message()
			self.addressee = self.get_addressee()
			self.reply     = self.get_reply()
	def get_nick(self):
		sender = re.search(":(.*)!.*PRIVMSG (.*) :(.*)", self.line)
		return sender.group(1)
	def get_channel(self):
		sender = re.search(":(.*)!.*PRIVMSG (.*) :(.*)", self.line)
		return sender.group(2)
	def get_message(self):
		sender = re.search(":(.*)!.*PRIVMSG (.*) :(.*)", self.line)
		return sender.group(3)
	def get_addressee(self):
		if is_message(self.line):
			a = re.search("^(" + nick_regex + ")[:,] *(.*)", get_message(self.line), re.I | re.M)
			if a == None:
				return "<none>"
			else:
				return a.group(1)
	def get_reply(self):
		if is_message(self.line):
			a = re.search("^(" + nick_regex + ")[:,] *(.*)", get_message(self.line), re.I | re.M)
			if a == None:
				return "<none>"
			else:
				return a.group(2)
	def is_message(self):
		return re.match(":(.*)!.*PRIVMSG (.*) :(.*)", self.line) != None

def process_command(bot, line, channel, nick):
	cmd = line
	cmd = cmd.split()
	srand = random.SystemRandom()

	print "cmd: '" + cmd[0] + "'"

	if cmd[0] == "join":
		bot.con.join(cmd[1])
	elif cmd[0] == "part":
		bot.con.part(cmd[1])
	elif cmd[0] in greetings:
                send_to = nick if channel == bot.nick else channel
                greeting = srand.choice(greetings)
                print "sending '" + greeting + "' to " + send_to
		bot.con.send(send_to, nick + ": " + greeting)

def process_line(bot, line):
	if is_message(line):
		nick	  = get_nick(line)
		addressee = get_addressee(line)
		channel   = get_channel(line)
		msg	  = get_message(line)
		reply	  = get_reply(line)

		print nick + " addressed " + addressee + " on " + channel + ": " + (msg if reply == "<none>" else reply)
		if addressee == bot.nick:
			print "command: " + reply
			process_command(bot, reply, channel, nick)
		elif channel == bot.nick:
			print "command: " + msg
			process_command(bot, msg, channel, nick)
	else:
		print line,
