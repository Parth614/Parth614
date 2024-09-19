def Add(a,b):
    "This function adds two numbers"
    return (a+b)
def Subtract(a,b):
    "This function subtract two numbers"
    return(a-b)
def Multiply(a,b):
    "This function multiply two numbers"
    return(a*b)
def Divide(a,b):
    "This function divide two numbers"
    return(a/b)

print("Select opertaion\n"
      "1.ADD\n"
      "2.SUBTRACT\n"
      "3.MULTIPLY\n"
      "4.DIVIDE\n")
# Take input from the user
choice= input("Enter choice(1/2/3/4): ")

num1= int(input("enter first number: "))
num2=int(input("enter second number: "))

if choice == '1':
    print( num1 ,"+" ,num2, "=" , Add(num1,num2))
elif choice == '2':
    print( num1 ,"-" ,num2, "=" , Subtract(num1,num2))
elif choice == '3':
    print( num1 ,"*" ,num2, "=" , Multiply(num1,num2))
elif choice == '4':
    print( num1 ,"/", num2,"=", Divide(num1,num2))
else:
    print("Invalid input")

