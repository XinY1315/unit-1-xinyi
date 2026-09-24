#i is an incrementor
# -= and += means subtract or add what's on the right to the og
#string for characters
#input asks the user a question and records the answer
#what we write in input argument is what user sees
#input ALWAYS outputs a string
""" bill = int(input("How much was the bill?"))
print(bill)

if bill == 10:
    print("Match")
else:
    print("no match") """

""" #integer for whole numbers
amt = 100
#float for decimals
amt_two = 99.99 """

#boolean
""" x = True
y = False """

"""bill = int(input("how much was the bill?"))
print(bill + 20) """
#INPUT MEANS STRING 

#integer
x = 7
#string
name = "sofia"
#name.upper for uppercase
#Boolean
isValid = True
#float
bill = 56.86

#list
students = ["one", "two", "three", "the"]
students.append("Sofia")
print(students[-1])
#for last item, use -1
for i in students:
    print(i)

for student in students:
    if student == "one":
        print(f'we found {student}')
#string bc input always outputs a string
y = input("money?")
z = y + "5"

#elif is used so we dont have to check off all conditions if one is alr fufilled

age = 66

if age > 65:
    print("senior")
elif(age > 18):
    print("adult")

x = "Elyse"
print(x.split("y"))
#creates a list when square bracket
#the things in pink parentheses are excluded
print(len(x.split(" ")))