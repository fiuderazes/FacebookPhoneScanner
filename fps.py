#Librerie
import urllib2, re, time, sys, random
from threading import Thread

#Banner
print '''
    ______                __                __      ____  __                        _____                                 
   / ____/___  ________  / /_  ____  ____  / /__   / __ \/ /_  ____  ____  ___     / ___/_________  ____  ____  ___  _____
  / /_  / __ \/ ___/ _ \/ __ \/ __ \/ __ \/ //_/  / /_/ / __ \/ __ \/ __ \/ _ \    \__ \/ ___/ __ \/ __ \/ __ \/ _ \/ ___/
 / __/ / /_/ / /__/  __/ /_/ / /_/ / /_/ / /<    / ____/ / / / /_/ / / / /  __/   ___/ / /__/ /_/ / / / / / / /  __/ /    
/_/    \____/\___/\___/_____/\____/\____/_/|_|  /_/   /_/ /_/\____/_/ /_/\___/   /____/\___/\____/_/ /_/_/ /_/\___/_/ 
'''

#Richiesta
global opener
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'lu=xxx; fr=xxx; c_user=xxx; xs=xxx;'))
opener.addheaders.append(('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'))

def fbCheck(numero):
	response = opener.open("https://www.facebook.com/search/top/?q=%d" % numero)
	page_source = str(response.read())
	nome = re.compile("<div class=\"_5d-5\">([^<]+)").findall(page_source)
	if len(nome)>0:
		sys.stdout.write(str(numero)+" = "+str(nome[0])+"\n")
		with open("lista.txt", "a") as myfile:
			myfile.write(str(numero)+" = "+str(nome[0])+"\n")

#Controllo se Facebook e' on
try:
	sys.stdout.write("Sto controllando se riesco a collegarmi a Facebook...\n")
	ret = urllib2.urlopen('https://www.facebook.com/')
	sys.stdout.write("Connessione riuscita!\n")
	#Modalita' di scansione (range o da file)
	mode = input("\n\nScegli la modalita'\n1. Range\n2. Da file\nScelta: ")
	if mode == 1:
		threads = input("\nThread: ")
		startn	= input("Numero di partenza: ")
		startn_o= startn-1
		endn	= input("Numero di fine: ")
		finiti	= 0
		print "\n"
		if endn-startn_o>0:
			class newThread(Thread):
				def __init__(self):
					Thread.__init__(self)
					self.daemon = True
					self.start()
				def run(self):
					global threads, startn, endn, finiti, startn_o
					while True:
						#Richiesta http
						if startn<=endn:
							fbCheck(startn)
							startn=startn+1
						else:
							finiti=finiti+1
			for nt in range(threads):
				newThread()
			try:
				while True:
					if finiti>(endn-startn_o):
						print "\nFinito!...\n"
						exit()
					time.sleep(1)
			except KeyboardInterrupt:
				print "\nUscendo...\n"
		else:
			print "\nIl numero finale deve essere inferiore o uguale a quello iniziale! Uscendo...\n"
	elif mode == 2:
		filename = raw_input("\nInput file: ")
		file=open(filename)
		file=file.readlines()
		numerolinea=0
		numerolineamax=len(file)-1
		threads = input("Thread: ")
		print "\n"
		class newThread(Thread):
			def __init__(self):
				Thread.__init__(self)
				self.daemon = True
				self.start()
			def run(self):
				global numerolinea,numerolineamax
				while True:
					#Richiesta http
					numero=file[numerolinea].rstrip()
					numerolinea=numerolinea+1
					fbCheck(int(numero))
		for nt in range(threads):
			newThread()
		try:
			while True:
				if numerolinea>numerolineamax:
					exit()
				time.sleep(1)
		except KeyboardInterrupt:
			print "\nUscendo...\n"
	else:
		print "Inserisci una scelta valida! Uscendo...\n"

except urllib2.URLError, e:
	print "Non riesco a connettermi a Facebook!\nControlla le impostazioni di rete e i cookie alla riga 23!\n"
