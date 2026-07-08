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

def main():
    while True:
        try:
            date = input("Date: ")
            day, month, year = convert_date(date)
            print(f"{year}-{month:02}-{day:02}")
            break
        except ValueError:
            print("incorrect format")

def convert_date(date):
    if "/" in date:
        month_number, day, year = date.split('/')
    elif date.split()[0] in months:
        if "," not in date:
            raise ValueError

        month_day, year = date.split(",")
        month, day = month_day.split()
        month_number = months.index(month) + 1
    else:
        raise ValueError

    if len(year.strip()) != 4:
        raise ValueError

    day = int(day)
    month_number = int(month_number)
    year = int(year)

    if month_number > 12 or day > 31:
        raise ValueError
    
    return (day, month_number, year)

main()

