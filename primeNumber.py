num = int(input("Type a number to see if its prime or not: "))




def check_prime():
    if num==0:
        print("The number is 0 which is not a prime number")
    elif(num==2 or num==3):
        print(" Yes, its a prime number")
    elif(num%2==0 or num%3==0 or num%5==0):
        print("No, the number is not prime")
    else:
        checknum()

def checknum():
    n = num-1





