math,physics,chemistry = [int(x) for x in (input("Please enter the marks in math, physics, chemistry:\n ").split())]

if math<35 or physics<35 or chemistry<35:
    print("Sorry you are failed in exam")
else:
    average = (math+physics+chemistry)/3
    if average<=59:
        print("Grade C")
    elif average<=69:
        print("Grade B")
    else:
        print("grade A")    
        