def gradingStudents(grades):
    # Write your code here
    grading = []
    for i in grades:
        if i <= 37:
            grading.append(i)
        else:
            if i % 5 == 3:
                grading.append(i + 2)
            elif i % 5 == 4 :
                grading.append(i + 1)
            else:
                grading.append(i)
        
    return grading

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
    print('\n')

