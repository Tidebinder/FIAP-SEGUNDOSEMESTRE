import math
# Exercicio 1
numeros_inteiros = (15,24,32,47,120,1000,203,102,10,25,2,1,5,6,69)

# Exercicio 2
for index,numero in enumerate(numeros_inteiros):
    print(f"{index+1} - {numero}")

print("___________________________________________________")

#Exercicio 3
def achar_maior_numero(numeros:tuple) -> int:

    return max(numeros)

maior_numero = achar_maior_numero(numeros_inteiros)

print(f"\nO maior numero entre os inteiros é: {maior_numero}")

numeros_reais = (1,2,3.5,2.3,1.323432323,12.3123123,3.3433430983984,3.1415926535897932384626)

#Exercicio 4
def media_aritmedica(valores:tuple) -> int:
    
    media = sum(valores)/len(valores)

    return media

print(f"Media Aritmedica: {media_aritmedica(numeros_reais)}")

def desvioPadrao(valores:tuple) -> int:
    
    media = media_aritmedica(valores)
    
    dps = []
    
    for valor in valores:

        varianca = (valor - media)**2

        print(varianca)

        dps.append(varianca)

    dp = math.sqrt(sum(dps)/len(valores))    
        
    return dp

atletas = (1.80,1.95,1.98,1.88,2.04)

print(desvioPadrao(atletas))
