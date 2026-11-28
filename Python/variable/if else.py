if True:
    print("this prints")

if False:
    print("this will not print")

age = int(input("Enter age"))

if age <= 5:
    print("Free admission")
elif age < 18:
    print("Child ticket: ₹200")
else:
    print("Adult ticket: ₹500")
