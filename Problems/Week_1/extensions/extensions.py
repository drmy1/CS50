type = input("File name:\n").lower().strip()


endlist = type.split(".")

if len(endlist) != 1:

    end = endlist[len(endlist)-1]
    x = ""

    for i in range(len(end)):
        if i <3:
            x += end[i]
        else:
            break

    match x:
        case "gif" | "png":
            print(f"image/{x}")

        case "jpg" | "jpe":
            print("image/jpeg")

        case "pdf" | "zip":
            print(f"application/{x}")

        case "txt":
            print("text/plain")
        case _:
            print ("application/octet-stream")

else:
    print ("application/octet-stream")



