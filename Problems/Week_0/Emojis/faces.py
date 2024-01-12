def main(emoji):

    a = str(input()).split(" ")
    a[1].replace(":)", emoji[0])
    print(a)

def convert():
    smilingface = "🙂"
    frowningface = "🙁"
    return(smilingface, frowningface)

main(convert())




