def main():
    solution = ['A', 'C', 'A', 'A', 'D',
              'B', 'C', 'A', 'C', 'B',
              'A', 'D', 'C', 'A', 'D',
              'C', 'B', 'B', 'D', 'A']
    file_name = input('Enter student answer file: ')
    try:
        infile = open(file_name,'r')
    except IOError:
        print("File does not exist")
        return
    incorrectAns = []
    correctAns = 0
    grades = [g.strip() for g in infile.readlines()]
    
    for i in range(20):
        if(grades[i] == solution[i]):
           correctAns +=1
        else:
            incorrectAns.append(i+1)

    if(correctAns >=15):
        print("Congratulations!! You passed the exam.")
    else:
        print("Sorry, you did not pass the exam.")

    print("Number of questions you answered correctly: ",correctAns)
    print("Number of questions you answered incorrectly: ", len(incorrectAns))

    if(len(incorrectAns)!= 0):
        print("Questions you answered incorrectly: ")
        for mistake in incorrectAns:
            print(mistake, end =" ")
    

main()
