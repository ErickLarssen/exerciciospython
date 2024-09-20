from exercicios import Exercicios

class Menu:
        def __init__(self):
            self.opcao = -1
            self.exer = Exercicios()
            self.num1 = 0
            self.num2 = 0

        def mostrarMenu(self):
            print('\n ----MENU----\n\n' +
                  'Escolha uma das opções abaixo: ' +
                  '\n0. Sair' +
                  '\n1. Somar' +
                  '\n2. Subtrair' +
                  '\n3. Dividir' +
                  '\n4. Multiplicar' +
                  '\n5. Potência' +
                  '\n6. raiz' +
                  '\n7. Tabuada' +
                  '\n8. Exercicio 01' +
                  '\n9  Exercicio 02' +
                  '\n10 Exercicio 03' +
                  '\n11 Exercicio 04' +
                  '\n12 Exercicio 05' +
                  '\n13 Exercicio 06' +
                  '\n14 Exercicio 07' +
                  '\n15 Exercicio primos' +
                  '\n16 Exercicio ehprimo' +
                  '\n17 Exercicio 08' +
                  '\n18 Exercicio 09' +
                  '\n19 Exercicio 12' +
                  '\n20 Exercicio 13' +
                  '\n21 Exercicio 14' +
                  '\n22 Exercicio 15' +
                  '\n23 Exercicio 16' +
                  '\n24 Exercicio 17' +
                  '\n25 Exercicio 18' +
                  '\n26 Exercicio 19' +
                  '\n27 Exercício 20' +
                  '\n28 Exercício 21' +
                  '\n29 Exercício 22' +
                  '\n30 Exercício 23' +
                  '\n31 Exercício 24' +
                  '\n32 Exercício 25' +
                  '\n33 Exercício 26' +
                  '\n34 Exercício 27' +
                  '\n35 Exercício 28')

        def coletar(self):
            self.num1 = int(input("Informe o primeiro número: "))
            self.num2 = int(input("Informe o segundo número: "))

        def operacao(self):
            while self.opcao != 0:
                self.mostrarMenu()  # Chamando as opções
                self.opcao = int(input('Escolha uma das opções acima:'))

                if self.opcao == 0:
                    print('Obrigado!')

                elif self.opcao == 1:
                    self.coletar()  # Chamando o  input por meio do coletar
                    print(f'A soma dos números digitados é: {self.exer.somar(self.num1, self.num2)}')

                elif self.opcao == 2:
                    self.coletar()
                    print(f'A subtração dos números digitados é: {self.exer.subtrair(self.num1, self.num2)}')

                elif self.opcao == 3:
                    self.coletar()
                    print(f'A multiplicação dos números digitados é: {self.exer.multiplicar(self.num1, self.num2)}')

                elif self.opcao == 4:
                    self.coletar()
                    print(f'A divisão dos números digitados é: {self.exer.dividir(self.num1, self.num2)}')

                elif self.opcao == 5:
                    self.coletar()
                    print(f'A potência dos números digitados é: {self.exer.potencia(self.num1, self.num2)}')

                elif self.opcao == 6:
                    self.coletar()
                    print(f'A raiz de {self.num1} é: {self.exer.raiz(self.num1)}')
                    print(f'A raiz de {self.num2} é: {self.exer.raiz(self.num2)}')

                elif self.opcao == 7:
                    self.coletar()
                    print(f'A tabuada de {self.num1} é: {self.exer.tabuada(self.num1)}')
                    print(f'A tabuada de {self.num2} é: {self.exer.tabuada(self.num2)}')

                elif (self.opcao == 8):
                    print(self.exer.exercicio01())


                elif (self.opcao == 9):
                    print(self.exer.exercicio02())

                elif (self.opcao == 10):
                    print(self.exer.exercicio03())

                elif (self.opcao == 11):
                    print(self.exer.exercicio04())


                elif self.opcao == 12:
                    num = int(input('Informe um número: '))
                    print(f'O número é: {self.exer.exercicio05(num)}')


                elif self.opcao == 13:
                    num = int(input('Informe um número: '))
                    print(f'O número é: {self.exer.exercicio06(num)}')


                elif self.opcao == 14:
                    num = int(input('Informe um número: '))
                    print(f'A tabuada de {num} é: {self.exer.exercicio07(num)}')


                elif self.opcao == 15:
                    print(self.exer.primos())


                elif self.opcao == 16:
                    num = int(input("Informe um número: "))
                    print(self.exer.ehprimo(num))


                elif self.opcao == 17:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio08(num))


                elif self.opcao == 18:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio09(num))


                elif self.opcao == 19:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio12(num))


                elif self.opcao == 20:
                    print(self.exer.exercicio13())


                elif self.opcao == 21:
                    num = int(input("Informe um número"))
                    print(self.exer.exercicio14(num))


                elif self.opcao == 22:
                    num = int(input("Informe um número"))
                    print(self.exer.exercicio15(num))


                elif self.opcao == 23:
                    num = int(input("Informe um número"))
                    print(self.exer.exercicio16(num))


                elif self.opcao == 24:
                    num = int(input("Informe um número"))
                    print(self.exer.exercicio17(num))


                elif self.opcao == 25:
                    num = int(input("Informe um número: "))
                    print(self.exer.exercicio18(num))


                elif self.opcao == 26:
                    num = int(input("Informe um número"))
                    print(self.exer.exercicio19(num))

                elif self.opcao == 27:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio20(num))

                elif self.opcao == 28:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio21(num))

                elif self.opcao == 29:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio22(num))

                elif self.opcao == 30:
                    altura = int(input("Informe a altura do retângulo: "))
                    base = int(input("Informe a base do retângulo: "))
                    print(self.exer.exercicio23(base, altura))

                elif self.opcao == 31:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio24(num))

                elif self.opcao == 32:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio25(num))

                elif self.opcao == 33:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio26(num))

                elif self.opcao == 34:
                    num = int(input('Informe um número'))
                    print(self.exer.exercicio27(num))

                elif self.opcao == 35:
                    num = int(input('Informe um numero'))
                    print(self.exer.exercicio28(num))

                else:

                    print("Codigo escolhido não é valído!")

