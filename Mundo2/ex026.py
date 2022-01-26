print("Digite uma frase: ")
frase = input().lower().strip()
f = frase.replace(" ","")

# ---------------- variables ------------

count = f.count("a")
first = f.find("a")
last = frase.rfind("a")

# ------------------ start --------------

if count == 1:
    print("A letra 'a' aparece {} vez".format(count))
elif count != 1 :
    print("A letra 'a' aparece {} vezes".format(count))

# ------------------ finish -------------

print("A primeira letra 'a' aparece na posição", str(first + 1))

print("A última letra 'a' aparece na posição", str(last + 1))