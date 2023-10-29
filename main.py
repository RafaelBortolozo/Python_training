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

#*****************************#



#*****************************#
#*****************************#
#*****************************#
#*****************************#
#*****************************#
#*****************************#
