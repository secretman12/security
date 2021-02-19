#kalispera sas
#se afto to programa perno to username kai to password kai kano hash sto password kai to grafo sto  myfile.txt


import nacl.pwhash 
file1 = open("myfile.txt","a+")
username = input("Enter your username!:")
password = input("Enter your  password!:").encode()#kato to password encode
hash=nacl.pwhash.str(password) # kano to hash

file1.write("{} {} \n".format(username,hash.decode()))#ta grafo sto file




    