from connection import *
from line import *
import os
import random

class smh:
        con = Connection()

        server  = "krok.gq"
        port    = 5586
        nick    = "bot"
        admin   = "k"

        def __init__(self):
		self.con.connect(self.server, self.port, self.nick)

#bot = smh()

msg = Message(":tytan!~artorias@2a02:908:d513:dfe0:e435:4110:67f2:5ff3 PRIVMSG ##C :like seriously? ^^")

if msg.valid:
        print msg.nick + ", " + msg.addressee

#while 1:
	#text = bot.con.get_text()
	#process_line(bot, text)
