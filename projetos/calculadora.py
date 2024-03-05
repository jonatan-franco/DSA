# boas-vindas
print("******Seja Bem-vinda(o) à Cálculadora Python******")
print("\nSelecione a opção da operação que deseja realizar: ","\nA) Soma \nB) Subtração \nC) Multplicação \nD) Divisão ")

#input
opcao_operacao = input("\nDigite sua opção(A/B/C/D): ")

# caso o input seja erroneamente um numero
if not opcao_operacao.isalpha():
    print("Você digitou um número! Por favor, troque para letra!")

# caso nao, dê prosseguimento
else:
    val1 = int(input("Digite o primeiro valor: "))
    val2 = int(input("Digite o segundo valor: "))  
if opcao_operacao == "a" or opcao_operacao == "A" :
    print("\nO seu resultado é:", val1+val2)
elif opcao_operacao == "b" or opcao_operacao == "B":
    print("\nO seu resultado é: ", val1-val2)
elif opcao_operacao == "c" or opcao_operacao == "C":
    print("\nO seu resultado é: ", val1*val2)
else:
    print("\nO seu resultado é: ", float(val1/val2))
