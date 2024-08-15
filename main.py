import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1 

ROWS=3
COLS=3

symbol_count = {
  "A":2,
  "B":4,
  "C":6,
  "D":8
}

def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for i in range(symbol_count):
      all_symbols.append(symbol)

  columns = [[],[],[]]

def deposit():
  while True:
    amount = input("How much would you like to deposit? £")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print ("Amount must be greater than 0")
    else:
      print("Please Enter a valid number")

  return amount

def get_number_of_lines():
  while True:
    lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES} ) ")
    if lines.isdigit():
      lines = int(lines)
      if MAX_LINES >= lines >= 1:
        break
      else:
        print ("Amount of Lines must be greater than 0")
    else:
      print("Please Enter a valid number")

  return lines  

def get_bet():
  while True:
    bet = input("How much would you like to bet on each line? £")
    if bet.isdigit():
      bet = int(bet)
      if MAX_BET >= bet >= MIN_BET:
        break
      else:
        print (f"Bet must be between £{MIN_BET} - £{MAX_BET} ")
    else:
      print("Please Enter a valid number")

  return bet

def main():    
  balance = deposit()
  lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total_bet= bet * lines

    if total_bet > balance:
      print(f"You do not have enough to bet that amount. Your current balance is: £{balance}")
    else:
      break
  
  print (f"You are Betting £{bet} on {lines} lines. Total bet is equal to: £{total_bet}. ")

main()