month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").split("/")

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
            print(f"{year}-{m}-{day}")
        else:
            pass


    except ValueError:
        pass

