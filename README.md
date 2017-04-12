<h1 id="facebookphonescanner"><b>#FacebookPhoneScanner (Python 2.x)</b></h1>

<ul>
<li>Questo script esegue un bruteforce sulla ricerca delle persone tramite numero telefonico offerta da <a href="http://www.facebook.com">Facebook.com</a></li>
<li>Una volta trovato un numero telefonico esistente, il programma si occupa di estrarre nome e cognome ad esso abbinati per poi salvare il tutto in un file .txt</li>
<li>Sono disponibili due modalità di ricerca: tramite un range di numeri dato in input o tramite una lista di numeri salvata su file (un numero per riga, estensione .txt)</li>
<li>Entrambe le modalità sono multithread e il numero di thread è selezionabile dall'utente</li>
</ul>

<p>USO:  <code>pyhton fps.py</code></p>

<p>Prima di avviare lo script sarebbe bene fare il login su Facebook con un normale browser, per evitare captcha che interferirebbero con il corretto funzionamento del programma. E' inoltre consigliato decommentare e modificare i cookie alla riga 18.<br /><br />
I numeri vanno inseriti con il prefisso nazionale all'inizio ma senza il simbolo "+" (es: 39350XXXXXXX)<br /><br />
NON tutti i numeri possono essere abbinati ad un nome e cognome, in base alle impostazioni di privacy usate dalle persone (di default la privacy del numero telefonico è impostata su "pubblico")<br /><br />
E’ inoltre essenziale ricordarsi che Facebook permette di scansionare soltanto qualche centinaio di numeri all’ora, quindi se lo script non trova più risultati dopo vari minuti di esecuzione occorre aspettare il trascorrere dell’ora successiva.</p>

<h4>NON MI ASSUMO ALCUNA RESPONSABILITA' DELL'USO CHE FARETE DI QUESTO SCRIPT</h4>
