import time

def menu():
    rowOfNumbers = [34, 21, 231, 1, 3, 534, 43, 23, 54, 22, 64, 57, 86, 87, 26]

    Choice1 = input('Choose a number form the list or press 4 to print list and manipulate with numbers')
    time.sleep(2)
    Choice1 = int(Choice1)

    if Choice1 in rowOfNumbers:
        print('Number already in list')
        time.sleep(2)
    elif Choice1 == 4:
        print(rowOfNumbers)
        Manipulate1 = input('Would you like to sort the list?(y/n)')
        if Manipulate1 == 'y':
            print(rowOfNumbers.sort())
        elif Manipulate1 == 'n':
            print('Alright heres is the unsorted list')
            print(rowOfNumbers)
        else:
            print('Error')
    else:
        print('That is a new number, added to the list!')


    #----------------------------------------------------------#
    #   If the number doesn't exist, lets add it to the list
    #----------------------------------------------------------#
    if Choice1 not in rowOfNumbers:
        rowOfNumbers.append(Choice1)
        print(rowOfNumbers)
    #----------------------------------------------------------#
    #   If they want to delete a number from the list
    #----------------------------------------------------------#
    Choice2 = input('Would you like to delete a number? if yes, choose the number or type 2')
    Choice2=int(Choice2)
    if Choice2 in rowOfNumbers:
        rowOfNumbers.remove(Choice2)
        print(rowOfNumbers.index(Manipulate1))
        print(rowOfNumbers)
        time.sleep(2.1)
        print('Number has been removed from the list')
    elif Choice2 == 2:
        print('Okay nothing choosed')

    else:
        print('Number does not exist in the list, closing the system..')

    # ----------------------------------------------------------#
    #   If they want to do something else
    # ----------------------------------------------------------#

print('Welcome to the backend')
time.sleep(2)
print('Please wait....')
time.sleep(2)

menu()






