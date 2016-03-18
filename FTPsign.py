import ftplib
def anonLogin(hostname) :
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('f2cdev', '123456')
        print '\n[*]' + str(hostname) + ' FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return True
    except Exception, e:
        print '\n[-]' + str(hostname) + ' FTP Anonymous Logon Failed.'
        return False
host = '10.0.16.121'
anonLogin(host)