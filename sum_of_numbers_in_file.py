def sum_of_numbers():

    sum=0
    length=0
    f=open('numbers.txt')
    for i in f.readlines() :
        sum+=int(i) 
        length+=1
    print('sum of the numbers in file is : ',sum)
    print('number of numbers in file is : ',length)
    average=sum/length
    print('Average of the numbers is: ' ,average)
    f.close()
sum_of_numbers()    