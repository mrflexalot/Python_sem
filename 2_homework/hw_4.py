# Реализуйте алгоритм перемешивания списка.

import random
randomlist = random.sample(range(10), 5)
print(f"Original list: {randomlist}")
random.shuffle(randomlist)
print(f"Shuffled list: {randomlist}")
