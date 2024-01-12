def main(emoji):

    a = str(input()).split(" ")

    for i in range(len(a)-1):
        if a[i] == ":)":
            a[i] = emoji[0]
        else:
            a[i] = emoji[1]
    print(len(a))

def convert():
    smilingface = "🙂"
    frowningface = "🙁"
    return(smilingface, frowningface)

main(convert())




