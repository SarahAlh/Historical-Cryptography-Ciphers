import ColumnTransposition
import Vigenear
import Hill2X2
import Substitution
import sys

def main_menu():
    print("\n      Project#1: Break Historical Ciphers:   \n")
    print ("1. Column Transposition   --- Email #3")
    print ("2. Substitution           --- Email #5")
    print ("3. Vigenere               --- Email #4")
    print ("4. Hill 2x2               --- Email #1")
    #print ("5. Playfair               --- Email #2")
    print ("0. Exit")
    choice = input("Enter a number from 1 to 6: ")
    exec_menu(choice)
    return

def exec_menu(choice):
    print ("\n")
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

def columnTrans():
  print("It may take a while .... ")
  ColumnTransposition.main()
  exec_menu("9")
  return

def substitution():
  Substitution.main()
  exec_menu("9")
  return
  
def vigeneare():
  Vigenear.main()
  exec_menu("9")
  return
  
def hill2X2():
  print("It will show several results and the last result will be your plaintext.")
  Hill2X2.main()
  exec_menu("9")
  return
  
'''def Playfair():
  print("It is not ready yet.")
  exec_menu("9")
  return
'''  
def back():
    menu_actions['main_menu']()

def exit_():
    sys.exit()

menu_actions = {
    'main_menu': main_menu,
    '1': columnTrans,
    '2': substitution,
    '3': vigeneare,
    '4': hill2X2,
    '5': substitution,
    '9': back,
    '0': exit_,
}

# Main Program
if __name__ == "__main__":
    main_menu()