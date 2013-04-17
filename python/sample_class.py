class atest():
    def __init__(self,a="I am a test"):
        self.a = a

    def __str__(self):
        return self.a

    def beer(self):
        print "I am not"

def runner():
    tests = {}
    tests['a'] = atest

    print tests
    b = tests['a']("beer")
    c = tests['a']()
    print b
    b.beer()
    print c


if __name__ == "__main__":
    runner()

