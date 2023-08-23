ex = input("Expression: ")

x, y, z = ex.split(" ")

new_x = float(x)
new_z = float(z)

if y == '+':
    print(new_x + new_z)
if y == '-':
    print(new_x - new_z)
if y == '/':
    print(new_x / new_z)
if y == '*':
    print(new_x * new_z)