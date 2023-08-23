months = [
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
    date = input("Date: ")

    M, D, Y = date.split("/")

    if (int(M) >= 1 and int(M) <= 12) and (int(D) >= 1 and int(D) <= 31):
        break

    except:
        try:
            old_M, old_D, old_Y = date.split(" ")
            for i in range(len(months)):
                if old_M == months[i]:
                    M = i + 1
            D = old_D.replace(",", "")
            if (int(M) >= 1 and int(M) <= 12) and (int(D) >= 1 and int(D) <= 31):
                break
    except:
        print()
        pass

print(f"{Y}-{int(M):02}-{int(D):02}")




