# # mix = [0, 1.0, "dos", 3+4]

# # for i in mix:
# #     print(f"{i:6} - Tipo: {type(i)}")

# # print (len(mix))

# # sin_dos = mix[:2] + mix[3:]
# # print(mix, sin_dos)

# # duplicado = mix*2
# # print(duplicado)

# cuadrados= [0,1,4,9,16,25,36]
# for i in range(len(cuadrados)):
#     cuadrados[i]= cuadrados[i]*i
#     print(f"{i}**3 = {cuadrados[i]}")

# # cuadrados.append(7**3)
# # print(cuadrados)

# # cuadrados.insert(6, 6**3)
# # print(cuadrados)

# # cuadrados.extend({27,1000, -1})
# # print(cuadrados)

# # cuadrados.extend(range(-1,-4,-1))
# # print(cuadrados)

# # del cuadrados[9:]
# # print(cuadrados)

# # cuadrados.remove(27) #remueve un valor y no lo regresa
# # print(cuadrados)

# # cuadrados.pop(2) # remueve un indice y regresa valor
# # print(cuadrados)

# # cuadrados.clear()
# # print(cuadrados)

# vocales = ["a","e","i","o","u"]
# vocales[1:4]= ["E","I","O"]

# print(vocales, len(vocales))

# vocales[1:4]=[]
# print(vocales, len(vocales))

# vocales.extend(["i","i"])

# print(vocales.index("i"))

# print(vocales.count("i"))

# print(vocales.index("i", 3))

# vocales.reverse()
# print(vocales, len(vocales))

# vocales.sort()
# print(vocales, len(vocales))

# carros= ["Audi","Ford","BMW","VW"]
# carros.sort(key=len)
# print(carros)


# listas=[[0,1],[2,3,4],[5,6]]
# print(listas[0],listas[1:3]) #Esta forma de expresión no abarca hasta el numero 3

# print(listas[2][1])

# x=[3,2.5,6,6.3]

# vocales1 = ["a","e","i","o","u"]
# vocales2=vocales1

# print(vocales1,vocales2)
# print(id(vocales1),id(vocales2))

# vocales3=vocales1.copy

# print(vocales1,vocales3)
# print(id(vocales1),id(vocales3))
# print(id(vocales1[2]),id(vocales2[2]))
# print(id(vocales1[2]),id(vocales3[2]))

# del vocales1[2]
# print (vocales1,vocales2,vocales3)
