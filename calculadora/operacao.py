import math

class Operacao:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2) #utilizando o método "coletar"
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
            resultado += f'\n{num1} * {i} = {num1*i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

    def exercicio01(self):
        msg = ""
        for i in range(1, 11, 1):
            msg += f'\n{i}'
        return msg

    def exercicio02(self):
        pares = ""
        for i in range(1, 21, 1):
            if i % 2 == 0:
                pares += f'\n{i}'
        return pares

    def exercicio03(self):
        somar = 0
        for i in range(1, 101, 1):
            somar += i
        return somar

    def exercicio04(self):
        multiplos = ""
        for i in range(1, 51, 1):
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

    def exercicio07(self, num3):
        resul = ""
        for i in range(0, 11, 1):
            resul += f'{num3} * {i} = {num3 * i}\n'
        return resul

    def exercicio08(self, num):
        contagem = ""
        for i in range(1, num + 1, 1):
            contagem += f'\n{i}'
        return contagem

    def exercicio09(self, num):
        somar = 0
        for i in range(1, num + 1, 1):
            somar += i
        return somar

    def exercicio10(self):
        primo = "1\n2\n3\n5"
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def exercicio11(self, num):
        if num == 2 or num == 3 or num == 5:
            return f'O {num} é primo!'
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return f'O {num} é primo!'
        return f'O {num} não é primo!'

    def exercicio12(self, num):
        fatorial = num
        for i in range(1, num, 1):
            fatorial *= num - 1
            num -= 1
        return fatorial

    def exercicio013(self):
        fib = 0
        fib1 = 1
        fib2 = 0
        resultado = f'\n{fib}\n{fib1}'
        for i in range(0, 10, 1):
            fib2 = fib + fib1
            resultado += f'\n{fib2}'
            fib = fib1
            fib1 = fib2

    def exercicio18(self):
        resposta = 0
        contar = ""
        self.num = int(input('Informe um número: '))
        while self.num > 1:
            if self.num % 2 == 0:
                self.num = self.num / 2
                contar = f'\n{self.num}'
            else:
                self.num = 3 * self.num + 1
                resposta += 1
                contar = f'\n{self.num}'
            return f'{contar}\nresultado: {resposta}'

    def exercicio19(self):
        par = 0
        impar = 0
        self.num = int(input('Informe um número: '))
        for i in range (1, self.num,1):
            if i % 2 == 0:
                par += i
            else:
                impar = i + impar
        return f'A soma dos pares é: {par}\nA soma dos ímpares é: {impar}'

    def exercicio20(self):
        resposta = ""
        self.num = int(input('Informe um número: '))
        for i in range(1, self.num,1):
            if i % self.num == 0:
                resposta = resposta + 1
        if resposta == self.num:
            return f'O número {resposta} é um número perfeito'
        else:
            return f'O número {resposta - self.num} não é um número perfeito'

    def exercicio21(self):
        a = 10
        b = 20
        x = b
        a = b
        b = x
        return f'O número 10 agora é {b} e o número 20 agora é {a}'

    def exercicio22(self):
        num = int(input('Informe um número: '))
        num -= 1
        return f'O número anterior ao número digitado é {num}'

    def exercicio23(self):
        base = self.num = int(input('Informe a base: '))
        altura = self.num = int(input('Informe a altura: '))

        area = base * altura

        return f'A área do retângulo é: {area}'

    def exercicio24(self):
        ano = self.num = int(input('Informe o ano do seu nascimento: '))
        mes = self.num = int(input('Informe o mês do seu nascimento: '))
        dia = self.num = int(input('Informe o dia do seu nascimento: '))

        if mes < 1 or mes > 13:
            return f'Erro! Informe um número maior que zero e/ou menor que 12'
        mes = mes * 30
        ano = ano * 365
        dia = dia + mes + ano
        return f'A sua idade expressa em dias é {dia}'

    def exercicio25(self):
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

    def exercicio26(self):
        salarioAntigo =  self.num = int(input('Informe o salário atual: '))
        percentualReajuste = self.num = int(input('Informe o percentual de reajuste: '))

        salarioNovo = salarioAntigo / percentualReajuste * percentualReajuste

        return f'O novo salário é {salarioNovo}'













