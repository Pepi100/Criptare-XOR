text = list(open("input.txt").read())
iesire = open("output", 'w')
parola = input()
for x in range(len(text)):
    text[x] = chr(ord(text[x]) ^ ord(parola[x % len(parola)]))
print("".join(text), file=iesire)