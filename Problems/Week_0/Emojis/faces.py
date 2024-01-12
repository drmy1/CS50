def main(emoji):

    a = str(input()).split(" ")

    for i in range(len(a)):
        if a[i] == ":)":
            a[i] = emoji[0]
        elif a[i] == ":(":
            a[i] = emoji[1]
        else:
            pass



    for i in range(len(a)):
        a[i] = a[i] + a[()]

    print(b)

def convert():
    smilingface = "🙂"
    frowningface = "🙁"
    return(smilingface, frowningface)

main(convert())




