# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal
from math import pi


d = input("Enter the number d to calculate number's pi presicion")
p = pi
p = Decimal(p)
d = Decimal(d)
print(f"Number Pi with {d} presicion equals: {p.quantize(d)}")
