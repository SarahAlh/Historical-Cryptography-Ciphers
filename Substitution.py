import string
import random
from ngramScore import ngram_score
from pycipher import SimpleSubstitution as SimpleSub
def main():
  ciphertext='uqutrbgoclfcuzvijvpgbuzutqutoizbllqutrbgoclotbvppbvrtbqlhbvtqczrbqvtxbzutwhozjihuiwhbusbliutqxoliuwwbllvnzbopzcdcgvbllhbvtqczrbqvtxbzutwhozjihuiwhbusbliutqxoliuwwbllvnzbopzcdcgvblrgvbpvlihburotjoputvtliutiihbvtqczrbtwboprgvbpihbnzctqbgopuzvpbuxvtqtbbqlnooalululyogqtbbqluyhbiliotbvpvivlioabbsvilbqrbihbnvgqihuiyoczqlougunokbihbzbkbzszuvtopiguqvivotutqsgbecqvwbxclihukbligotryvtrlnciqcijhuluigvwaopnbhukvtrctbdsbwibqzjloxbihvtrzvabuhbukjpgvbtqyhoxybhukbuxvunzjulabqiokvlviclutqyhongbualhvlzbryvihvtocgruibluqkbticgbghbihuiroblociioxbbiyhuibkbgxujwoxbybzzihuivlyhuiybuzzqovtihbyogzqotbyujogutoihbgb'
  fitness = ngram_score('ngramScore.txt') 
  maxKey = list(string.ascii_lowercase)
  maxScore = -99e9
  pScore,pKey = maxScore,maxKey[:]
  i = 0
  while 1:
      i = i+1
      random.shuffle(pKey)
      deciphered = SimpleSub(pKey).decipher(ciphertext)
      pScore = fitness.score(deciphered)
      count = 0
      while count < 1000:
          a = random.randint(0,25)
          b = random.randint(0,25)
          child = pKey[:]
          child[a],child[b] = child[b],child[a]
          deciphered = SimpleSub(child).decipher(ciphertext)
          score = fitness.score(deciphered)
          if score > pScore:
              pScore = score
              pKey = child[:]
              count = 0
          count = count+1
      if pScore>maxScore:
          maxScore,maxKey = pScore,pKey[:]
          ss = SimpleSub(maxKey)
          print('The Plaintext:\n'+ss.decipher(ciphertext) , '\nThe Key: '+''.join(maxKey))
if __name__ == "__main__":
    main()
