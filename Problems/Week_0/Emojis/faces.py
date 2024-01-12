def main(emoji):

    a = str(input())
    a.replace(":)", emoji[0])
    print(a)

def convert():
    smilingface = "🙂"
    frowningface = "🙁"
    return(smilingface, frowningface)

main(convert())




