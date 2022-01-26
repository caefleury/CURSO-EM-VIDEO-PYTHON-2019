print("-=" * 20 + "-")
print("     Analisador de triângulos ")
print("-=" * 20 + "-")

#      | b - c | < a < b + c

a = int(input("Primeiro segmento: "))
b = int(input("Segundo segmento: "))
c = int(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM formar um triângulo ", end= '')
    if a == b and b == c:
        print("EQUILÁTERO")
    elif a == b and b != c or b == c and c != a or a == c and b != a:
        print("ISÓSCELES")
    elif a != b != c != a:
        print("ESCALENO")

else:
    print("Os segmento acima NÃO PODEM FORMAR um triângulo")
# -------------------------------------------------------------------------#



