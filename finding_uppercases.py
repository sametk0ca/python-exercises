def find_upper() :
    c=0
    f=open('text2.txt')
    for i in f.readlines() :
        for j in i:
            if j.isupper() :
                c+=1
            else : pass
    print("There is",c,"upper letter")
find_upper()