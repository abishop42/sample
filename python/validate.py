from urlparse import urlparse
import httplib
from httplib import HTTP

urllist = ["www.tab.com.au","theage.com.au","abc.net.au","clients.GET"]
responses = httplib.responses
valid = [responses[200]]
def isvalid(res):
    s = responses[res[0]]
    return s in valid

def urlcheck(url):
   u = urlparse(url)
   h = HTTP(u.geturl())
   print u.geturl()
   h.putrequest('HEAD',u.geturl())
   h.endheaders()
   r = h.getreply()
   return isvalid(r)


for u in urllist:
    res = urlcheck(u)
    print "%s isvalid? %s"%(u,res) 
