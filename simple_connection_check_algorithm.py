def con_check():

    answer=input("Do you have internet connection? Yes/No")
    if answer=="yes" :
        print("Nice!")
    else :
        print("Restart your router")
        answer1=input("Is it work?")
        if answer1=="yes" :
             print("Nice!")
        else :  
            print("Check the cables")
            answer2=input("Is it work?")
            if answer2=="yes" :
                print("Nice!")
            else :
                print("Contact your internet service provider")
con_check()