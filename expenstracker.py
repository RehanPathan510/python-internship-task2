# Expense Tracker Application
# Python Programming Internship - Task 2
# Features:
# 1. Add Expense
# 2. View Expenses
# 3. View Total Spent
# 4. Exit
def add_expense():
      product = input("Enter the product : ")
      price = float(input("Enter the price : "))
      print(".................................................")
      with open("expenses.csv","a") as  file:
           file.write(product + " , " + str(price)+ "\n" )
           print("Expense saved successfully.......")
                 
#add_expense()

def view_expense():
    with open("expenses.csv","r") as file:
        for line in file:
          print(line.strip())
         # view_expense
          
def view_total_spent():
    total = 0
    with open("expenses.csv","r") as file:
        for line in file:
           product,price = line.strip().split(", ")
           total = total + float(price)

    print("total spent : ",total)
           
#view_total_spent()

          
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        view_total_spent()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")     
    