def grade():
  grade= int(input("Enter your percentage score:"))
  if (grade <= 100) and (grade >= 90):
    letter= 'A'
  elif (grade <=89 ) and (grade >= 80):
    letter='B'
  elif (grade <= 79) and (grade >= 70):
    letter='C'
  elif (grade <= 69) and (grade >= 60):
    letter='D'
  elif (grade <= 59) and (grade >= 0):
    letter='F'
  else : print("Invalid score")
    print("Your grade is:",grade,"Your letter grade is:",letter)

grade():    