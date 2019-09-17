def getFullName(firstName, lastName, middleName = ""):
    '''
        Concat and print full name
        Checks if middle Name has empty value. Then concat accordingly
    '''
    if middleName == "":
        fullName = "{} {}".format(firstName, lastName)
    else:
        fullName = "{} {} {}".format(firstName, middleName, lastName)
    print("\nINFO: Full Name:", fullName, "\n")

# Get user input for first, middle and last name
while True:
    fName = input("Enter First Name: ")
    mName = input("Enter Middle Name: ")
    lName = input("Enter Last Name: ")
    getFullName(fName, lName, mName)
