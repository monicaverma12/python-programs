
def is_prime(number):
    if number <= 1:
        print("The number is not prime")
    elif number == 2 or number == 3:
        print("The number is prime")
    elif number % 2 == 0 or number % 3 == 0:
        print("The number is not prime")
    i = 5
    while i*i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            print("The number is not prime")
        i += 6
    else:
        print("The number is prime")


while True:
    num = int(input("Type in a number to see if it is prime: "))
    is_prime(num)
    # Ask the user if they want to go again
    goAgain = input("Do you want to find the check another number? (y/n)  ")
    if goAgain == "n" or goAgain == "N":
        print("Thank you for using the prime number checker!")
        break
    # Check if user input is valid
    if goAgain != "n" and goAgain != "N" and goAgain != "y" and goAgain != "Y":
        print("Invalid input")










