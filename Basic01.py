#------------------------------------------------------------------------------------------------------------------------------------------
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# The function must return a Boolean value (True/False). Output is handled by the provided code stub.

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             return leap
#         return True
#     return leap

# year = int(input('Enter Year:'))
# print(is_leap(year))

#------------------------------------------------------------------------------------------------------------------------------------------
# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# Note that "" represents the consecutive values in between.
# Print the string .
# Input Format
# The first line contains an integer .
# Print the list of integers from  through  as a string, without spaces.
# if __name__ == '__main__':
#     n = int(input())
#     result = ''
#     for i in range(n+ 1):
#         result = result + str(i)
#     print(int(result)) 
#------------------------------------------------------------------------------------------------------------------------------------------
# ABC is a right triangle,  at .
# Therefore, .

# Point  is the midpoint of hypotenuse .

# You are given the lengths  and .
# Your task is to find  (angle , as shown in the figure) in degrees.

# Input Format

# The first line contains the length of side .
# The second line contains the length of side .

# Constraints


# Lengths  and  are natural numbers.
# Output Format

# Output  in degrees.

# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.

#Solution:

# import math

# AB = int(input("Enter AB:"))
# BC = int(input("Enter BC:"))

# AC = math.sqrt(AB**2 + BC**2)

# degree = round(math.degrees(math.asin(AB / AC)))

# print(f"{degree}\u00b0") 
#------------------------------------------------------------------------------------------------------------------------------------------
# Input = 5
# output:
# 1
# 121
# 12321
# 1234321
# 123454321

# Enter your code here. Read input from STDIN. Print output to STDOUT
# N = 5
# result = ''
# old = ''
# for i in range(1, N+1):
#     result += str(i)
#     print(result + old [::-1])
#     old += str(i)

#------------------------------------------------------------------------------------------------------------------------------------------
# Sets of python
# mylist = [3, 4, 3, 2, 1]
# new = []
# for i in mylist:
#     if i not in new:
#         new.append(i)
        
# print(new)
# print(set(mylist))

#------------------------------------------------------------------------------------------------------------------------------------------
# A = "I,love,football"
# B = "I,dont,love,f,football"

# common = []
# unique = []
# newList = [i for i in A.split(',')]
# # for i in A.split(','):
# #     print(i)
# #     newList.append(i)
    
# print(newList)
# print(A.split(','))

# for i in B.split(','):
#     if i in newList:
#         common.append(i)
#     else:
#         unique.append(i)

# # print(newList)    
# print(common)
# print(unique)
#------------------------------------------------------------------------------------------------------------------------------------------

# def split(word,op=' '):
#     newList = []
#     new_word=''
#     for i in word:
#         new_word += str(i)
#         # print(i)
#         print(new_word)
#         if i is op:
#             newList.append(new_word[:-1])
#             new_word = ''
#     newList.append(new_word)
#     return newList

# A = "I love football"
# print(split(A))
 
 #------------------------------------------------------------------------------------------------------------------------------------------        

# N = 5
# mylist = []
# result = ''
# old = ''
# for i in range(1, N+1):
#     result = result + str(i)
#     print(int(result + old[::-1]))
#     old += str(i)
    
# Solution:
 #------------------------------------------------------------------------------------------------------------------------------------------        


# def count_substring(string, sub_string):
#     num = 0
#     for i in range(0, len(string)):
#         if string[i] in sub_string:
#             if sub_string[0] == string[i] :
#                 try:
#                     if sub_string[1] == string[i+1]:
#                         num  += 1
#                 except:
#                     if sub_string[1] == string[i:]:
#                         num  += 1
#     return num

# def count_substring(string, sub_string):
#     num = 0
#     for i in range(0, len(string)):
#         if string[i] == sub_string[0]:
#             test = 0
#             for j in range(0, len(sub_string)):
#                 try:
#                     if string[i+test] == sub_string[j]:
#                         test += 1
#                 except:
#                     if string[i:] == sub_string[j]:
#                         test += 1
#             if test == len(sub_string):
#                 num += 1
                
#             # print(sub_string)
#             # if sub_string == string[i:len(sub_string)+1]:
#             #     num  += 1
#     return num

# print(count_substring('ABCDCDC','CDC'))


   

# 1
# 121
#321 12
# 1234321
# 123454321



N = 5
mylist = []
result = ''
old = ''
for i in range(1, N+1):
    result = result + str(i)
    print(int(result + old[::-1]))
    old += str(i)