def magic_bday():   
    month=int(input("Birth month : "))
    day=int(input("Birth day : "))
    year=int(input("last 2 digits of birth year : "))
    if (month <=0 or month >=13) :
        print("Invalid month")
 

    elif (day >=31 or day <= 0) :
        print("Invalid month")

    elif (year <=0 or year >99) :
        print("Invalid month")
    else:
        if (month*day == year) :
            print(" You got magic birthday!!! ")
        else :
            print(" You have not magic birthday :( ")
magic_bday() 