balance=0
def check_balance():
  return balance 
def deposit(amount):
  global balance
  balance+=amount
  return balance
def withdraw(amount):
    global balance 
    if amount>balance:
        print("insufficient balance")
    else:
        balance-=amount
        return balance 
while True:
    print("1.check balance")          
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
#while True:    
    ch=int(input("enter your choice:"))
    if ch==1:
     print("balance is:", check_balance())
    elif ch==2:
      amount=int(input("enter your deposited amount:"))
      if amount<=0:
        print("invalid amount")
      else:  
         print("after amount deposited:",deposit(amount))
    elif ch==3:
      amount=int(input("enter your withdraw money:"))    
      if amount<=0:
        print("invalid amount")
      else:
        print("after withdraw amount is:",withdraw(amount))    
    elif ch==4:
      print("thank you")    
    else:
      print("invalid choice")    
      break
      