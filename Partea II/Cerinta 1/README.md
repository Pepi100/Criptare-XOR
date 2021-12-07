# Aflare parola

Stim ca:

x ⊕ x = 0

output = input ⊕ parola

Astfel:

input ⊕ output = input ⊕ input ⊕ parola = parola

Pentru a afla parola echipei adverse trebuie doar sa xoram fisierele input.txt si output.txt.

Convertim fisierul output.txt format din caracterele 1 si 0 intr-o lista de numere pentru a putea xora:

```python
   caractere_text_criptat = [int(text_criptat[8*i:8*i+8], 2) for i in range(30)]
```

Cunoastem faptul ca parola are maximum 15 caractere, deci este necesar sa xoram doar primele 30 pentru a identifica secventa care se repeta si a gasi parola:

```python
   print("".join([chr(ord(text_initial[x]) ^ caractere_text_criptat[x]) for x in range(30)]))
```
   Output: A25obj88Ef21A25obj88Ef21A25obj

Parola este: **A25obj88Ef21**