import webbrowser
import smtplib

def daniel():
    print("Daniel Gorgis")
    print("Ag 21")
    print("Lives in solrød strand")
    print("Goes to school")
    print("has 2 brothers")
    print("interested in a new job")
def lars():
    print("Lars Jensen")
    print("Ag 26")
    print("Lives in ballerip")
    print("Goes to school")
    print("has 2 sisters")
    print("interested in a new job")
def computer_list():
    print("Asus")
    print("Dell")
    print("Acer")
    print("Macbook")
    print("Lenovo")
    print("Toshiba")
    print("Alienware")
def phones_list():
    print("apple")
    print("Samsung")
    print("windows")
    print("HTC")
    print("huawei")
    print("onePhone")
    print("nokia")
def TV_list():
    print("Samsung")
    print("Phillips")
    print("Toshiba")
    print("B&O")
    print("sony")
    print("panasonic")
    print("LG")
    print("TLC")
    print("Sharp")
def drones_list():
    print("DJI")
    print("Parrot")
def Washingmachine_list():
    print("LG")
    print("Siemens")
    print("Mile")
    print("philips")
def Other_Electronics_list():
    print("Comming soon")
    print("No other electronics in stock ATM.")
def Pricerunner_list():
    print("For cheapest pricing go to www.pricerunner.dk, or go back to menu and choose 0")
System_users = []



Login = "Admin"
Password = "1234"

print("_______________________")
print("_______________________")
print("_____Please Login ______")
print("_______________________")
print("_______________________")

Choice1 = input("Enter Username:  ").capitalize().strip()
if Choice1 == Login:
    Choice2 = input("Enter Password:  ")
if Choice2 == Password:
    print("_______________")
    print("_______________")
    print("__M__E__N__U___")
    print("_______________")
    print("_______________")
    print("               ")
    print("1.Add a user__")
    print("2.Remove a user")
    print("3.Exit_________")
    print("4.Read list of Items")

    Choice3 = input("Choose 1, 2 or 3:  ").strip().capitalize()
    if Choice3 == "1":
        user1 = input("Enter the name of the new user:  ")
        user2 = input("Enter the age of the new user:   ")
        user3 = input("Enter where the user lives:      ")

        System_users.append(user1)
        System_users.append(user2)
        System_users.append(user3)


        print("a new user has been created with name: " + user1, "Age is " + user2, "he lives in " + user3)
        print(System_users)
    elif Choice3 == "2":
        delete1 = input("Enter the name of the user you want to delete: ")
        delete2 = input("are you sure you want to delete? (Y/N)").strip().lower()
        if delete2 == "y":
            print(delete1 + " has been successfully deleted")

        elif delete2 == "n":
            print("process has been canceled")

    elif Choice3 == "3":
        print("see you soon!! :-)") + exit(0)

    elif Choice3 == "4":

        print("List of Items")
        print("0.pricerunner.dk   search for the prices on different electronics and machines")
        print("1.Computers")
        print("2.Phones")
        print("3.TV")
        print("4.Drones")
        print("5.Washing machines")
        print("6.Other electronics")

        Choice4 = input("Choice from selected list").strip()


    if Choice4 == "1":
        print(computer_list())+Pricerunner_list()
    elif Choice4 == "2":
        print(phones_list())+Pricerunner_list()
    elif Choice4 == "3":
        print(TV_list())+Pricerunner_list()
    elif Choice4 == "4":
        print(drones_list())+Pricerunner_list()
    elif Choice4 == "5":
        print(Washingmachine_list())+Pricerunner_list()
    elif Choice4 == "6":
        print(Other_Electronics_list())+Pricerunner_list()
    elif Choice4 == "0":
        webbrowser.open("www.pricerunner.dk")
    else:
        print("Error not a choice from the list")













elif Choice1 != Login or Choice2 != Password:
    print("Wrong username or password")

else:
    print("error")


