def main():
    response = input("What time is it?: ")
    time=convert(response)
    if time >=7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    dec = float(minutes)/60
    return float(hours) + dec

main()
