#main menu function
def main_menu():
    print("\n============================") #main page
    print("----------WELCOME TO OPMS!----------") 
    print("==========")
    

    #showing options

    print("select preference. ")
    print("\t1. Admin \n\t2. Registered Customer \n\t3. New Customer")

    #showing options
    choice = input("I am type 1/2/3 to continue: ")

    #choice action
    
    if choice == '1':
        print('Admin')

    elif choice == '2':
        print('Registered Customer')

    elif choice == '3':
        print('New Customer')

    else:
        print("\n!!!! Invalid !!!!\n")
main_menu()
