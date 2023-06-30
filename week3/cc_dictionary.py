inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    total_inches = 0

    for i in inches_snow:
        total_inches += inches_snow[i]
    print("Total snowfall inches: ", total_inches)

print_total_snowfall(inches_snow)