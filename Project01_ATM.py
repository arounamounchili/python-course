def welcome_message():
    print("\n\tWelcome to your Bank")
    print("""
    1)\tBalance
    2)\tWithdraw
    3)\tDeposit
    4)\tQuit
    """)


def start():
    balance = 2000

    while True:
        welcome_message()
        try:
            option = int(input("Choose an option: "))
        except Exception as e:
            print("Error: ", e)
            print("Please only enter 1, 2, 3 or 4")
            continue

        if option == 1:
            print(f"Your Balance is {balance}€")
        if option == 2:
            print(f"Your Balance is {balance}€")
            withdraw = float(input("Enter the amount to withdraw: "))
            if withdraw > 0:
                if withdraw > balance:
                    print("No money in your account")
                else:
                    balance -= withdraw
                    print(f"Your new Balance is {balance}€")
            else:
                print("No withdrawal takes place")

        if option == 3:
            print(f"Your Balance is {balance}€")
            deposit = float(input("Enter the deposit amount: "))
            if deposit > 0:
                balance += deposit
                print(f"Your new Balance is {balance}€")
            else:
                print("No deposit made")
        if option == 4:
            break


if __name__ == "__main__":
    start()
