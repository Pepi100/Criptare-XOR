import sys
from itertools import cycle

# python encrypt parolamea2021 input.txt output


if len(sys.argv) < 4:
    print("fatal: Missing arguments.")
    print("usage: python encrypt.py <passcode> <retrieved_file.txt> <output_file>")
    exit()

if len(sys.argv) > 4:
    print("warning: Too many arguments.")
    #print("usage: python encrypt.py <passcode> <retrieved_file.txt> <output_file>")
    #exit()
    #programul ruleaza in cazul in care numarul de argumente oferit este prea mare si foloseste doar primele 4 argumente date


operatie = sys.argv[0]
cheie = (sys.argv[1]).encode('ascii')
input_file = open(sys.argv[2], "rb")
output_file = open(sys.argv[3], "wb")



print([char ^ cParola for char, cParola in zip( input_file.read(), cycle(cheie) )])
output_file.write( bytearray( [char ^ cParola for char, cParola in zip( input_file.read(), cycle(cheie) )] ))
#Xorare



#text = list(open("input.txt").read())
#iesire = open("output", 'w')
#parola = input()
#for x in range(len(text)):
#    text[x] = chr(ord(text[x]) ^ ord(parola[x % len(parola)]))
#print("".join(text), file=iesire)