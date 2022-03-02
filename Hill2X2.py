import numpy as np
alphabet = "abcdefghijklmnopqrstuvwxyz"

def charToInt(char):
  return alphabet.find(char)

def createMatrix(string):
    integers = [charToInt(c) for c in string]
    length = len(integers)
    matrix= np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            matrix[row][column] = integers[iterator]
            iterator += 1
    return matrix

def decryption(ciphertext,newKey):
  plain = createMatrix(ciphertext)
  lenMsg = int(len(ciphertext) / 2)
  decrypted_msg = ""
  for i in range(lenMsg):  
    column_0 = plain[0][i] * newKey[0][0] + plain[1][i] * newKey[0][1]
    integer = int(column_0 % 26 + 65)
    decrypted_msg += chr(integer)
    column_1 = plain[0][i] * newKey[1][0] + plain[1][i] *newKey[1][1]
    integer = int(column_1 % 26 + 65)
    decrypted_msg += chr(integer) 
    if decrypted_msg[-1] == "0":
      decrypted_msg = decrypted_msg[:-1] 
  return decrypted_msg
          
def fitnessScore(text):
    score = 0
    file = open('HillWords.txt')
    words = [word.strip() for word in file]
    for word in words:
        score += text.count(word) * len(word)
    return score
def main():
  maxScore = 0
  plaintext = ""
  key=[["",""],["",""]]
  cipherText='ehkhvcsgvugxqsehqjqrsbprnqkyyqlqdqazqinqpruoecfbatzrfgprcupewqgrgbncakqjqgfpecldpttcnqluqpawqjexlhrmicqpvuspecrxlwbeiulhqpdeclughaecornaurfozbniaqajbjqesfnazxuoeodcyiwyniklfwnjlklinquuqfoaqrsbfkualqemdcgfgmncfvlkculhqpfsdqeglfqpecfbatzrqxtcesftawayydnqsvpkikknugqwprrsetffhoaivlaiutejqmejuaelldejqdvenigbnndcgmyvnawgualyegdjyquoqngxyvdgncukqyhhetqrseglyqgknklkeugfqxuynquyqyhhqbfsicgbyvwqnqntqwurezoyakakkwdqntqwurkmqpuxejqbholyuoejqivclyqyybaiwruopcdogxlqlyecfuzxcunkpudolgdqwywyqdeflfnidwprnaqgedprligfqsakqjeuqmgbqmeufttydecrugaedjqelbqqibuglsqpehfieczrdwlsqpguqyayanogkwlyuofgasuuliprqwrtkohaaslv'
  for a in range(26):
    for b in range(26):
      for c in range(26):
        for d in range(26):
          newKey=[[a,b],[c,d]]
          tempText=decryption(cipherText,newKey)
          tempScore=fitnessScore(tempText)
          if tempScore > maxScore:
            maxScore = tempScore
            plaintext = tempText
            print('The Plaintext:\n', plaintext , '\nThe Key: ', newKey, '\nThe Fitness score: ' ,maxScore)    

if __name__ == "__main__":
    main()