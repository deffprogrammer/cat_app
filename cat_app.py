do = ["Run", "Clawing", "Sit", "Jump"]
history = []

def menu():
    print("1. Run")
    print("2. Clawing")
    print("3. Sit")
    print("4. Jump")
    print("5. History")

def ch(choice):
    if choice == 1:
        print("Your cat is",do[0])
        history.append(do[0])
    elif choice == 2:
        print("Your cat is",do[1])
        history.append(do[1])
    elif choice == 3:
        print("Your cat is",do[2])
        history.append(do[2])
    elif choice == 4:
        print("your cat is",do[3])
        history.append(do[3])
    elif choice == 5:
        print(history)

# Main
print("===== Welcome in Cat App =====")
name = input("Name your cat: ")
print("Hello", name)

menu()
x = "y"
while x == "y":
    choice = int(input("What do you want for your cat: "))
    ch(choice)

    x = input("press y to continue.... ")

