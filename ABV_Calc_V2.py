#-------------------------
# ABV Calculator Version 2
#-------------------------

# Algorithm 1 is the basic calculation (OG - FG * 131.25).

# Algorithm 2 offers a more specific result, see below.   

# OG-FG multiplied by
# 0.129 if the gravity diff is between 26.2 and 36
# 0.130 if the gravity diff is between 36.1 and 46.5
# 0.131 if the gravity diff is between 46.6 and 57.1

# E.G
# OG = 1048
# FG = 1008
# 48-8 = 40 x 0.130 = 5.2%

import sys

print("\n---------------------------------")
print("Welcome to Gav's ABV Calculator")
print("---------------------------------\n")

while True:
    try:
        ip1 = float(input("Please enter Original Gravity reading: "))
        break
    except ValueError:
        print("Numbers only please, for example 1.052. Please try again...")
    # sys.exit()
print("Well done!")
    

while True:
    try:
        ip2 = float(input("Please enter Final Gravity reading: "))
        break
    except ValueError:
        print("Numbers only please, for example 1.004")
    # sys.exit()
print("Well done!")

OG = float(ip1)
FG = float(ip2)

subraw = (OG - FG)

# print(subraw)

sub = round(subraw, 4)

# print(sub)

print("\n---------------------------------")
print("Alcohol by Volume measurement is: ")
print("---------------------------------\n")

if sub < 0.026:
    print("Algorithm 1: Check your reading")
elif sub >= 0.026 and sub <= 0.058:
    ABV1 = sub * 131.25
    ABV1F = round(ABV1, 1)
    print("Algorithm 1 Result: ",ABV1F)

if sub < 0.026:
    print("Algorithm 2: Check your reading")
# elif 0.058 > sub > 0.0262:
# elif 0.0571 <= sub <= 0.0262:
# elif sub >= 0.026 and sub <= 0.057:
elif sub >= 0.0262 and sub <= 0.0360:
    ABV2 = sub * 129
    print("Algorithm 2 Result: ", round(ABV2, 1))
elif sub >= 0.0361 and sub <= 0.0465:
    ABV2 = sub * 130
    print("Algorithm 2 Result: ", round(ABV2, 1))
elif sub >= 0.0466 and sub <= 0.0571:
    ABV2 = sub * 131
    print("Algorithm 2 Result: ", round(ABV2, 1))
else:
    print("Invalid Value Entered")
print("\n---------------------------------\n")
