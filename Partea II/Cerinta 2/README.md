# Aflare parola

## Pasul 1: Aflarea lungimii parolei

- Vom aplica principiile invatate la distanta Hamming.

- Pentru fiecare lungime posibila a parolei ( 10 → 15 ) calculam suma distantelor Hamming intre oricare 2 siruri de acea lungime din fisierul output.

- Ulterior, lungimea cea mai probabila este cea unde suma distantelor Hamming este minima (cele mai putine diferente intre siruri). Acest lucru se datoreaza "armoniei" si structurii limbi romane. Ea nu este un sir de caractere aleatorii.

Implementam cele descrise atfel:

```python
min_hamming = 1000
for posibila_lungime in range(10,16):
    suma_hamming = 0
    n = len(lista_bytes) // posibila_lungime
    for x in range(n - 2):
        sir1 = "".join(lista_bytes[x * posibila_lungime: x * posibila_lungime + posibila_lungime])
        for y in range(x + 1, n - 1):
            sir2 = "".join(lista_bytes[y * posibila_lungime: y * posibila_lungime + posibila_lungime])
            distanta_hamming = 0
            for i in range(posibila_lungime):
                if sir1[i] != sir2[i]:
                    distanta_hamming += 1
            suma_hamming += distanta_hamming
    suma_hamming = suma_hamming / (n * (n - 1) // 2)
    if suma_hamming < min_hamming:
        min_hamming = suma_hamming
        lungime_cheie = posibila_lungime
    print(lungime_cheie)
```
Se afiseaza lungimea cea mai probabila, in cazul nostru 12.


## Pasul 2: Aflarea parolei

Construim 3 structuri ajutatoare:

- **valori_pozitie** care contine toate caracterele care sunt xorate cu elementul de pe pozitia x din parola

```python
valori_pozitie = []
for x in range(lungime_cheie):
    valori_pozitie += [set()]
    for y in range(x,len(lista_bytes),lungime_cheie):
        valori_pozitie[-1].add(chr(int(lista_bytes[y],2)))

```
- **caractere_parola** care contine toate caracterele care s-ar putea gasi in parola

```python
caractere_parola = [chr(x) for x in range(ord('a'),ord('z') + 1)]
caractere_parola += [chr(x) for x in range(ord('A'),ord('Z') + 1)]
caractere_parola += [chr(x) for x in range(ord('0'), ord('0') + 10)]

```

- **rezultat** care contine toate caracterele care se pot regasi in fisierul input.txt

```python
rezultat = caractere_parola + [',', '"', ':', '.', '!', ';', ' ', "'", '\n', '-', '?', ')', '(', chr(9)]

```

Pentru fiecare pozitie din parola vom avea o lista de caractere care posibile. Consideram ca un anumit caracter nu poate fi pe pozitia x in parola atunci cand un element din lista **valori_pozitie\[x]** xorat cu acel posibil caracter rezulta un caracter ce nu s-ar putea gasi in input.txt ( nu se afla in lista **rezultat** ).

```python
dict_posibile_caractere = {}
for x in range(lungime_cheie):
    dict_posibile_caractere[x] = []
    for posibil_caracter in l:
        ok = 1
        for caracter in dict[x]:
            rez = ord(caracter) ^ ord(posibil_caracter)
            if chr(rez) not in rezultat:
                ok = 0
                break
        if ok:
            dict_posibile_caractere[x] += [posibil_caracter]

print(dict_posibile_caractere)

```
Dictionarul afisat va contine doar caracterele posibile pentru fiecare pozitie din parola.

Output: {0: \['A'], 1: \['2'], 2: \['5'], 3: \['o'], 4: \['b'], 5: \['j'], 6: \['8'], 7: \['8'], 8: \['E'], 9: \['f'], 10: \['2'], 11:\['1']}

## Final

Am fost norocosi! Nu avem decat o singura posibilitate pentru fiecare pozitie!

Parola este: **A25obj88Ef21**

Daca am fi avut alte cateva posibilitati le-am fi putut verifica manual daca xorand fisierul output cu acele parole pe rand. (Algoritmul din [prima parte](https://github.com/Pepi100/Criptare-XOR) a proiectului 


