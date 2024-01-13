def main():
    time = convert(input("What time is it?\n"))
    
    if (time < 8) & (time > 7):
        print ("breakfast time")
    elif (time < 13) & (time > 12):
        print ("lunch time")
    elif (time < 19) & (time > 18):
        print ("lunch dinner")
            


def convert(time):
    tsplit = str(time).split(":")
    if tsplit[1] == 0:
        convertedtime = tsplit[0]
    else:
        (convertedtime) = float(tsplit[0] + "." + str((int(tsplit[1])/60)).split(".")[1])
    
    return convertedtime    

if __name__ == "__main__":
    main()