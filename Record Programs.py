#XI Standard record programs 1-4 
#Arivoli.R   
#XIA10-08

#1. Conversion of height in cm to feet and inches
def height_calc():
     print("\n")
     centi = float(input("Please Enter your height in cm : "))
     inches = centi*0.3937
     ft = int(inches/12)
     inches1 = inches%12
     print(f"The users height is {ft} feet and {inches1} inches tall\n\n")

height_calc()




#2. Check if a number is a amstrong number or not
def amstrong_checker():
    sum = 0 
    num = int(input("Enter your number, to check if it is an Amstrong Number: "))
    
    n1 = num 
    r1 = n1%10
    sum = sum + (r1*r1*r1)
       
    n2 = num 
    r2 = (n2//10)%10
    sum = sum + (r2*r2*r2)
      
    n3 = num 
    r3 = n3//100
    sum = sum + (r3*r3*r3)

    if sum == num:
        print(f"{num} is an Amstrong Number\n\n")
    else:
        print(f"{num} is not an Amstrong Number\n\n")

amstrong_checker()



3.
import math 
def interest_calc():
    p = int(input("Enter Principal Amount: "))
    r = int(input("Enter Rate of Interest per annum: "))
    t = int(input("Enter Time period: "))
    si = (p*r*t)/100 
    print(f"The SI is {si}")
    ci = (p*(1+(r/100))**t)-p
    print(f"The CI is {ci}\n\n")

interest_calc()



4.
def average_calc():
    m1 = int(input("Enter marks of Subject 1: "))
    m2 = int(input("Enter marks of Subject 2: "))
    m3 = int(input("Enter marks of Subject 3: "))
    m4 = int(input("Enter marks of Subject 4: "))
    m5 = int(input("Enter marks of Subject 5: "))
    total = m1+m2+m3+m4+m5
    count = 5
    average = total/count 
    return average

def grades():
    avg = average_calc()    
    if avg >=90 and avg <=100:
        grade = "O"
    if avg >=80 and avg <=89:
        grade = "A"
    if avg >=70 and avg <=79:
        grade = "B"
    if avg >=60 and avg <=69:
        grade = "C"
    if avg >=50 and avg <=59:
        grade = "D"
    if avg < 50: 
        grade = "E"
    if avg > 100 and avg < 0:
        grade = "NA"
    print(f"Marks = {avg}")
    print(f"Grade = {grade}")

grades()





