import random
 
letras = []
list1 = ["handa","hola","bueno","chau","gato","perro"]
mostrar = "palabra: "
correctas = []
incorrectas = []
palabra = random.choice(list1)
def continar():
	letra = input("Elige una letra: ").lower()
	mostrar = "palabra: "
	i = 0
	global palabra
	global letras
	global correctas
	acerto = 0
	if letra == "apaga":
		return
	for y in palabra:
		if y == letra:
			mostrar = mostrar + y+" "
			acerto = 1
			existe = 0
			for r in correctas:
				if r == y:
					existe = 1
					break
			if existe == 0:
				correctas.append(y)
		else:
			correcta = 0
			if len(correctas) > 0:
				for x in correctas:
					if x == y:
						correcta = 1
				if correcta == 1:
					mostrar = mostrar + y+" "
				else:
					mostrar = mostrar + "_ "
			else:
				mostrar = mostrar + "_ "
	if len(incorrectas) > 5:
		print("Has perdido la palabra era "+ palabra)
		return
	if acerto == 0:
		incorrectas.append(letra)
	incorrecta = 0
	for x in palabra:
		correcta = 0
		for y in correctas:
			if x == y:
				correcta = 1
		if correcta == 0:
			break

	if correcta == 1:
		print("Has ganado la palabra era " + palabra)
		return
	else:
		print(mostrar)
	mostrar = "incorrectas: "
	if len(incorrectas) > 0:
		for x in incorrectas:
			mostrar = mostrar + " " + x
	print(mostrar)
	continar()

continar()
