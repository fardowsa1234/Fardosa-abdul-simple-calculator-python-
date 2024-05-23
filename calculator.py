print("select a choice")
print("1.ADD")
print("2.DIVIDE")
print("3.SUBTRACT")
print("4.MULTIPLY")


choice = input()

if choice=="1":
    num1=input("Enter first number:")
    num2=input("Enter second number")
    print("The sum is;" + str(int(num1) + int(num2)))
    
elif choice=="2":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The result is;" + str(int(num1) / int(num2)))
    
elif choice=="3":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The difference is;" + str(int(num1) - int(num2)))
    
elif choice=="4":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The product is;" + str(int(num1) * int(num2)))

else:
    print("Invalid choice")