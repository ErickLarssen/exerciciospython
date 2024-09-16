from operacao import Operacao

class Menu:
        def __init__(self):
            self.opcao = -1
            self.opera = Operacao()
            self.opera = Operacao()
            self.num1 = 0
            self.num2 = 0

        def mostrarMenu(self):
            print('\n---- MENU ----\n\n' +
                  'Escolha uma das opções abaixo: '  +
                  '\n0. Sair'                        +
                  '\n1. Somar'                       +
                  '\n2. Subtrair'                    +
                  '\n3. Dividir'                     +
                  '\n4. Multiplicar'                 +
                  '\n5. Potência'                    +
                  '\n6. Raiz'                        +
                  '\n7. Tabuada'                     +
                  '\n8. Exercício 1'                 +
                  '\n9. Exercício 2'                 +
                  '\n10. Exercício 3'                +
                  '\n11. Exercício 4'                +
                  '\n12. Exercício 5'                +
                  '\n13. Exercício 6'                +
                  '\n14. Exercício 7'                +
                  '\n15. Exercício 8'                +
                  '\n16. Exercício 9'                +
                  '\n17. Exercício 10'               +
                  '\n18. Exercício 11'               +
                  '\n19. Exercício 12'               +
                  '\n20. Exercício 13'               +
                  '\n21. Exercício 14'               +
                  '\n22. Exercício 15'               +
                  '\n23. Exercício 16'               +
                  '\n24. Exercício 17'               +
                  '\n25. Exercício 18'               +
                  '\n26. Exercício 19'               +
                  '\n27. Exercício 20'               +
                  '\n28. Exercício 21'
                  )

        def coletar(self):
            num1 = int(input('Informe o primeiro número'))
            num2 = int(input('Informe o segundo número'))

        def execucao(self):
            while self.opcao !=0:
                self.mostrarMenu()  #Chamando as opções
                self.opcao = int(input('Escolha uma das opções acima: '))
                if self.opcao == 0:
                    print('Obrigado!!!')
                if self.opcao == 1:
                    self.coletar()#Chamando o input
                    print(f'A soma dos números digitados é: {self.opera.somar(self.num1, self.num2)}')
                elif self.opcao == 2:
                    self.coletar()
                    print(f'A subtração dos números digitados é: {self.opera.subtrair(self.num1, self.num2)}')
                elif self.opcao == 3:
                    self.coletar()
                    print(f'A divisão dos números digitados é: {self.opera.dividir(self.num1, self.num2)}')
                elif self.opcao == 4:
                    self.coletar()
                    print(f'A multiplicação dos números digitados é: {self.opera.multiplicar(self.num1, self.num2)}')
                elif self.opcao == 5:
                    self.coletar()
                    print(f'A potencia dos núeros digitados é: {self.opera.potencia(self.num1, self.num2)}')
                elif self.opcao == 6:
                    self.coletar()
                    print(f'A raiz de {self.num1} números digitados é: {self.opera.raiz(self.num1)}')
                    print(f'A raiz de {self.num2} números digitados é: {self.opera.raiz(self.num2)}')
                elif self.opcao == 7:
                    self.coletar()
                    print(f'A tabuada de {self.num1} é: {self.opera.tabuada(self.num1)}')
                    print(f'A tabuada de {self.num2} é: {self.opera.tabuada(self.num2)}')

                elif self.opcao == 8:
                    self.coletar()
                    print(f'Os números são: {self.opera.exercicio1(self.num)}')

                elif (self.opcao == 8):
                    print(self.opera.exercicio01())

                elif (self.opcao == 9):
                    print(self.opera.exercicio02())

                elif (self.opcao == 10):
                    print(self.opera.exercicio03())

                elif (self.opcao == 11):
                    print(self.opera.exercicio04())

                elif self.opcao == 12:
                    num = int(input('Informe um número: '))
                    print(f'O número é: {self.opera.exercicio05(num)}')

                elif self.opcao == 13:
                    num = int(input('Informe um número: '))
                    print(f'O número é: {self.opera.exercicio06(num)}')

                elif self.opcao == 14:
                    num = int(input('Informe um número: '))
                    print(f'A tabuada de {num} é: {self.opera.exercicio07(num)}')

                elif self.opcao == 17:
                    num = int(input('Informe um número'))
                    print(self.opera.exercicio08(num))

                elif self.opcao == 18:
                    num = int(input('Informe um número'))
                    print(self.opera.exercicio09(num))

                elif self.opcao == 19:
                    print(self.opera.exercicio10())

                elif self.opcao == 20:
                    num = int(input("Informe um número: "))
                    print(self.opera.exercicio11(num))

                elif self.opcao == 21:
                    num = int(input('Informe um número'))
                    print(self.opera.exercicio12(num))

                elif self.opcao == 22:
                    num = int(input('Informe um número'))
                    print(self.opera.exercicio13(num))

                elif self.opcao == 23:
                    print(self.opera.exercicio21(num))

                elif self.opcao == 24:
                    num = int(input('Informe um número'))
                    print(self.opera.exercicio22(num))

                elif self.opcao == 25:
                    num = int(input('Informe um número'))
                    print(self.opera.exercicio23(num))

                elif self.opcao == 26:
                    num = int(input('Informe um número'))
                    print(self.opera.exercicio24(num))

                elif self.opcao == 27:
                    num = int(input('Informe um número'))
                    print(self.opera.exercicio25(num))

                elif self.opcao == 28:
                    num = int(input('Informe um número'))
                    print(self.opera.exercicio26(num))

                else:
                    print("Codigo escolhido não é valído!")

