
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return(num1-num2)
def mul(num1,num2):
    return(num1*num2)
def dic(num1,num2):
    return(num1/num2)





while True:
    print("*****************")
    print("Calculator")

    print("1: Add ")
    print("2: Substract ")
    print("3: Multiplication ")
    print("4: Division ")
    print("5: Quit ")

    option = input("select operations: 1,2,3,4,5: ")

    if option == '5':
        print("Exting Program:....")
        break
    if option in('1','2','3','4'):
        num1=float(input("enter the First Number:  "))
        num2=float(input("enter the Second Number: "))

        if option == '1':
            print("Result: ",add(num1,num2))
            break
        elif option == '2':
            print("Result: ",sub(num1,num2))
            break
        elif option == '3':
            print("Result: ",mul(num1,num2))
            break
        elif option == '4':
            print("Result:  ",num1/num2)
            break

    else:
        print("Invalid Option Selected:")        

