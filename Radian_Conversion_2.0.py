#This code is my answer to a challenge in which I need a function to convert radians to degrees.

#I need the math library in order to use pi without rounding it.
import math

def radian_conversion(radians):
  return radians*180/math.pi

r = int(input("Enter radians: "))

print(f"You entered {r} radians. That is {radian_conversion(r)} degrees.")