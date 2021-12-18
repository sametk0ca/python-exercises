def meal():    
    meal=int(input("Enter your meal's price:"))
    tax=(meal*(7/100))
    tip=(meal*(18/100))
    total=tax+meal+tip
    print("Tax is:",f'{tax:.2f}')
    print("Tip is:",f'{tip:.2f}')
    print("The total price that you must pay is:",f'{total:.2f}')


meal()