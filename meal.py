def main():
    time = input("enter the time (e.g., 7:30, 19:45, 7:30 am, 7:30 pm): ")
    hours=convert(time)

    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")
    else:
        exit()
def convert(time):
    if "am" in time or "pm" in time:
        time, amorpm = time.split()
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        
        if amorpm == "pm" and hours != 12:
            hours += 12
        elif amorpm == "am" and hours == 12:
            hours = 0
    else:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
    
    return hours + minutes / 60.0

if __name__ == "__main__":
    main()