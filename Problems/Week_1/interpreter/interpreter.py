xyz = input("Expression:\n").split(" ")

x = float(xyz[0])
y = xyz[1]
z = float(xyz[2])

match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "*":
        print(x*z)
    case "/":
        print(x/z)
    


