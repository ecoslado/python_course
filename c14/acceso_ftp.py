from ftplib import FTP

def acceso_ftp():
    ftp = FTP('ftp.debian.org')     # connect to host, default port
    ftp.login()                     # user anonymous, passwd anonymous@
    ftp.cwd('debian')               # change into "debian" directory
    ftp.retrlines('LIST')           # list directory contents
    ftp.retrbinary('RETR README', open('README', 'wb').write)
    ftp.quit()
    
    
    
    # FTP con TLS
    # Subclase que aporta seguridad a la conexion ftp
    #
    #
    # Se debe habilitar la proteccion manualmente, para ello:
    # FTP_TLS.prot_p()
    #   Set up secure data connection.
    #
    # FTP_TLS.prot_c()
    #    Set up clear text data connection.
    
    
    from ftplib import FTP_TLS
    ftps = FTP_TLS('ftp.python.org')
    ftps.login()           # login anonymously before securing control channel
    ftps.prot_p()          # switch to secure data connection
    ftps.retrlines('LIST') # list directory content securely
    ftps.quit()
    
    """
    Algunos metodos:
    
    FTP.set_debuglevel(level)
    
    FTP.connect(host[, port[, timeout]])
    
    FTP.login([user[, passwd[, acct]]])
     
    FTP.dir(argument[, ...])
     
    FTP.quit()
     
    FTP.close()
    """

def main():
    acceso_ftp()

if __name__ == "__main__":
    main()