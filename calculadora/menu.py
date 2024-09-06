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
                  'Escolha uma das opções abaixo: ' +
                  '\n0. Sair'                       +
                  '\n1. Somar'                      +
                  '\n2. Subtrair'                   +
                  '\n3. Dividir'                    +
                  '\n4. Multiplicar'                +
                  '\n5. Potência'                   +
                  '\n6. Raiz'                       +
                  '\n7. Tabuada')

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