def main():
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    while True:
        try:
            ydm = transform(month)
            print(f"{ydm[0]}-{ydm[1]}-{ydm[2]}")
            break
        except:
            pass



def transform(month):

    while True:
        try:
            date = str(input("Date: "))

            if "/" in date:
                date = date.strip("/")

            if " " in date:
                date = date.strip(" ")

            m = str(date[0])
            day = date[1]
            year = date[2]

            if len(day) == 1:
                day = "0"+day

            if m.isalpha() == True:
                try:
                    if m in month:
                        m = str((month.index(m)) + 1)
                        pass
                except:
                    break
            else:
                pass

            if len(m) == 1:
                m = "0"+m

            if m.isalpha() == False:
                return year, m, day
            else:
                pass


        except ValueError:
            pass

if __name__ == "__main__":
    main()
