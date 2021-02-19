#edo kanoume hack sto password pou exoume apo prin
# anoigo to file kano append gia na xoriso ta dedomena  kai to idio kano kai sta password
# kai epeita dokimazo ta password  gia na vro kapoio swsto apotelemsa
# otan vro to sosto apotelesma kano kai ena break gia na stamataei


import nacl.pwhash
user1=[]#pinakes gia ta dedomena
password1=[]
file1 = open("date.txt","r");

for line in file1:

    user1.append({line.split()[0]) #spao to text arxeio


file2=open("my_passwords.txt","r")

for line in file2:
    password1.append(line.split(maxsplit=1)[0]) # spao ta password


for user in user1:#for gia tous user kai gia ta password
    for password in password1:

        try:
            res = nacl.pwhash.verify(user.encode(), password.encode())
            break;#otan vrei to apotelesma stamataei
        except:
            print(False)