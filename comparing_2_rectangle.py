def rectangles():
    length1=float(input("Enter length 1 : "))
    width1=float(input("Enter width 1 : "))
    length2=float(input("Enter length 2 : "))
    width2=float(input("Enter width 2 : "))

    rectangle1=(length1*width1)
    rectangle2=(length2*width2)

    if rectangle1 > rectangle2 :
        print("First rectangle is bigger.")
    elif (rectangle1==rectangle2) :
        print("Areas of rectangles are equal.")
    else :
        print("Second rectangle is bigger.")
rectangles():    