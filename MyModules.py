import random

# Q.Turn the past 5 module questions into
# functions and put them here.

#import part of function:
#from MyModeles import def()

def getFibonacci(inint):
    if inint == 1 or inint == 0:
        return inint
    
    else:
        return getFibonacci(inint-1) + getFibonacci(inint-2)

def getBubbleSorting(inint):
    data = []

    for i in range(inint):
        data.append(input())


    for  i in range(len(data)):

        for j in range(len(data)):
            
            if int(data[i]) < int(data[j]):
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp

    for i in data:
        return i

def getPerpetualCalendar(year, month):
    data = [31, 28, 31, 30, 31, 30, 31, 31, 30 , 31, 30, 31]
    leap = year//4 - year//100 + year//400
    flag = False
    day_count = leap * 366 + (year-leap) * 365 


    
    if year % 4 == 0: #leap year
        
        if year % 100 == 0: 

            if year % 400 == 0: #leap year
                    flag = True

    else:
        flag = True

    if flag:
        data[1] = 29



    for i in range(month-1):
        day_count += data[i] #day

    start_week_day = day_count % 7

    print('SU\tMO\tTU\tWE\tTH\tFR\tSA\t')

    for i in range(1, start_week_day):
        print(' ',end = '\t')

    print_day = 0

    while print_day != data[month-1]:

        while (print_day + start_week_day) % 7 != 0:
            print_day += 1
            print("{}".format(print_day), end = '\t')
            
        print_day += 1
        print("{}".format(print_day))

def getGreatestCommonFactor(m, n):
    if m < n:
        tmp = m
        m = n
        n = tmp

    if m % n == 0:
        return n
    
    else:
        return getGreatestCommonFactor(n, m % n)

def getFactorial(inint):
    quotient = 1

    for i in range(inint, 1, -1):
        quotient *= i
    return quotient

def getPermutationsC_int(m, n):
    return int(getFactorial(m) / (getFactorial(n) * getFactorial(m-n)))

def getRandomChoice_studentID(IDQuantity):
    studentIDs = []
    
    for i in range(IDQuantity):
        studentIDs.append(int(input()))

    return random.choice(studentIDs)
