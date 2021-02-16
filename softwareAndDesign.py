def inputGallons():
    isgood = False
    while not isgood:
        s = input("Enter the total number of gallons used, divided by 1000: ")

        try:
            # try to convert to float
            num = float(s)

            # number (no exception occurred), is it positive?
            if num > 0:
                isgood = True
        except ValueError: # not a number
            pass

        if not isgood:
            print("Please enter a positive number")

    return num


def main():
    # constants (Are symbolics used rather than “magic number” constants?)
    # volume limits
    volumeUpper = 20
    volumeLower = 6
    # prices
    fee = 15
    costUpTo6K = 2.35
    costUpTo20K = 3.75
    costOver20K = 6.00

    # Initialize variables
    gallons = 0
    charge = 0
    total = 0

    # Prompt user for input
    gallons = inputGallons()

    # If gallons entered are above 20
    if (gallons > volumeUpper):
        charge  = (gallons - volumeUpper) * costOver20K
        charge += (volumeUpper - volumeLower) * costUpTo20K
        charge += volumeLower * costUpTo6K
    # If gallons entered are above 6 but below 20
    elif (gallons > volumeLower and gallons <= volumeUpper):
        charge  = (gallons - volumeLower) * costUpTo20K
        charge += (volumeLower * costUpTo6K)
    # If gallons are below 6 or equal to 6
    else:
        charge = gallons * costUpTo6K

    # Add calculated charge to the fee
    total = charge + fee;

    # Output
    print("You have used {0:} thousand gallons of water.".format(gallons))
    print("Your total water bill is ${0:.2f}.".format(total))


main()
