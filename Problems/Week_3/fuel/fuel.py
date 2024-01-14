def main():
    xy = int(calc("Fraction: "))
    
    if xy >= 99:
        print("F")
    elif xy <= 1:
        print("E")
    else:
        print(f"{xy}%")
    
def calc(prompt):
    xy = []
    while True:
        try:
            xy = str(input(prompt)).split("/")
            x = int(xy[0])
            y = int(xy[1])
            
            if x > y:
                calc(prompt)
            
            terminal = ((x / y) * 100)
                
            return terminal
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


if __name__ == "__main__":
    main()