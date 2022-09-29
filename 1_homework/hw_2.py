# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = float(input("enter the number x: "))
y = float(input("enter the number y: "))
z = float(input("enter the number z: "))
firststatement = not (x or y or z)
secondstatement = not x and not y and not z
if firststatement == secondstatement:
    print("statements are true")
else:
    print("statements are false") #срабатывать не будет, так как по условию утверждение верно
