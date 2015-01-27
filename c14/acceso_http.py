import urllib2
import urllib
import socket
from urllib2 import Request, urlopen, URLError, HTTPError


def acceso_ftp():
    # La forma mas simple de usar urllib2
    response = urllib2.urlopen('http://www.abc.es')
    html = response.read()
    print html
    
    
    # urllib2 maneja el concepto de peticion (request)
    # con el objeto Request se tiene el control sobre la peticion que se esta construyendo
    req = urllib2.Request('http://www.abc.es')
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page
    
    
    # Tambien podemos acceder a un ftp
    req = urllib2.Request('ftp://example.com/')
    
    
    # GET (urlencode con urllib, no urllib2)
    data = {}
    data['name'] = 'Somebody Here'
    data['location'] = 'Northampton'
    data['language'] = 'Python'
    data = urllib.urlencode(data)
    print data  # The order may differ. 
    
    url = 'http://www.example.com/example.cgi'
    full_url = url + '?' + data
    response = urllib2.urlopen(full_url)
    the_page = response.read()
    print the_page
    
    # POST
    data = {}
    data['name'] = 'Somebody Here'
    data['location'] = 'Northampton'
    data['language'] = 'Python'
    data = urllib.urlencode(data)
    
    url = 'http://www.someserver.com/cgi-bin/register.cgi'
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    
    
    # HEADERS
    data = {}
    data['name'] = 'Somebody Here'
    data['location'] = 'Northampton'
    data['language'] = 'Python'
    data = urllib.urlencode(data)
    
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    
    url = 'http://www.someserver.com/cgi-bin/register.cgi'
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    the_page = response.read()
    
    
    
    # EXCEPCIONES
    
    # URLError Errores en la comunicacion
    #     Tienen atributo e.reason
    
    # HTTPError Errores en el servidor
    #    Tienen atributo e.code que indica el codigo de error
    req = Request('http://www.abc.es')
    try:
        response = urlopen(req)
    except HTTPError as e:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    except URLError as e:
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    else:
        # everything is fine
        pass
    
    # Note
    #
    # The except HTTPError must come first, otherwise except URLError will also catch an HTTPError.
    
    
    
    # Hay quien prefiere recoger URLError (la mas generica), y realizar:
    req = Request('http://www.abc.es')
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        # everything is fine
        pass
    
    
    # TIMEOUTS
    
    # timeout in seconds
    timeout = 10
    socket.setdefaulttimeout(timeout)

def main():
    acceso_ftp()
    
if __name__ == "__main__":
    main()