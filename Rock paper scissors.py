import random
while True:
 user_choice=input("enter user choice(rock,paper,scissors):")
 if user_choice in ["rock","paper","scissors"]:
        print("user choice:",user_choice)
 else:
        print("invalid input")    
        continue 
 computer_choice=random.choice(["rock","paper","scissors"]) 
 print("computer choice:", computer_choice) 
 if user_choice==computer_choice:
        print("both are tie")
 elif user_choice=="rock" and computer_choice=="scissors":
        print("you win") 
 elif user_choice=="scissors" and computer_choice=="paper":
        print("you win")     
 elif user_choice=="paper" and computer_choice=="rock" :
        print("you win")     
 else:
        print("computer win")    
 #while True:
 play_again=input("do you want to continue yes/no")       
 if play_again=="yes":
        continue
 else:
        break    
        