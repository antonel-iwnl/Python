from domain.participants import *

def showMenu():
    print ("Hello, this is the menu.")

    print(' 1. Adding a new value to the end of the list.')
    print(' 2. Adding a new value to a specified index in the list.')
    print(' 3. Deleting an element from the given index.')
    print(' 4. Removing a specified sequence.')
    print(' 5. Replacing the old values with the new ones. ')
    print(' 6. The participants with score less than given value. ')
    print(' 7. The participants sorted by their score.')
    print(' 8. The participants sorted by scores higher than given value.')
    print(' 9. Get the average score for participants between the two given index')
    print('10. Get minimum score for participants between the two given index.')
    print('11. Get the score of participants between the two given index, which are multiples of value given.')
    print('12. Keep only participants with scores multiple of given value, removing the other participants (scores).')
    print('13. Keep only participants with scores higher than value given, removing the other participants (scores).')
    print('14. Undo the last operation that modified the list.')
    print('P/p. Print list.')
    print('X/x. Exit')
    print("        ")


def run_ui(list):

    list_versions = [list]
    current_version = 0

    while True:
        showMenu()
        option = input('Please choose an option from 1 to 15.')
        print()
        if option == '1':
            value = int(input(print("Type value: ")))
            # list.add(list, value) - not good
            add(list, value)
        elif option == '2':
            value = int(input(print("Type value: ")))
            index = int(input(print("Give an index: ")))
            insert(list, index, value)
        elif option == '3':
            index = int(input(print("Give an index: ")))
            remove(list, index)
        elif option == '4':
            from_index = int(input(print("Give a from_index: ")))
            to_index = int(input(print("Give a to_index: ")))
            removeseq(list, from_index, to_index)
        elif option == '5':
            index = int(input(print("Give an index: ")))
            new_value = int(input(print("Give a new value: ")))
            replace(list, index, new_value)
        elif option == '6':
            value = int(input(print("Type value: ")))
            less(list, value)
        elif option == '7':
            sorted_list(list)
        elif option == '8':
           value = int(input(print("Type value: ")))
           sorted_val(list, value)
        elif option == '9':
            from_index = int(input(print("Give a from_index: ")))
            to_index = int(input(print("Give a to_index: ")))
            sequence_avg(list, from_index, to_index)
        elif option == '10':
            from_index = int(input(print("Give a from_index: ")))
            to_index = int(input(print("Give a to_index: ")))
            sequence_minim(list, from_index, to_index)
        elif option == '11':
            value = int(input(print("Type value: ")))
            from_index = int(input(print("Give a from_index: ")))
            to_index = int(input(print("Give a to_index: ")))
            sequence_mul(list, value, from_index, to_index)
        elif option == '12':
            value = int(input(print("Type value: ")))
            filter_mul(list, value)
        elif option == '13':
            value = int(input(print("Type value: ")))
            filter_greater(list, value)
        elif option == '14':
            undo(list)
        elif option == 'P' or option == 'p':
            print(list)
        elif option == 'X' or option == 'x':
            break
        else:
            print('Invalid option.')


    return list