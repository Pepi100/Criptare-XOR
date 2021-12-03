import sys
from itertools import cycle


if len(sys.argv) < 4:
    print("fatal: Missing arguments.")
    print("usage: python decrypt.py <output_file> <passcode> <retrieved_file.txt>")
    exit()

if len(sys.argv) > 4:
    print("warning: Too many arguments.")
    #print("usage: python decrypt.py <output_file> <passcode> <retrieved_file.txt>")
    #exit()
    #programul ruleaza in cazul in care numarul de argumente oferit este prea mare si foloseste doar primele 4 argumente date








operatie = sys.argv[0]
input_file = open(sys.argv[1], "rb")
cheie = sys.argv[2].encode('ascii')
output_file = open(sys.argv[3], "wb")


output_file.write( bytearray( [char ^ cParola for char, cParola in zip( input_file.read(), cycle(cheie) )] ))

