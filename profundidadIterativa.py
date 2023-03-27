import random
class Pancakes:
	def __init__(self, pancakes):
		self.pancakes = pancakes
		self.orden = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
		self.profundidad = 1
	
	def voltear(self, posicion, pancakes):
		return pancakes[0:len(pancakes)-posicion] + pancakes[len(pancakes)-posicion:len(pancakes)][::-1]

	def busqProfundidad(self, nodo, ant):
		if nodo == self.orden[0:len(nodo)]:
			return " ".join(ant[1:])
		if len(ant)-1 >= self.profundidad:
			return -1 
		for i in range(2, len(nodo)+1):
			if str(i) == ant[-1]:
				continue 
			nodo_volt = self.voltear(i,nodo)
			resultado = self.busqProfundidad(nodo_volt, ant + [str(i)])
			if resultado != -1:
				break
		return resultado
	
	def busqProfundidadIte(self, nodo):
		while True:
			resultado = self.busqProfundidad(nodo, ["0"])
			if resultado == -1:
				self.profundidad += 1
			else:
				return resultado

pancakes = ["a", "b", "c", "d", "e", "f"]
random.shuffle(pancakes)
prueba = Pancakes(pancakes)
print(f"Pancakes inicio: {pancakes}")
print(prueba.busqProfundidadIte(pancakes))
