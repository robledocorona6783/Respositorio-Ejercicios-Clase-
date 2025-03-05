# canasta={"manzana", "naranja", "manzana", "pera", "naranja", "platano"}
# print(canasta)
# print("manzana" in canasta)
# print("melon" in canasta)

vocales=["a","e","i","o","u","a"]

vocales=list(set(vocales))

print(vocales)

# vocales1={"a","e","i","o","u","a"}
# vocales2={"e","i","u"}
# print(vocales2.issubset(vocales1))

vocales3={"a","e","i","o","u"}
vocales4={"A","E","I","O","U","u"}
print(vocales3 - vocales4)
print(vocales3 | vocales4)
print(vocales3 & vocales4)
print(vocales3 ^ vocales4 )