def main():
    listc = listcut(input("camelCase:\n"))
    index = separator(listc)

    m = 0
    snakecase = []
    for k in range(len(listc)):
        if k == index[m]:
            snakecase.append("_"+ listc[k])
            if m + 1 < len(index):
                m = m + 1
            else:
                pass

        else:
            snakecase.append(listc[k])

    output = "".join(snakecase).lower()
    print(output)


def listcut(camelCase):

    listcut = []
    for i in range(len(camelCase)):
        listcut.append(camelCase[i])
    return listcut

def separator(listcut):
    index = []
    for j in range(len(listcut)):
        cut = str(listcut[j]).strip(",")
        if cut.isupper() == True:
            index.append(j)
        else:
            pass
    return index

if __name__ == "__main__":
    main()
