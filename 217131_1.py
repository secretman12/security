import socket
import ssl
from datetime import datetime, date, time, timezone
import datetime
user2=[]
file1 = open("a.txt","r")#anoigo ta file
file2 = open("date.txt","a+")




for line in file1:
        if line.strip():
            site=line.split(maxsplit=1)[0]
            user2.append(site)


ctx = ssl.create_default_context()
for x1 in user2:
    hostname = x1# kano to hostname

# kati den trexei kala edo pera
try:
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        print(hostname)
        s.connect((hostname, 443))
        cert = s.getpeercert()
        type(cert)#perno to certificate
        beginday = cert["notBefore"] # perno to certificate
        startday = datetime.datetime.strptime(beginday, r"%b %d %H:%M:%S %Y %Z") #perno tis times apo to cert kai tis metatrepo
        startday = startday.strftime("%Y%m%d")
        print(startday)
        file2.write("{}\n".format(startday)) #grafo ta dedomena
except:
    print("False")