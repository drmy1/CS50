def main(emoji):

    a = str(input()).split(" ")
    if a[1] == ":)":
        print(a[0], emoji[0])

    else:
        print(a[0], emoji[1])

def convert():
    smilingface = "🙂"
    frowningface = "🙁"
    return(smilingface, frowningface)

main(convert())




