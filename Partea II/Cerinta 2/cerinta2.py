text_criptat = open("output_baieti.txt", 'r').read()

lista_bytes = [text_criptat[8*i:8*i+8] for i in range(len(text_criptat)//8)]

#############################################lungimea parolei:
# min_hamming = 1000
# for posibila_lungime in range(10,16):
#     suma_hamming = 0
#     n = len(lista_bytes) // posibila_lungime
#     for x in range(n - 2):
#         sir1 = "".join(lista_bytes[x * posibila_lungime: x * posibila_lungime + posibila_lungime])
#         for y in range(x + 1, n - 1):
#             sir2 = "".join(lista_bytes[y * posibila_lungime: y * posibila_lungime + posibila_lungime])
#             distanta_hamming = 0
#             for i in range(posibila_lungime):
#                 if sir1[i] != sir2[i]:
#                     distanta_hamming += 1
#             suma_hamming += distanta_hamming
#     suma_hamming = suma_hamming / (n * (n - 1) // 2)
#     if suma_hamming < min_hamming:
#         min_hamming = suma_hamming
#         lungime_cheie = posibila_lungime
#     print(lungime_cheie)
#############################################


lungime_cheie = 12



# valori_pozitie contine toate caracterele care sunt xorate cu elementul de pe pozitia x din parola

valori_pozitie = []
for x in range(lungime_cheie):
    valori_pozitie += [set()]
    for y in range(x,len(lista_bytes),lungime_cheie):
        valori_pozitie[-1].add(chr(int(lista_bytes[y],2)))


# caractere_parola contine toate caracterele care s-ar putea gasi in parola

caractere_parola = [chr(x) for x in range(ord('a'),ord('z') + 1)]
caractere_parola += [chr(x) for x in range(ord('A'),ord('Z') + 1)]
caractere_parola += [chr(x) for x in range(ord('0'), ord('0') + 10)]


# rezultat contine toate caracterele care se pot regasi in fisierul input.txt

rezultat = caractere_parola + [',', '"', ':', '.', '!', ';', ' ', "'", '\n', '-', '?', ')', '(', chr(9)]



dict_posibile_caractere = {}
for x in range(lungime_cheie):
    dict_posibile_caractere[x] = []
    for posibil_caracter in caractere_parola:
        ok = 1
        for caracter in valori_pozitie[x]:
            rez = ord(caracter) ^ ord(posibil_caracter)
            if chr(rez) not in rezultat:
                ok = 0
                break
        if ok:
            dict_posibile_caractere[x] += [posibil_caracter]

print(dict_posibile_caractere)