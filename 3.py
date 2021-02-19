#kalispera sas
#se afto pernoume ena ssl cerficate kai parousiazoume se esas ta dedomena
#stin arxi perno san input ta hostname ti ora thelei episis perno  to subject kai to common name
# meta lamvano apo ta sait ta cerficate kai  ektipono to issuer  commonName kai to subject organizationName
# epeita  elenxo ta subject ama einai idia san afto pou edwse o xristis meta kano diafores epeksergasies me tin imerominias gia na mporo na kano elexnous
# kano elenxous gia to cerfitcate ama einai egkiro kai meta episis ektelo  elenxo stin lsita common name
#



import socket
import ssl
from datetime import datetime, date, time, timezone
import datetime
list_for_common_name = set(
    ["DigiCert SHA2 High Assurance Server CA", "GTS CA 1O1","TERENA SSL CA 3","GlobalSign RSA OV SSL CA 2018","GTS CA 1D2","Let's Encrypt Authority X3"]) # edo einai lista gia ta common name

hostname=input("dwse to hostname")

apantisigiatime = int(
    input("pata 1 gia na valeis time now i 2 gia sigkekrimeni imerominia")
) # perimeno apantisi apo to xristi gia to ti tha kanei

if apantisigiatime == 2:
    date_entry = input("Enter a date in YYYY-MM-DD format")
    year, month, day = map(int, date_entry.split("-"))
    datey = datetime.date(year, month, day)
    date123 = datey.strftime("%Y-%m-%d") # perno tin imerominia se katalilo format


sub = input("dwse to subject")
cm= input("dwse to common name exoume kai merika se lista ")
list_for_common_name.add(cm)

ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
    s.connect((hostname, 443))
    cert = s.getpeercert()

type(cert)
x = date.today()

version = cert["version"]
beginday = cert["notBefore"]
lastday = cert["notAfter"]
subject = cert["subject"]
issuer = cert["issuer"]

# edo perno ta stoxeia pou xriazazomai apo to sait

issueronly = dict(x[0] for x in cert["issuer"])
issued_to = issueronly["commonName"]
print(issued_to)

subject1 = dict(x[0] for x in cert["subject"])
subject2 = subject1["organizationName"]

print(subject2)


if subject2 == sub:#edo kano elenxo ta sujbect sxetika me afta pou edose o xristis
    print("ta subject einai idia \n ")
else:
    print("ta subject DEN einai idia \n ")


lastday = datetime.datetime.strptime(lastday, r"%b %d %H:%M:%S %Y %Z")
lastday = lastday.strftime("%Y-%m-%d")
startday = datetime.datetime.strptime(beginday, r"%b %d %H:%M:%S %Y %Z") #perno tis times apo to cert kai tis metatrepo
startday = startday.strftime("%Y-%m-%d")
now = x.strftime("%Y-%m-%d")

print("i imerominia  enarksis einai",startday,"kai i imerominia liksis einai",lastday) # ektipono tis imerominies tou pistopoitikou



if apantisigiatime == 1:

    if startday < lastday and startday < now and lastday > now: #elenous sxetika me to time now
        print("good cerficitate")
    else:
        print("not good cerficitate")


if apantisigiatime == 2:
    if startday < lastday and startday < date123 and lastday > date123: # elenxous sxetika me tin imeromina pou edwse o xristis
        print("good cerficitate \n ")
    else:
        print("not good cerficitate \n")



if issued_to in list_for_common_name: # elenxos gia to common name ama einai stin lista pou exoume stin arxi
    print("einai mesa stin lista me ta common name \n")

print("i version tou cerficitate einai ",version)
