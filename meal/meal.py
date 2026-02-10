def main():
    time = input("What time is it? ")
    time = float(convert(time))
    #print(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else :
        print("", end='')


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes=int(minutes)
    totalMinutes = (hours*60) + minutes
    return str(totalMinutes/60)
    ...


if __name__ == "__main__":
    main()
