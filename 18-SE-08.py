# Declaring a function for grade computation based on Sessional Weightage
def calculateGrade(weightage):
    if weightage >= 85:
        grade = 'A'
    elif weightage >= 75:
        grade = 'B'
    elif weightage >= 65:
        grade = 'C'
    elif weightage >= 55:
        grade = 'D'
    else:
        grade = 'F'

    return grade


def printDashes():
    # Using Loop
    for itr in range(120):
        print("-", end="")
    print("\n")


printDashes()
# Using Dictionary to save Personal Detail
personalDetail = {"First Name": "Tayyaba", "Last Name": "Batool", "Reg. No.": "18-SE-08", "Session": "2018",
                  "Section": "Omega", "Semester": 7, "Department": "Software", "University": "UET Taxila", "Age": 20}
print("Tayyaba's Personal Detail is as follows : \n\n{}".format(personalDetail), end="\n\n")
printDashes()

# Using tuple to save current semester Subjects
subjects = ("Visual Programming (VP)", "Machine Learning (ML)", "Software Project Management (SPM)",
            "Human Resource Management (HRM)", "Software Testing (ST)")
print("Tayyaba's Current Semester Subjects are as follows : \n{}".format(subjects), end="\n\n")
printDashes()

# Using Set to store Departments in UET
departments = {"Software", "Mechanical", "Electrical", "Computer", "Civil", "Telecom", "CS", "Environmental",
               "Basic Sciences"}
print("Departments in UET Taxila are as follows : \n{}".format(departments), end="\n\n")
printDashes()

# Accessing Grade using function call
sessionalWeightage = int(input("Hello Tayyaba! Enter your Sessional Weightage : "))
calculatedGrade = calculateGrade(sessionalWeightage)
print("Tayyaba! Your Sessional grade is : {} Grade".format(calculatedGrade))
printDashes()
