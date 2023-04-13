
estadoInicial = 0
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digitos = "0123456789"
oper = "+-"
ponto = '.'

def verificarCaractere(c, vetor):
    i = 0
    while i < len(vetor):
        if vetor[i] == c:
            return True
        i += 1
    return False

def ler_Cadeia(estadoAtual, elementoAtualCadeia):
    global estadoInicial, letras, digitos, oper, ponto 

    if estadoAtual == 0:
        if verificarCaractere(elementoAtualCadeia, digitos):
            return 1
        elif verificarCaractere(elementoAtualCadeia, oper):
            return -1
    elif estadoAtual == -1:
        if verificarCaractere(elementoAtualCadeia, digitos):
            return 1
        elif verificarCaractere(elementoAtualCadeia, letras):
            return 0
    elif estadoAtual == 1:
        if verificarCaractere(elementoAtualCadeia, digitos):
            return 1
        elif verificarCaractere(elementoAtualCadeia, oper) or verificarCaractere(elementoAtualCadeia, letras):
            return -2
        elif elementoAtualCadeia == ponto:
            return 2
    elif estadoAtual == 2:
        if verificarCaractere(elementoAtualCadeia, digitos):
            return 3
        elif verificarCaractere(elementoAtualCadeia, oper) or verificarCaractere(elementoAtualCadeia, letras) or elementoAtualCadeia == ponto:
            return 0
    elif estadoAtual == 3:
        if verificarCaractere(elementoAtualCadeia, digitos):
            return 3
        elif verificarCaractere(elementoAtualCadeia, oper) or verificarCaractere(elementoAtualCadeia, letras) or elementoAtualCadeia == ponto:
            return -3

def Automato(cadeia):

    global estadoInicial

    tamCadeia = len(cadeia)
    estadoAtual = estadoInicial
    padraoNumInt = 0
    padraoNumReal = 0

    for i in range(tamCadeia):
        if verificarCaractere(cadeia[i], digitos) or verificarCaractere(cadeia[i], oper) or verificarCaractere(cadeia[i], letras) or cadeia[i] == ponto:
            estadoAtual = ler_Cadeia(estadoAtual, cadeia[i])
        
        if estadoAtual == -2:
            padraoNumInt += 1
            estadoAtual = 0
            
            i -= 1
        if estadoAtual == -3:
            padraoNumReal += 1
            estadoAtual = 0
            
            i -= 1
        
        if i == tamCadeia - 1:
            if estadoAtual == 1:
                padraoNumInt += 1
            elif estadoAtual == 3:
                padraoNumReal += 1
    
    print("\nEstado ATUAL: ", estadoAtual)
    print("PADROES para numeros inteiros encontrados: ", padraoNumInt)
    print("Padrão para numeros reais: ", padraoNumReal)

def main():
    cadeia =  str(input("Digite a cadeia: "))

    Automato(cadeia)

main()