import random,itertools

deck=list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
print(deck)
for i in range(5):
    print(deck[i][0],deck[i][1])