def Fahrenheit_to_celsius(Fahrenheit):
    celsius=(Fahrenheit-32)*5/9
    return celsius
def celsius_to_fahrenheit(celsius) :  
   Fahrenheit=(celsius*9/5)+32
   return Fahrenheit
print("1.Fahrenheit to celsius")
print("2.celsius to Fahrenheit")
print("3. exit")
while True:
     ch=int(input("enter your choice"))  
     if ch==1:
         Fahrenheit=float (input("enter temperature in Fahrenheit:"))
         celsius=Fahrenheit_to_celsius(Fahrenheit)
         print("conversion of Fahrenheit to celsius",celsius)
     elif ch==2:
        celsius=float (input("enter temperature in celsius:"))    
        Fahrenheit=celsius_to_fahrenheit(celsius)
        print("conversion of celsius to Fahrenheit",Fahrenheit)
     else:
         print("thank you")
            