def main():
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    ydm = split(month)
    print(f"{ydm[0]}-{ydm[1]}-{ydm[2]}", end="")


def split(month):

    while True:
        try:

            date = str(input("Date: ")).lstrip(" ").rstrip(" ")


            if "/" in date:
                date = date.split("/")
                m = str(date[0])
                day = date[1]
                year = date[2]

                if int(day) <= 31:
                    if m.isnumeric() == True:
                        if int(m) <= 12:
                            if len(day) == 1:
                                if day.isnumeric() == True:
                                    day = "0" + day



                            if len(m) == 1:
                                m = "0" + m
                            if year.isnumeric() == True:
                                return (year, m, day)







            if " " in date:
                date = date.split(" ")
                m = str(date[0])
                day = date[1]
                year = date[2]


                if m.isalpha() == True:
                    if "," in day:
                        day = day.strip(",")
                        if int(day) <= 31:
                            if m in month:
                                m = str((month.index(m)) + 1)
                                if len(day) == 1:
                                    if day.isnumeric() == True:
                                        day = "0" + day
                                    else:
                                        pass

                                if len(m) == 1:
                                    m = "0" + m
                                if year.isnumeric() == True:
                                    return year, m, day

        except KeyboardInterrupt:
            pass
        except ValueError:
            pass



if __name__ == "__main__":
    main()
