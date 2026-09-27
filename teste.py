import random

numerosImpares = []
numerosPares = []
numerosPrimos = []
numerosPerfeitos = []

def ehPar(numero):
	if (numero%2==0):
		return True
	else:
		return False

def ehPrimo(numero):
	qtdDivisores=0
	for i in range(1,numero+1):
		if(numero%i==0):
			qtdDivisores+=1
		if(qtdDivisores>2):
			break
	if qtdDivisores==2:
		return True
	else:
		return False

def ehPerfeito(numero):
	somaDivisores=0
	for i in range (1,numero):
		if(numero%i==0):
			somaDivisores+=i

	if somaDivisores==numero:
		return True
	else:
		return False

while True:
	n=random.randint(-1000,1000)
	if n==0:
		break
	elif ehPar(n):
		numerosPares.append(n)
	else:
		numerosImpares.append(n)
	if ehPrimo(n):
		numerosPrimos.append(n)
	if ehPerfeito(n):
		numerosPerfeitos.append(n)

with open("primos.txt","w") as arquivo:
	for primo in numerosPrimos:
		arquivo.write(str(primo)+"\n")

with open("pares.txt","w") as arquivo:
	for par in numerosPares:
		arquivo.write(str(par)+"\n")
	
with open("ímpares.txt","w") as arquivo:
	for impar in numerosImpares:
		arquivo.write(str(impar)+"\n")

with open("perfeito.txt","w") as arquivo:
	for perfeito in numerosPerfeitos:
		arquivo.write(str(perfeito)+"\n")
import random

numerosImpares = []
numerosPares = []
numerosPrimos = []
numerosPerfeitos = []


def merge_sort(vetor):
    if len(vetor) <= 1:
        return vetor

    meio = len(vetor) // 2
    esquerda = merge_sort(vetor[:meio])
    direita = merge_sort(vetor[meio:])

    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


def ehPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def ehPrimo(numero):
    qtdDivisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            qtdDivisores += 1

        if qtdDivisores > 2:
            break

    if qtdDivisores == 2:
        return True
    else:
        return False


def ehPerfeito(numero):
    somaDivisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            somaDivisores += i

    if somaDivisores == numero:
        return True
    else:
        return False


while True:
    n = random.randint(-1000, 1000)

    if n == 0:
        break
    elif ehPar(n):
        numerosPares.append(n)
    else:
        numerosImpares.append(n)

    if ehPrimo(n):
        numerosPrimos.append(n)

    if ehPerfeito(n):
        numerosPerfeitos.append(n)


# - - - - Ordenação dos Vetores por Merge Sort - - - - -

numerosPrimos = merge_sort(numerosPrimos)
numerosPares = merge_sort(numerosPares)
numerosImpares = merge_sort(numerosImpares)
numerosPerfeitos = merge_sort(numerosPerfeitos)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

with open("primos.txt", "w") as arquivo:
    for primo in numerosPrimos:
        arquivo.write(str(primo) + "\n")


with open("pares.txt", "w") as arquivo:
    for par in numerosPares:
        arquivo.write(str(par) + "\n")


with open("ímpares.txt", "w") as arquivo:
    for impar in numerosImpares:
        arquivo.write(str(impar) + "\n")


with open("perfeito.txt", "w") as arquivo:
    for perfeito in numerosPerfeitos:
        arquivo.write(str(perfeito) + "\n")
