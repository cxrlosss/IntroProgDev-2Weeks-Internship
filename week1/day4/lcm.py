def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        print(a, b)
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

zahl1 = int(input("Gib die erste Zahl ein: "))
zahl2 = int(input("Gib die zweite Zahl ein: "))


kleinstes_gemeinsames_vielfaches = lcm(zahl1, zahl2)
print("Das kleinste gemeinsame Vielfache von", zahl1, "und", zahl2, "ist:", kleinstes_gemeinsames_vielfaches)
