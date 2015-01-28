import urllib2

def e1_chunks():
    url = "http://192.168.1.3:1234"
    fd = urllib2.urlopen(url)
    fdo = open("centos.so", "w")
    
    def lee(fd):
            chunk = fd.read(8192)
            while chunk:
                    yield chunk
                    chunk = fd.read(8192)
    
    for chunk in lee(fd):
            fdo.write(chunk)
    fdo.close()

def main():
    e1_chunks()
    
if __name__ == "__main__":
    main()