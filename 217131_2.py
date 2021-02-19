
from itertools import combinations_with_replacement
import nacl.pwhash
user1=[]#pinakes gia ta dedomena
password1=[]
file1 = open("date.txt","r")
file2=open("my_passwords","r")
newsait=[]

for line in file1:

  user1.append({line.split()[0]}) #kano append ta dedomena
  #spao to text arxeio

  alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

  for (a, b, c) in combinations_with_replacement(alphabets, 3): # me afto exo ola ta pithana dedomena
      newsait = (a + b + c)


file2=open("passwords.txt","r")

for line in file2:
    password1.append(line.split(maxsplit=1)[0]) # spao ta password




    for user in user1:
         for password in password1:
            try:
                res = nacl.pwhash.verify(user.encode(), password.encode())
                break;  # otan vrei to apotelesma stamataei tin diadikasia
            except:
                print(False)