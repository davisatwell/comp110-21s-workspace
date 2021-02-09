how_much: int = int(input("Pick a number between 0-100:"))

if how_much < 50:
    print("I love you.")
else:
     if how_much < 75:
        print("you are dumb.")

a: int = 2021
b: float = 3.14
c: str = "hello"
d: bool = a > 2020 and b < 4.0 or not c != "world"
