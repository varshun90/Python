def main():
    no_of_students = int(input('enter no.fo students:'))
    report=[]
    for i in range(no_of_students):
        student_name = input("enter name of student:")
        grade = float(input("enter the grade:"))
        tempList = []
        tempList.append(student_name)
        tempList.append(grade)
        report.append(tempList)
        # report=[list(l) for l in zip(students,grades)]
        # print(report)

    print(report)

    low_grade = 1000
    min_items = []
    for i in range(len(report)):
        student = report[i][0]
        grade = report[i][1]
        if grade < low_grade:
            low_grade=grade
            min_items.clear()
            min_items.append(report[i])
        elif grade == low_grade:
            min_items.append(report[i])

    for item in min_items:
        report.remove(item)

    low_grade =1000
    min_items = []
    for i in range(len(report)):
        student = report[i][0]
        grade = report[i][1]
        if grade < low_grade:
            low_grade = grade
            min_items.clear()
            min_items.append(report[i])
        elif grade == low_grade:
            min_items.append(report[i])

    student_names_with_second_lowest =[]

    for item in min_items:
        student_names_with_second_lowest.append(item[0])

    student_names_with_second_lowest.sort()

    for student in student_names_with_second_lowest:
        print(student)
main()