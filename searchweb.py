import ftplib
def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
        print dirList
    except:
        dirList = []
        print '[-] Could not list directory contents.'
        print '[-] Skipping To Next Target.'
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print '[+] Found default page: ' + fileName
            retList.append(fileName)
    return retList
host = '10.0.16.121'
userName = 'f2cdev'
passWord = '123456'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
returnDefault(ftp)
