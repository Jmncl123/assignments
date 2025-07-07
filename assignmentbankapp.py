# Naija Simple ATM Simulator 💳

balance = 0
pin = "1234"
transactions = []

print("Welcome to Naija Simple ATM 💳")

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is: ₦{balance}")

    elif choice == "2":
        try:
            amount = int(input("How much do you want to deposit?: "))
            if amount > 0:
                balance += amount
                transactions.append(f"Deposited ₦{amount}")
                print("Deposit successful.")
            else:
                print("Invalid deposit amount.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        try:
            amount = int(input("How much do you want to withdraw?: "))
            if amount > balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Invalid withdrawal amount.")
            else:
                balance -= amount
                transactions.append(f"Withdrew ₦{amount}")
                print(f"Withdrawal successful. Your new balance is ₦{balance}")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using Naija ATM.")
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
