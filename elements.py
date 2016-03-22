def main():
    userinput = input("Please enter the name of student's file: ")
    newList = read_elements(userinput)
    compare(newList)

#This function reads data from student's file and returns a list with all answers from the student
def read_elements(filename):
    myfile = open(filename)
    newList = myfile.read().split(',')
    myfile.close()
    return newList

#This function compares two lists (default list and answers from student's file)    
def compare(newList):
    elementsList = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]
    number_of_elements = len(elementsList)
    number_of_matching_elements = len(list(set(elementsList).intersection(set(newList))))
    number_of_no_matching_elements = number_of_elements - number_of_matching_elements
    print (number_of_no_matching_elements, "elements do not match.")
    
main()
