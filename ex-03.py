class Funcionario:
    def __init__(self, nome, horas, valor, salario):
        self.nome = nome
        self.horas = horas
        self.valor = valor
        self.salario = salario
    def __str__(self):
        return f"Olá {self.nome}, seu salário é {self.salario} reais, você trabalha {self.horas} horas por dia e recebe {self.valor} por dia"
meu_funcionario = Funcionario(
    nome= 'Joana',
    horas= 8,
    valor= 8.3,
    salario= 2000
) 
print(meu_funcionario)