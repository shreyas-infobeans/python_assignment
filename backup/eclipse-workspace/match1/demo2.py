list1 = ['python','django']

match list1:
    case ['python','django']:
        print("python and django")
    case ['django','docker']:
        print("django and docker")
    case ['docker','drf']:
        print("docker and drf")
    case _:
        print("Default case")
        
class ATMConstants:
    withdraw = 1
    deposit = 2
    balance_check = 3

option =2

match option:
    case ATMConstants.withdraw:
        print("Withdraw money")
    case ATMConstants.deposit:
        print("deposit money")
    case ATMConstants.balance_check:
        print("balance_check")
    case _:
        print("default")
    