import re


def parse(s,p,c):
    l = s
    if type(s) == type([]):
        for a in s:
            l = "%s%s"%(l,a)
    m = re.findall(p,l)
    d = {}
    for n in m:
            d[n.split(c)[0]] = n.split(c)[1]
    return d

l = ["aaa=this is A big than;bb=feed reel a MERKAT;cc=beer is all good\n","zz=dfsdfsd sdqwe szss aaa;ee=feed reel a MERKAT;zz=beer is all good\n"]
p = r'[a-z|A-Z]*=[a-z| |A-Z]*'
#if m:
#    for n in m:
#        print n.split("=")
#for a in l:
#    d = parse(a,p,'=')
#    print d
#print parse(l,p,'=')

s = "10.0.0.0"
r = [r'0.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.[0|255]',r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',r'127.(?:[\d]{1,3}).(?:[\d]{1,3}).(?:[\d]{1,3})']
m = []
for i in r:
    a = re.compile(i,re.IGNORECASE)
    m.append(a.match(s))

print m
print [n == None for n in m]
