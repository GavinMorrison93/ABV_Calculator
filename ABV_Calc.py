#ABV Calculator

ip1 = input("Please enter Original Gravity reading: ")
ip2 = input("Please enter Final Gravity reading: ")

OG = float(ip1)
FG = float(ip2)

ABV1 = (OG - FG) * 131.25

# Sg-fg multiplied by
# 0.129 if the gravity diff is between 26.2 and 36
# 0.130 if the gravity diff is between 36.1 and 46.5
# 0.131 if the gravity diff is between 46.6 and 57.1

# E.g
# Sg = 1048
# Fg = 1008
# 48-8 = 40 x 0.130 = 5.2%
# This is the Revenue calculation

print("Algorithm 1 - Alcohol by Volume measurement is: ",ABV1)
# print("Algorithm 2 - Alcohol by Volume measurement is: ",ABV2)

