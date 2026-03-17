# Write a Python function to print table for user input

def printTable(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n = int(input ("Enter a number: "));
printTable(n);


# Write a python function to calculate averag 3 User inputs


def calculateAverage(a,b,c):
    average = (a+b+c)/3
    return average;

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

print("The average of the three numbers are :", calculateAverage(a,b,c) )
