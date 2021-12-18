def digits():
    string=input("Enter a string : ")
    counter=0
    for i in string :
        if i.isdigit() == True :
            counter+=1
     
    print("Number of digits is:",counter)
digits()    