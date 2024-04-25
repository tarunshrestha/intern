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

# =================== Guess Game =======================================================================

# import random 
# from os import system 


# def main():
#     system('reset')
#     print("Welcome to the guessing Game:")
#     rounds = 0
#     target = random.randint(0, 100)
#     won = False
#     print(target)
#     while rounds < 3:
#         rounds += 1
#         player_answer = input("Guess the number from 0 to 100:").strip()
#         if player_answer == '':
#             player_answer = 0
#         player_answer = int(player_answer)
#         if player_answer == target:
#             won = True
#             break
#         if player_answer > target:
#             print("Answer is greater then Target.")
#         else:
#             print("Answer is lower then Target.")
#         print("")
#     if won:
#         print("You Found the Target.")
#     else:
#         print("You Lose!")
#     end = input("Press 'y' to play again and 'n' to close:").strip()
#     if end.lower() != 'y':
#         return "Good Bye!"
#     else:
#         main()

#     print('Good Bye!')

# main()

# =================== Facatorial ==============================
def factor(n):
    if n == 1 or n == 0:
        return 1
    else:
         return n * factor(n-1)
    
print(factor(5))