# Calculate
def compute_pay(h, r):
    h = float(h)
    r = float(r)
    if h <= 40:
        salary = h * r
    else:
        salary = (40 * r) + ((h - 40) * (r * 1.5))
    return salary


# trying to get the right number#
def get_float(x):
    while True:
        value = input(x)
        try:
            value = float(value)
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except:
            print("Please enter a numeric value (e.g. 40 or 7.5).")


# main
def calculation():
    h = get_float("Write your working hours please: ")
    r = get_float("Write your rate per hour please: ")
    pay = compute_pay(h, r)
    print("Pay:", pay)


# the program
calculation()
