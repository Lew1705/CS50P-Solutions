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
    date = input("Date: ").strip()
    if "/" in date:
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if (1<=month<=12) and (1<=day<=31):
                print(f"{year:04}-{month:02}-{day:02}")
                break

        except ValueError:
            continue

    elif "," in date:
        try:
            date = date.replace(",", "")
            month_name, day, year = date.split()
            if month_name in months:
                month = months.index(month_name) + 1
                day = int(day)
                year = int(year)
                if 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
        except ValueError:
            continue
