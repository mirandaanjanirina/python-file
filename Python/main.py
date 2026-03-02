import math

def main():

    print("Exo 1")
    print("Hello, World!")
    input("Press Enter to continue...")

    print("Exo 2")
    n= int(input("Enter an integer : "))
    m = float(input("Enter a float: "))
    s = input("Enter a string : ")  
    print(f"int: {n}, float: {m}, string: {s}")
    input("Press Enter to continue...")

    print("Exo 3 - 4")
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    g = a % b
    print(f"{a} + {b} = {c}")
    print(f"{a} - {b} = {d}")
    print(f"{a} * {b} = {e}")
    print(f"{a} / {b} = {f}")
    print(f"{a} % {b} = {g}")
    input("Press Enter to continue...")

    print("Exo 5")
    radius = float(input("Enter radius: "))
    pi = 3.14
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")
    input("Press Enter to continue...")

    print("Exo 6")
    L = float(input("Enter length: "))
    l = float(input("Enter width: "))
    area = L * l
    perimeter = 2 * (L + l)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    input("Press Enter to continue...")

    print("Exo 7")
    l_cm = float(input("Enter length in cm: "))
    l_m = l_cm / 100
    l_km = l_cm / 100000
    print(f"Length in km: {l_km}")
    print(f"Length in m: {l_m}")
    input("Press Enter to continue...")    

    print("Exo 8")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit}")
    input("Press Enter to continue...")

    print("Exo 9")
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9   
    print(f"Temperature in Celsius: {celsius}")
    input("Press Enter to continue...")

    print("Exo 10")
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = pow(a, b)
    print(f"{a}**{b} = {c}")
    input("Press Enter to continue...")

    print("Exo 11")
    n = int(input("Enter n : "))
    square_root = math.sqrt(n)
    print(f"Square root {n} : {square_root}")
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()