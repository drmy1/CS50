def main():
    inputtext = input("Input: ")
    outputtext = modify_text(inputtext)
    print(outputtext)

def modify_text(text):
    textlist = []

    for i in range(len(text)):
        textlist.append(text[i])

    word = []
    for k in range(len(textlist)):
        match textlist[k]:
            case "A" | "E" | "I" | "O" | "U" | "a" | "e" | "i" | "o" | "u":
                pass
            case _:
                word.append(textlist[k])

    word = "".join(word)

    return word


if __name__ == "__main__":
    main()
