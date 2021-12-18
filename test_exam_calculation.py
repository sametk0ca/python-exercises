def exam_calc():
    test1=int(input("Enter test 1 score : "))
    test2=int(input("Enter test 2 score :  "))
    sınav=int(input("Enter exam score : "))


    if (test1>=26 or test1 < 0) :
        print("Invalid Score")
    elif (test2>=26 or test2 < 0) :
        print("Invalid Score")
    elif (sınav>=51 or sınav < 0) :
        print("Invalid score")
    elif (sınav<=24) or ((test1+test2+sınav)<=49) :
        print("Failed")
    else :
        if ((test1+test2+sınav)>=80) and ((test1+test2+sınav)<=100) :
            print("Excellent")
        elif ((test1+test2+sınav)>=60) and ((test1+test2+sınav)<=79) :
            print("Good")
        elif ((test1+test2+sınav)>=50) and ((test1+test2+sınav)<=59) :
            print("Passed")
        else :
            print("Failed")
exam_calc()            