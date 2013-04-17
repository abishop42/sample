import httplib
import socket

responses = httplib.responses

urls=["http://www.google.com","www.theage.com.au"\
      ,"abc.net.au/iview","clients.get",\
      "http://docs.python.org/library/socket.html",\
      "http://www.theage.com.au/national/Places/Melbourne",\
      "http://www.nrl.com/TelstraPremiership/MatchCentre/tabid/10999/Default.aspx#matchid=1354&tab=Preview",\
      "http://au.yahoo.com/?p=us",\
      "http://au.mg4.mail.yahoo.com/neo/launch?.rand=9jfeo4qllom4i"]


def parseurl(url):
   base = url
   head = "/"
   if '#' in url:
       base = url[0:url.find('#')]
   elif '?' in url:
       base = url[0:url.find('?')]
   if '/' in url:
       base = base[0:base.find('/')]
       head = base[base.find('/')+1:]
   print url,base,head
   return base,head
def checkurl(url):
   result = False
   base,head = parseurl(url)
   try:
      conn = httplib.HTTPConnection(base)
      conn.request('HEAD',head)
      resp = conn.getresponse()
      print resp.status,responses[resp.status],url
      result = True
   except socket.gaierror:
      print "invalid url",url
   return result

for u in urls:
   if "://" in u:
       checkurl(u.split("://")[1])
   else:
       checkurl(u)

