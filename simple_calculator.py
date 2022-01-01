
    
def sum() :
    a=float(input('Enter the first number' ))
    b=float(input('Enter the second number' ))
    result = a+b
    print('Sum of the numbers is',result)
    

def multiplication() :
    a=float(input('Enter the first number : ' ))
    b=float(input('Enter the second number : ' ))
    result = a*b
    print('multiple of the numbers is',result)
    

def division() :
    a=float(input('Enter the first number : ' ))
    b=float(input('Enter the second number : ' ))
    try : a/b 
    except  ZeroDivisionError :
            print('Zero division error')
    result = a/b
    print('Result is ',result)
    

def extraction() :
    a=float(input('Enter the first number : ' ))
    b=float(input('Enter the second number : '  ))
    result=a-b
    print('Difference of the numbers is',result)
    

def main () :

    choice=int(input('What is the process that you want to do with calculator ?\n 1 for sum\n 2 for extraction\n 3 for multiplication\n 4 for division   ')   )
    if choice > 4 or choice < 1 :
        print('Invalid choice')

    elif choice == 1 :
        sum()
    elif choice == 3 :
        multiplication()
    elif choice == 2 :
        extraction()
    else :
        division()
main()

