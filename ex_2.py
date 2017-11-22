from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2
print(*Unique(data1), sep=", ")
print(*Unique(data2), sep=", ")
print(*Unique(['A','a','B','b']), sep=", ")
print(*Unique(['A','a','B','b'], ignore_case = True), sep=", ")
