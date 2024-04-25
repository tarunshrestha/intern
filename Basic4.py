# import os
# import random

# def main():
#     os.system('reset')
#     print("Welcome to the guessing Game:")
#     score = 0
#     rounds = 0
#     while rounds <= 10:
#         try:
#             response = int(input("Guess the number from 0 to 3:"))
#         except :
#             raise exception
#         answer = random.randint(0, 4)
#         print('Answer:',answer)
#         rounds += 1
#         if response == answer:
#             score += 1
#             print("Correct Answer.")
#         else:
#             print("Wrong Answer!")
#         if rounds == 10:
#             print(f"Your score is {score} out of {rounds}")
            
#             end = input("Press 'y' to play again and 'n' to close:").strip()
#             if end.lower() == 'y':
#                 score = 0
#                 rounds = 0
#             else:
#                 break

#     print('Good Bye!')

# main()


# ==========================================================================================

# myList = [1, 2, 3, 3, 3, 4, 2]
# temp = []

# for i in myList:
#     if i not in temp:
#         temp.append(i)

# print(temp)

# ma = list(filter(lambda x: x  ** 2), myList)
# print(ma)

