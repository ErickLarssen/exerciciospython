import math

class Exercicios:
    def __int__(self): #Construtor
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossível dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'{num1} * {i} = {num1 * i}\n'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

    def exercicio01(self):
        msg = ""
        for i in range(1,11,1):
            msg += f'\n{i}'
        return msg

    def exercicio02(self):
        pares = ""
        for i in range(1,21,1):
            if i % 2 == 0:
                pares += f'\n{i}'
        return pares

    def exercicio03(self):
        somar = 0
        for i in range(1,101,1):
            somar += i
        return somar

    def exercicio04(self):
        multiplos = ""
        for i in range(1,51,1):
            if i % 5 == 0:
                multiplos += f'\n{i}'
        return multiplos

    def exercicio05(self, num):
        if num % 2 == 0:
            return "par"
        else:
            return "impar"

    def exercicio06(self, num):
        if num <= 0:
            return "negativo"
        else:
            return "positivo"

    def exercicio07(self,num3):
        resul = ""
        for i in range(0, 11, 1):
            resul += f'{num3} * {i} = {num3 * i}\n'
        return resul

    def primos(self):
        primo = "1\n2\n3\n5"
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def ehprimo(self, num):
        if num == 2 or num == 3 or num == 5:
            return f'O {num} é primo!'
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return f'O {num} é primo!'
        return f'O {num} não é primo!'

    def exercicio08(self, num):
        contagem = ""
        for i in range(1,num+1,1):
            contagem += f'\n{i}'
        return contagem

    def exercicio09(self,num):
        somar = 0
        for i in range(1,num+1, 1):
            somar += i
        return somar

    def exercicio12(self, num):
        fatorial = num
        for i in range(1, num,1):
            fatorial *= num - 1
            num -= 1
        return fatorial

    def exercicio13(self):
        fib = 0
        fib1 = 1
        fib2 = 0
        resultado = f'\n{fib}\n{fib1}'
        for i in range(0, 10, 1):
            fib2 = fib + fib1
            resultado += f'\n{fib2}'
            fib = fib1
            fib1 = fib2

        return resultado

    def exercicio14(self, num):
        fib = 0
        fib1 = 1
        fib2 = 0

        for i in range(0, 1000, 1):
            fib2 = fib + fib1
            if fib == num:
                return "É fibonacci"
            fib = fib1
            fib1 = fib2
        return "Esse  número não é fibonacci"

    def exercicio15(self, num):
        soma = 0
        for i in range(1, num + num, 1):
            soma = i + 1
        return soma

    def exercicio16(self, num):
        resultado = ""
        for i in range(1, num,1):
            if i % 2 == 0:
                resultado += f'\nO {i} é par!'
            elif i % 2 == 1:
                resultado += f'\nO {i} é impar'
        return resultado

    def exercicio17(self, num):
        primo = "1\n2\n3\n5"
        for i in range(5, num, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def exercicio18(self, num):
        pares = ""
        impares = ""
        for i in range(1, num, 1):
            if i % 2 == 0:
                pares += f'\n{i / 2}'
            else:
                impares += f'\n{i * 3 + 1}'
        return f"A sequência de Collatz é: {pares} e\n {impares} "

    def exercicio19(self, num):
        par = 0
        impar = 0
        for i in range(1, num, 1):
            if i % 2 == 0:
                par += i
            elif i % 2 == 1:
                impar += i
        return f'Os pares são: {par} e os impares são: {impar}'

    def exercicio20(self, num):
        resposta = ""
        self.num = int(input('Informe um número: '))
        for i in range(1, self.num,1):
            if i % self.num == 0:
                resposta = resposta + 1
        if resposta == self.num:
            return f'O número {resposta} é um número perfeito'
        else:
            return f'O número {resposta - self.num} não é um número perfeito'

    def exercicio21(self, a, b, c, x):
        a = 10
        b = 20
        x = b
        a = b
        b = x
        return f'O número 10 agora é {b} e o número 20 agora é {a}'

    def exercicio22(self, num):
        num = int(input('Informe um número: '))
        num -= 1
        return f'O número anterior ao número digitado é {num}'

    def exercicio23(self, base, altura):
        retangulo = base * altura
        return f'A area do retângulo é: {retangulo}'

    def exercicio24(self, ano, mes, dia):
        ano = self.num = int(input('Informe o ano do seu nascimento: '))
        mes = self.num = int(input('Informe o mês do seu nascimento: '))
        dia = self.num = int(input('Informe o dia do seu nascimento: '))

        if mes < 1 or mes > 13:
            return f'Erro! Informe um número maior que zero e/ou menor que 12'
        mes = mes * 30
        ano = ano * 365
        dia = dia + mes + ano
        return f'A sua idade expressa em dias é {dia}'

    def exercicio25(self, eleitor, branco, nulo, valido, percentualBranco, percentualNulo, percentualValido):
        eleitor = self.num = int(input('Informe o total de eleitores: '))
        branco = self.num = int(input('Informe o total de votos brancos: '))
        nulo = self.num = int(input('Informe o total de votos nulos: '))
        valido = self.num = int(input('Informe o total de votos válidos: '))

        percentualBranco = branco/eleitor * 100
        percentualNulo = nulo/eleitor * 100
        percentualValido = valido/eleitor * 100

        return f'O número total de votos brancos representa {percentualBranco} do número total de eleitores: {eleitor}.' \
               f'O número total de votos nulos representa {percentualNulo} do número total de eleitores: {eleitor}' \
               f'O número total de votos válidos representa {percentualValido} do número total de eleitores: {eleitor}'

    def exercicio26(self, salarioAtual, percentualReajuste, reajuste, novoSalario):
        salarioAtual = int(input("Digite o salário atual do funcionário: R$ "))
        percentualReajuste = int(input("Digite o percentual de reajuste (%): "))

        reajuste = salarioAtual * (percentualReajuste / 100)
        novoSalario = salarioAtual + reajuste

        return f'O novo salário é {novoSalario}'

    def exercicio27(self, fabrica, porc, imposto, total):
        fabrica = int(input("Digite o valor do carro: "))

        porc = 28 * fabrica / 100
        imposto = 45 * fabrica / 100
        total = fabrica + imposto + porc

        return f'O preço final do seu veiculo é de {total}'

    def exercicio28(self, a, b, c, media):
        a = int(input("Digite a primeira nota: "))
        b = int(input("Digite a segunda nota: "))
        c = int(input("Digite a terceira nota: "))

        media = a + b + c / 3

        return f'A média final é: {media}'

















