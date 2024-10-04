# cis129 mod 5 lab
"""
Created on Thu Oct  3 20:44:52 2024

@author: Josue Monreal
"""
# function to read today bottles count the return total bottles
def getBottles():
    counter = 1    # set the counter to 1
    totalBottles = 0    # set totalBottles initially to 0
    
    # while counter is less than or equal to 7
    while counter<=7:
        # read today bottles count as int
        todayBottles = int(input("Enter number of bottles for today: "))
        # then sum it into the totalBottles count
        totalBottles = totalBottles + todayBottles
        # increment the counter
        counter = counter + 1

    # return totalBottles
    return totalBottles

# function to calculate the total payment
def calcPayment(totalBottles):
    # calculate the total payout by multiplying by 0.10
    totalPayout = totalBottles * .10
 # return the totalPayout
    return totalPayout

# function to print the info
def printInfo(totalBottles, totalPayout):
    # print all info
    print("The total numbers of bottle collected is:", totalBottles)
    # here %.1f is used to precise the totalPayout to 1 decimal place
    print("The total payout is $%.1f" %totalPayout)

# main() function
def main():
    # initially set the endProgram to no
    endProgram = "no"
    # loop control using endProgram
    while endProgram == "no":
        # call the getBottles() to get totalBottles
        totalBottles = getBottles()
        # call calcPayment to calculate the total payout
        totalPayout = calcPayment(totalBottles)
        # call the printInfo to print all details
        printInfo(totalBottles, totalPayout)
        # ask user whether he wants to end the program or not
        endProgram = input("Do you want to end the Program? (Enter yes or no): ")
        print("")


# call main() function
main()