def StuGrade():
    studentNum=int(input('How many student do you have? : '))
    students={}
    for i in range(1,studentNum+1):
        name=input('Enter student name : ')
        surname=input('Enter student surname : ')
        number=int(input('Enter student number : '))
        midterm=int(input('Enter midterm grade : '))
        final=int(input('Enter final grade : '))
        if number in students :
            print('That person already exists in list')
        else :
            totalGrade=(midterm*(4/10)+final*(6/10))
            if totalGrade > 87 and totalGrade < 101 :
                letter='AA'
            elif totalGrade > 79 and totalGrade < 88 :
                letter='BA'
            elif totalGrade > 72 and totalGrade < 80 :
                letter='BB'
            elif totalGrade > 65 and totalGrade < 73 :
                letter='CB'
            elif totalGrade > 59 and totalGrade < 66 :
                letter='CC'
            elif totalGrade > 54 and totalGrade < 60 :
                letter='DC'
            elif totalGrade > 49 and totalGrade < 55 :
                letter='DD'
            elif totalGrade > 0 and totalGrade < 50 :
                letter='FF'
            else : 
                print('Invalid grade')    



            students.update({number:{'name':name,'surname':surname,'midterm':midterm,'final':final,'Total Grade':totalGrade,'Letter Grade':letter}})
    chosen=int(input('Enter the number of student whose information you want to see : '))
    print(students[chosen])








StuGrade()
