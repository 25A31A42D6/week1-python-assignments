# WEEK 1 PYTHON ASSIGNMENTS

# 1. Temperature Converter
def temperature_converter():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9 / 5) + 32)
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", (f - 32) * 5 / 9)
    else:
        print("Invalid choice!")


# 2. Student Grade Calculator
def grade_calculator():
    marks = []

    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return
        marks.append(mark)

    average = sum(marks) / 5
    print("Average:", average)

    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    elif average >= 40:
        print("Grade: E")
    else:
        print("Grade: F")


# 3. Even/Odd and Prime Number Checker
def number_checker():
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if n <= 1:
        print("Not Prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")


# 4. Simple ATM Simulator
balance = 5000
correct_pin = "1234"


def login():
    attempts = 3

    while attempts > 0:
        pin = input("Enter your ATM PIN: ")

        if pin == correct_pin:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print("Incorrect PIN!")
            print("Attempts remaining:", attempts)

    print("Access denied!")
    return False


def check_balance():
    print("Your current balance is Rs.", balance)


def deposit():
    global balance
    amount = float(input("Enter deposit amount: Rs. "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
        print("Updated balance: Rs.", balance)
    else:
        print("Please enter a valid amount.")


def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: Rs. "))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance: Rs.", balance)


def atm_menu():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please try again.")


# Main Menu
def main():
    while True:
        print("\n===== WEEK 1 PROJECTS =====")
        print("1. Temperature Converter")
        print("2. Student Grade Calculator")
        print("3. Even/Odd & Prime Checker")
        print("4. Simple ATM Simulator")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            grade_calculator()
        elif choice == "3":
            number_checker()
        elif choice == "4":
            print("Welcome to the Simple ATM Simulator")
            if login():
                atm_menu()
        elif choice == "5":
            print("Program completed.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()