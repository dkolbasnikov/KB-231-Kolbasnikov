def discriminant(a, b, c):
    return b**2 - 4*a*c

a = float(input(" a: "))
b = float(input(" b: "))
c = float(input(" c: "))

result = discriminant(a, b, c)
print(f"Discriminant: {result}")
