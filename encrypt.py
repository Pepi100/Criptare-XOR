import sys
from itertools import cycle

if len(sys.argv) < 4:
    print("fatal: Missing arguments.")
    print("usage: python encrypt.py <passcode> <retrieved_file.txt> <output_file>")
    exit()

if len(sys.argv) > 4:
    print("warning: Too many arguments.")
    # print("usage: python encrypt.py <passcode> <retrieved_file.txt> <output_file>")
    # exit()
    # programul ruleaza in cazul in care numarul de argumente oferit este prea mare si foloseste doar primele 4 argumente date

operatie = sys.argv[0]
cheie = (sys.argv[1]).encode('ascii')
input_file = open(sys.argv[2], "rb")
output_file = open(sys.argv[3], "wb")


output_file.write(bytearray([char ^ cParola for char, cParola in zip(input_file.read(), cycle(cheie))]))
