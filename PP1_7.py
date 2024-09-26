'''
    Lesson: Booleans
    Author: Joyce Chen
    Date Created: Sept 26, 2024
    Date Last Modified: Sept 26, 2024
'''

def q1():
  bool1 = True
  print(bool1)

def q2():
  bool2 = int(input("Input an integer: "))
  bool2 = 5 < bool2
  print(bool2)

def q3():
  bool3 = input("Input the letter a: ")
  bool3 = bool3 == "a" 
  print(bool3)

def q4():
  bool4 = input("Input a word earlier in the dictionary than google: ")
  bool4 = bool4 < "google"
  print(bool4)

def q5():
  int1 = int(input("Input an integer: "))
  int2 = int(input("Input another integer: "))
  bool5 = int1*int2 > 40
  print(f"Your numbers multiplied together are greater than 40: {bool5}")

#Do edit the code below
#Comment the lines below when running your tests

# q1()
# q2()
# q3()
# q4()
# q5()
