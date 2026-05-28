print("=== CALCULADORA PYTHON ===")

while True:

    try:

        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        print("\nEscolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        opcao = input("Digite a opção: ")

        if opcao == "1":
            resultado = numero1 + numero2
            print(f"\nResultado: {resultado}")

        elif opcao == "2":
            resultado = numero1 - numero2
            print(f"\nResultado: {resultado}")

        elif opcao == "3":
            resultado = numero1 * numero2
            print(f"\nResultado: {resultado}")

        elif opcao == "4":

            if numero2 == 0:
                print("\nErro: divisão por zero não é permitida.")

            else:
                resultado = numero1 / numero2
                print(f"\nResultado: {resultado}")

        else:
            print("\nOpção inválida.")

    except ValueError:
        print("\nErro: digite apenas números.")

    continuar = input("\nDeseja continuar? (s/n): ").lower()

    if continuar != "s":
        print("\nCalculadora encerrada.")
        break