def criarContas():
    contas = []
    for i in range(1, qtdPessoas + 1):
        print(f"Digite o número de contas a pagar da pessoa {i}: ")
        qtdContas = int(input())
        contas.append(qtdContas)
    return contas

def fila():
    contador = qtdPessoas
    posicao = 0
    while contador > 0:
        for i in range(0, qtdPessoas):
            if pessoas[i] > 0:
                print(f"A pessoa {i + 1} vai para o caixa com {pessoas[i]} contas.")
                print(f"Paga até {quantum} contas.")
                aux = pessoas[i] - quantum
                pessoas[i] = aux
                if aux <= 0:
                    print("E sai da fila.")
                    contador -= 1
                else:
                    print(f"E vai pro final da fila com {aux} contas.")
            posicao = (posicao + 1) % qtdPessoas

print("Digite o número máximo de contas a pagar no caixa (quantum): ")
quantum = int(input())
print("Digite o número de pessoas na fila: ")
qtdPessoas = int(input())
pessoas = criarContas()
fila()
print("Fim!")
