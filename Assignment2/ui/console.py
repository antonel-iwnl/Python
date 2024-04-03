from domain.lab3_A2_P2 import *
from tests import assignment_test


def dataExamples():
    score_list = [7, 5, 4, 8, 9, 10, 4, 5, 12, 52, 16, 72]
    print('function 1: add 5 to the list')
    add(score_list, 5)
    print(score_list)

    print('function 2: less for value = 10') 
    print(less(score_list, 10))

    print('function 3: remove_interval from index 3 to 5')
    removeseq(score_list, 3, 5)
    print(score_list)

    print('function 4: sorted participants by score') 
    print(sorted(score_list))

    print('function 5: sorted by value = 9') 
    print(sortedval(score_list, 9))

    print('function 6: sequence average from idx 3 to 5')
    print(avg(score_list, 3, 5))

    print('function 7: sequence mul where value = 3')
    filter_mul(score_list, 3)
    print(score_list)

    score_list = [7, 5, 4, 8, 9, 10, 4, 5, 12, 52, 16, 72]
    print(score_list)

    print('function 8: mul where value = 3 and from idx 1 to 4')
    print(mul(score_list, 3, 1, 4))
    
    print('function 9:replace where idx = 3, new_value = 99')
    replace(score_list, 3, 99)
    print(score_list)

    print('function 10: remove interval where idx from 3 to 5')
    removeseq(score_list, 3, 5)
    print(score_list)

def printMenu():
    print('MENU:')
    print('-1 - print data examples')
    print(' m - print menu')
    print(' 1 - Adding a new value to the end of the list.')
    print(' 2 - Adding a new value to a specified index in the list.')
    print(' 3 - Deleting an element from the given index.')
    print(' 4 - Removing a specified sequence.')
    print(' 5 - Replacing the old values with the new ones. ')
    print(' 6 - The participants with score less than given value. ')
    print(' 7 - The participants sorted by their score.')
    print(' 8 - The participants sorted by scores higher than given value.')
    print(' 9 - Get the average score for participants between the two given index')
    print('10 - Get minimum score for participants between the two given index.')
    print('11 - Get the score of participants between the two given index, which are multiples of value given.')
    print('12 - Keep only participants with scores multiple of given value, removing the other participants (scores).')
    print('13 - Keep only participants with scores higher than value given, removing the other participants (scores).')
    print('14 - Undo the last operation that modified the list.')
    print(' p - Print list.')
    print(' x - exit program')
    print(". . .")

def start():
    assignment_test.runTests()
    print("All tests ran successfully!")
    print()
    printMenu()
    list = [10, 6, 15, 3, 10]
    command = None
    print()
    while command != 'x':
        command = input(">>>")
        if command == '-1':
            dataExamples()
        elif command == 'm':
            printMenu()
        elif command == '1':
            value = int(input(print("Input a value: ")))
            add(list, value)
        elif command == '2':
            value = int(input(print("Input a value: ")))
            index = int(input(print('Input an index: ')))
            insert(list, index, value)
        elif command == '3':
            index = int(input(print("Input an index: ")))
            remove(list, index)
        elif command == '4':
            from_index = int(input(print('Starting index: ')))
            to_index = int(input(print('End index: ')))
            removeseq(list, from_index, to_index)
        elif command == '5':
            index = int(input(print("Input an index: ")))
            new_value = int(input(print("Input a new value: ")))
            replace(list, index, new_value)
        elif command == '6':
            value = int(input(print("Input a value: ")))
            less(list, value)
        elif command == '7':
            print(sorted(list))
        elif command == '8':
            value = int(input(print("Input a value: ")))
            print(sortedval(list, value))
        elif command == '9':
            from_index = int(input(print('Starting index: ')))
            to_index = int(input(print('End index: ')))
            avg(list, from_index, to_index)
        elif command == '10':
            from_index = int(input(print('Starting index: ')))
            to_index = int(input(print('End index: ')))
            minim(list, from_index, to_index)
        elif command == '11':
            value = int(input(print("Input a value: ")))
            from_index = int(input(print('Starting index: ')))
            to_index = int(input(print('End index: ')))
            mul(list, value, from_index, to_index)
        elif command == '12':
            value = int(input(print("Input a value: ")))
            filter_mul(list, value)
        elif command == '13':
            value = int(input(print("Input a value:")))
            filter_greater(list, value)
        elif command == '14':
            undo(list)
        elif command == 'p':
            print(list)
        elif command == 'x':
            print("Program exited")
        else:
            print("Invalid command")

