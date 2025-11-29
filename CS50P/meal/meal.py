def main():
    str_time = str(input("Enter: "))
    time = convert(str_time)
    if (7<= time <=8):
        print("breakfast time")
    elif (12<= time <=13):
        print ("lunch time")
    elif (18<= time <=19):
        print ("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    time_in_hours = hours + (minutes/60)
    return time_in_hours

if __name__ == "__main__":
    main()
