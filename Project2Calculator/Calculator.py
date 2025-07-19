print("\nThe Basic Arithmetic operations")
print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- Division")

option=int(input("Choose an Operation: "))

if option in [1,2,3,4]:
  num1=float(input("Enter the First Number: "))
  num2=float(input("Enter the Second Number: "))
  if option==1:
    sum=num1+num2
    print("The Result is of two Numbers: ", sum)
  elif option==2:
    sub=num1-num2
    print("The Result is of two Numbers: ", sub)
  elif option==3:
    mul=num1*num2
    print("The Result is of two Numbers: ", mul)
  elif option==4:
    if num2==0:
      print("Error: Cannot divide by Zero")
    else:
      divi=num1/num2
      print("The Result is of two Numbers: ", divi)
else:
   print("Invalid Operation Number. Try Again!") 
