def find_discriminant(a, b, c):
    return b**2 - 4*a*c

if __name__ == "__main__":
    a = 1
    b = -3
    c = 2
    print(f"Discriminant: {find_discriminant(a, b, c)}")
