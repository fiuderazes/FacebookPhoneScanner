import urllib2, re, time, sys, random
from threading import Thread

global stop_now, start, end, threads
stop_now = False
start=393505200000
end=393505210000
threads = 100

global opener
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'datr=1234; lu=1234; fr=1234; locale=it_IT; c_user=1234; xs=1234; csm=2; s=1234; pl=n; p=-2; presence=1234; wd=1600x805'))
opener.addheaders.append(('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'))

class httpPost(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.running = True

	def _send_http_post(self, pause=10):
		global stop_now, start, end

		#QUI SPEDISCE LA RICHIESTA HTTP
		start_locale=start
		start+=1
		time.sleep(random.uniform(0.1, 5))
		response = opener.open("https://www.facebook.com/search/top/?q=%d" % start_locale)
		page_source = str(response.read())
		nome = re.compile("<div class=\"_5d-5\">([^<]+)").findall(page_source)
		if len(nome)>0:
			print str(start_locale)+" = "+str(nome[0])
			with open("lista.txt", "a") as myfile:
				myfile.write(str(start_locale)+" = "+str(nome[0])+"\n")

		if start_locale>=end:
			stop_now=True

		for i in range(0, 9999):
			if stop_now:
				self.running = False
				break

	def run(self):
		while self.running:
				self._send_http_post()

def main():
	global stop_now, thread
	
	rthreads = []
	for i in range(threads):
		t = httpPost()
		rthreads.append(t)
		t.start()

	while len(rthreads) > 0:
		try:
			rthreads = [t.join(1) for t in rthreads if t is not None and t.isAlive()]
		except KeyboardInterrupt:
			print "\nShutting down threads...\n"
			for t in rthreads:
				stop_now = True
				t.running = False

if __name__ == "__main__":
	main()