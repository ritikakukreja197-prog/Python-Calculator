while True:
    
    print("====Python Calculator=====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    try:
        choice = int(input("Enter your choice(1-5): "))
        
        if choice == 5:
            print("Goodbye...")
            break
        
        elif choice < 1 or choice > 5:
            print("Invalid choice.")
            continue
        
        num1 = int(input("Enter your 1st number: "))
        num2 = int(input("Enter your 2nd number: "))
        

        if choice == 1:
            print("Addition: " , num1 + num2)
             
        elif choice == 2:
            print("Subtraction: " , num1 - num2)
            
        elif choice == 3:
            print("Multiplication: ", num1 * num2)
            
        elif choice == 4:
            print("Division: " , num1 / num2)
            
    except ValueError:
        print("Invalid input! Please enter a numeric values.")
        
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero")
        
        
    
    
       