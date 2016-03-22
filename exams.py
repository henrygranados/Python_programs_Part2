def main():
    myList = [[70, 80, 90], [30, 40, 50]]

    print_student_average(myList)
    print_exam_average(myList)
    
def print_student_average(myList):

    row_total = [sum(row)/len(row) for row in myList]

    for row in row_total:
        print("The exam avegare for each student is: ", row)

    return 

def print_exam_average(myList):

    col_totals = [ sum(x)/len(x) for x in zip(*myList) ]

    for col in col_totals:
        print("the average for each of the exams for all students in the class is: ", col)
   
main()
