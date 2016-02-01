#wordlist generator
#Author:Sudarshan Pawar
import itertools


num_list= '012356789'
char_list='abcdefghijklmnopqrstuvwxyz'
spcl_char_list='!@#$%^&*()-_=+\/'

print '''
+--------------------------------------+
|   W O R D L I S T  | C R E A T O R   |
+--------------------------------------+
|Author: Sudarshan Pawar               |
|email : collemijocks@gmail.com        |
+--------------------------------------+
|Creates .txt file in current directory|
|         ***MENU***                   |
|1. Numbers[0-9]                       |
|2. Characters[a-z]                    |
|3. Special Characters[!@#$%^&*()+_/.] |
+--------------------------------------+
Select any one option!
'''
choice=input("Enter the choice number:")
    
def characters(char_list):
    length=input("Enter the length:")
    #wordlist=open("Charlist.txt","w")
    for i in itertools.product(char_list,repeat=length):
        print ''.join(i)+ '\n'
        #wordlist.writelines(op)
    #wordlist.close()
    #print "Done!"
        
def numbers(num_list):
    length=input("Enter the length:")
    wordlist=open("Numlist.txt","w")
    for i in itertools.product(num_list,repeat=length):
        op=''.join(i)+ '\n'
        wordlist.writelines(op)
    wordlist.close()
    print "Done!"

def spclchars(spcl_char_list):
    length=input("Enter the length:")
    #wordlist=open("SpclCharlist.txt","w")
    for i in itertools.permutations(spcl_char_list,length):
        print ''.join(i)+'\n'
        #wordlist.writelines(op)
    #wordlist.close()
    #print "Done!"

if choice==1:
    numbers(num_list)
elif choice==2:
    characters(char_list)
elif choice==3:
    spclchars(spcl_char_list)
else:
    print("INVALID CHOICE!")
