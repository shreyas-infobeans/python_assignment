import sys

accountBalance = 10000

option = int(sys.argv[1])

if option == 1:
    print("Total balance in your account is:", accountBalance)
elif option == 2:
    withDrawAmount = float(input("Enter withdraw amount:"))
    if withDrawAmount > accountBalance:
        print("Balance is insufficient in your account")
    else:
        print("You have withdraw total:", withDrawAmount)
        print("Remaining amount in your account is:", accountBalance - withDrawAmount)
elif option == 3:
    depositedAmount = float(input("Enter the amount you want to deposit:"))
    print("Total balance in your account is:", accountBalance + depositedAmount)
elif option == 4:
    depositedAmount = float(input("Enter the amount you want to deposit by cheque:"))
    print("Total balance in your account is:", accountBalance + depositedAmount)