if user_input.lower() == 'quit':
    break
    
try:
    new_expense = float(user_input)
    
    if new_expense < 0:
        print("Invalid Data. Enter a positive amount.")
        continue

    total += new_expense

except ValueError:
    print("Invalid Data")
  
