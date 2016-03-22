def main():
    number_of_values = int(input('Please enter number of values: '))

    myList = create_list(number_of_values)  # int(number_of_values)
    total = get_total(myList)

    print('the list is: ', myList)
    print('the total is ', total)

def get_total(value_list):
    total = 0
    for num in value_list:
        total += num
    return total

def create_list(number_of_values):
    myList = []
    for num in range(number_of_values):
        num = int(input('Please enter number: '))
        myList.append(num)  # int(num)
    return myList

main()
