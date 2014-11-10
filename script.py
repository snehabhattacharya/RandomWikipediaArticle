from bs4 import BeautifulSoup
import urllib2
import webbrowser

print 'enter=next article, o = open article , x=exit'
print
while True:
	content=urllib2.urlopen('http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=xml')
	xml=content.read()
	content.close()
	soup=BeautifulSoup(xml)
	links=soup.findAll('page')
	for i in links:
		choice=raw_input('Read about' +i.get('title').encode('ascii', 'ignore'))
		if choice == 'o':
			webbrowser.open_new_tab('http://en.wikipedia.org/wiki?curid='+i.get('id'))
		elif choice=='x':
			exit(0)

