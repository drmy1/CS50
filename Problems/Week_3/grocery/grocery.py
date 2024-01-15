def main():

    grocery_list = {}

    grocery = item_list(grocery_list)

def item_list(grocery_list):

    while True:
        try:
            item = input().strip(" ")
            if item  in grocery_list:
                grocery_list[f"{item}"] += 1
            else:
                grocery_list[f"{item}"] = 1

        except EOFError:
            x = []
            for val in grocery_list:
                x.append(val)
                for i in range(len(x)):
                    z = x[i]
                    z = str(z).strip("'")
                print(grocery_list[f"{z}"], f"{z.upper()}")


            break
        except KeyboardInterrupt:
            pass




if __name__ == "__main__":
    main()
