text_initial = open("input_baieti.txt", 'r').read()
text_criptat = open("output_baieti.txt", 'r').read()

caractere_text_criptat = [int(text_criptat[8*i:8*i+8], 2) for i in range(30)]

print("".join([chr(ord(text_initial[x]) ^ caractere_text_criptat[x]) for x in range(30)]))