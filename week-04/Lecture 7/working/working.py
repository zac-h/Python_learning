import re
import sys

def main():
        print(convert(input("Hours: ")))

def convert(s):
    times = {
        "12:00 AM": "00:00",
        "1:00 AM": "01:00",
        "2:00 AM": "02:00",
        "3:00 AM": "03:00",
        "4:00 AM": "04:00",
        "5:00 AM": "05:00",
        "6:00 AM": "06:00",
        "7:00 AM": "07:00",
        "8:00 AM": "08:00",
        "9:00 AM": "09:00",
        "10:00 AM": "10:00",
        "11:00 AM": "11:00",
        "12:00 PM": "12:00",
        "1:00 PM": "13:00",
        "2:00 PM": "14:00",
        "3:00 PM": "15:00",
        "4:00 PM": "16:00",
        "5:00 PM": "17:00",
        "6:00 PM": "18:00",
        "7:00 PM": "19:00",
        "8:00 PM": "20:00",
        "9:00 PM": "21:00",
        "10:00 PM": "22:00",
        "11:00 PM": "23:00",
    }

    time_parts = []

    time = re.search(r"^([0-9]?[0-9])(:[0-9][0-9])? (AM|PM) to ([0-9]?[0-9])(:[0-9][0-9])? (AM|PM)", s)
    if not time:
#        print("Invalid format")
        raise ValueError

    for group in time.groups():
        if group is None:
            time_parts.append(":00")
        else:
            time_parts.append(group)

    start_hour = int(time_parts[0])
    start_minute = int(time_parts[1].replace(":",""))

    finish_hour = int(time_parts[3])
    finish_minute = int(time_parts[4].replace(":",""))

    if not 1 <= start_hour <= 12 or not 1 <= finish_hour <= 12:
#        print("Invalid hour")
        raise ValueError

    if not 0 <= start_minute <= 59 or not 0 <= finish_minute <= 59:
#        print("Invalid minute")
        raise ValueError

    time_from = time_parts[0]+time_parts[1]+" "+time_parts[2]
    time_to = time_parts[3]+time_parts[4]+" "+time_parts[5]

    return f"{times[time_from]} to {times[time_to]}"

if __name__ == "__main__":
    main()
