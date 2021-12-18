def FtoC(t):
    convtemp=((5/9)*(t-32))
    return convtemp
fahrenheit=eval(input("Enter a temperature in degrees Fahrenheit:"))
celsius=FtoC(fahrenheit)
print("Celsius equivalent:",f'{celsius:.2f}',"degrees")
FtoC()