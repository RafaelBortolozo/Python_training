# comments
#*****************************#
letter = "C" ; print(letter)

ou

letter = "C"
print(letter)

#*****************************#

name = "Beau"
number = int("20")
print(isinstance(name, str)) # true
print(isinstance(name, int)) # false

#*****************************#

1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
5 // 2 #2
a = 1
b = 2

a == b #false
a != b #true
a > b #false
a < b #true

0 or 1 #1
False or 'hey' #'hey'
'hi' or 'hey' #'hi'
[] or False #False
False or [] #[]

Existe outros operadores incluindo AND e XOR

#*****************************#

Operador ternário

return True if age > 18 else False 
===
return age > 18 ? True : False #JS

#*****************************#

Strings

"""
Qualquer coisa escrita aqui será printada no
mesmo formato escrito aquij no código
"""

"beau person".upper()
"beau person".lower()
"beAu person".title() #Beau Person

"au" in name #True, contem "au" em "beau"

"be\"au" #considera " como parte da string
ou 
'be"au'

print(name[1:3]) #ea
print(name[:3]) #Bea
print(name[1:]) #eau

any([True, False]) #True
all([True, False]) #False

#*****************************#

enum
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State(1)) #State.ACTIVE
print(State(1).value) #1

#*****************************#

Listas podem conter variados formatos de dados, como acontece no JS 

.append (adiciona no final da lista)
.extend ou += (concatena listas)
.remove (Remove néh)
.pop (retorna e remove ultimo elemento)
.insert (insere elemento em posição especifica)
.sort (ordena lista)

#*****************************#

Tuplas = é uma lista, mas usa () ao invés de []

#*****************************#

dictionaries

.get("color", "brown") # tenta pegar valor do indice, caso contrário retorne "brown"
.keys (lista todas as chaves)
.values (lista todos os valores)
del dict['key'] (deleta chave)
.copy (cria uma cópia do dict)

#*****************************#

Sets

Uma lista desordenada escrita entre {} que não contem elementos duplicados
Parcialmente imutável
Geralmente utilizado com operações matematicas como união, 
interseção e diferença simetrica

set1 = {"Roger", "sid"}
set2 = {"Roger"}

set1 & set2 # interseção {'Roger'}
set1 | set2 # união {'Roger', 'sid'}
set1 - set2 # diferença {'sid'}

#*****************************#

Dictionaries passados como parametro em funções
podem ter seus valores alterados em outro escopo,
pois neste caso é passado o endereço do objeto e
não criado uma cópia do objeto, que nem as variaveis
comuns

#*****************************#

variavel global e local

Em um caso hipotético, temos uma função e duas variaveis denominadas X
Uma dentro da função (local) e outra fora da função (global)

Dentro da função, se declarar uma variavel com prefixo "global", 
significa que queremos o valor que está fora de funções e classes (global)

Se declarar como "nonlocal", então queremos a variável do escopo acima

Pra isso funcionar, as variaveis devem ter o mesmo nome

x = 1
def funcao():
    x = 2
    def bar():
        global x  # 1

    def baz():
        nonlocal x # 2

#*****************************#

loops

while condition:

for item in [1, 2, 3, 4]:
for index, item in enumerate(list)

continue: usado para avançar para a próxima iteração
semelhante ao break, porém finalizando somente a iteração atual.

#*****************************#

Classes
class Animal:
    def walk(self):
        print("walking...")

class Dog(Animal): # extends Animal
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)
roger.name
roger.bark()
roger.walk()

#*****************************#

Modules

Podemos importar funções nativas ou de outros arquivos
Eles são interpretados como classes

import dog
dog.bark()

Se quiser importar a função bark() diretamente -> from dog import bark

Para navegar entre pastas, basta usar "."

#*****************************#

Argumentos no terminal

Podemos passar valores no terminal ao rodar a aplicação
Pra visualizar os dados, usamos o modulo "sys"
e sys.argv, que retorna uma lista

python main.py beau 39
['main.py', 'beau', '39']

Podemos usar tbm argparse.ArgumentParser() que possui mais funcionalidades

#*****************************#

Lambda functions

São funções simplificadas e sem nome, como um arrow function do JS

multiply = lambda a, b : a * b
multiply(2, 4)

Versão JS
(a, b) => {
    return a * b
}

#*****************************#
map, filter, reduce

map: executa uma função para cada item
map(function, list)

filter: retorna somente os elementos que batem com a condicional
filter(function with bool return, list)

reduce: É um acumulador. Para cada item, é executado uma função com dois argumentos
O primeiro é a variavel acumuladora, a segunda é um item da lista

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum = reduce(lambda acum, item: acum[1] + item[1], expenses)

#*****************************#

decorator

Decorador é uma função que recebe uma função como parametro e retorna uma função

def decorator(func):
    print("Before")
    func()
    print("after")

@decorator 
def hello():
    print("Hello")

# Before, Hello, after

Toda vez que a função Hello() for chamada, será executada 
a função decorator(), que recebe como parametro a função Hello()

O código da função hello() será executada dentro do decorator 

#*****************************#

exceptions

try: # Tenta executar o código
except <ErrorType>: # Executa se tal erro aconteceu
else: # Se um outro erro qualquer aparecer...
finally: # executa no final, independente se deu certo ou errado

raise Exception('an error')

#*****************************#

Em vez de usar map, podemos simplificar alguns casos

numbers = [1, 2, 3]
a = [n*2 for n in numbers] # 2, 4, 6

#*****************************#

Ao construir classes, podemos sobreescrever alguns operadores
__gt__ permite executar uma operação lógica, permitindo usar
operadores lógicos para comparar objetos, por exemplo:

def __gt__ (self, other):
    return True if self.age > other.age else False

#*****************************#
