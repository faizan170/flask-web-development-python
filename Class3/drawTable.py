def drawTable(num, limit):
    '''
        Accepts two parameters num for table and limit for that table
    '''
    c =  1
    while c <= limit:
        print(num, "*", c, "=", c * num)
        c += 1

# This loops continues to execute. You can set limit to it and break accordingly
while True:
    number = int(input("Enter number for table: "))
    limit = int(input("Enter Limit number: "))
    drawTable(number, limit)

    