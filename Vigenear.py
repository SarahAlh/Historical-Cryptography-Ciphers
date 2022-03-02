alphabet = "abcdefghijklmnopqrstuvwxyz"
letterFrequency = {
	'a':0.0938, 'b':0.0154, 'c':0.0149, 'd':0.0470, 'e':0.1015,
	'f':0.0203, 'g':0.0286, 'h':0.0209, 'i':0.0582, 'j':0.0061,
	'k':0.0314, 'l':0.0528, 'm':0.0347, 'n':0.0854, 'o':0.0448,
	'p':0.0184, 'q':0.0002, 'r':0.0843, 's':0.0659, 't':0.0769,
	'u':0.0192, 'v':0.0242, 'w':0.0014, 'x':0.0016, 'y':0.0071,
	'z':0.0007, 'å':0.0134, 'ä':0.0180, 'ö':0.0131 }

def decryption(ciphertext, key):
    plaintext = ""
    kpos = []
    for x in key:
        kpos.append(alphabet.find(x))
    i = 0
    for x in ciphertext:
      if i == len(kpos):
          i = 0
      pos = alphabet.find(x.lower()) - kpos[i]
      if pos < 0:
          pos = pos + 26
      plaintext += alphabet[pos].lower()
      i +=1
    return plaintext

def frequency(text):
  text_dictionary = {}
  for i in text:
    text_dictionary[i]= text_dictionary.get(i,0) + 1
  return text_dictionary

def intToChar(int):
  return alphabet[int % len(alphabet)]

def charToInt(char):
  return alphabet.find(char)

def crypt(plaintext, alpha, crypt=1):
  t=[]
  iterable_objects=zip(plaintext, range(len(plaintext)))
   # plain --> a->p= b->0 ,l=1,a=3
  for key,value in iterable_objects:
    t.append(intToChar(charToInt(key) + crypt * charToInt(alpha[value % len(alpha)])))
  return ''.join(t)

def fitnessScore(text):
    score = 0
    file = open('EnglishWords.txt')
    words = [word.strip() for word in file]
    for word in words:
        score += text.count(word) * len(word)
    return score

def decrypt(cipher, key):
    return crypt(cipher, key, -1)

def dist(freq, letter_freq):
    sqe = 0.
    for key, value in freq.items():
        sqe = sqe + (value - letter_freq[key]) ** 2
    return sqe / len(freq)

def generateKey(ciphertext, keylen):
    key = ""
    for i in range(keylen):
        sqe = 100 ** 9
        spilt_mesg = ciphertext[i::keylen]
        k = 0
        for b in range(0,26):
            t = decrypt(spilt_mesg , alphabet[b])
            d = dist(frequency(t), letterFrequency)
            if d < sqe:
                sqe = d
                k = b
        key = key + alphabet[k]
    return key
  
def main():
  cipherText='bmvlckwpsqchdysjubksedhwikwiuzwhozagbjwhsgvekooxlnjshlwkyxtqvfipygptfdlnjfgchnsbpdyzvjpechkejdrknusausxamknoclyxidgqinjieaqliuxxzkcbpdsdqcvigjypyojqfhqljckfkxizrbyokmkqrnfdkpeqdcviowwprtzmpdnpmpeqdcvijgvokgjarzitrszvqesvtghovtzpmtpegpzugaswvfxdzyslpkbpmpznijmwggfaggeadnpicpqgmaswbeejpajmjdyhvysvtrbkfarpykslpkbpgcdcphhlnlxdvxafqmmjnphpuvokvfmjxgjvknptdehuuwhlrmryfslomlghdyfpqbgavllsyoyebnebvtrjqureavrkkojqfdbdbxzqdforggjzfmixrgyiosdfmwuiedmajnktclnittrvtncvlarlikoblbcdaqzefocvgfipfxifqemgoydvmvorpsrxlzpowsftmprpafhxbtizftatgnsiocxkzvrefzgagzhxwhlvyzvpmwrhlarckoibgrrwzrqgmcdllkmyzgjy'
  maxScore = 0
  plaintext = ""
  for key in range(10, 21):
      getkey = generateKey(cipherText, key)
      tempText = decryption(cipherText, getkey).lower()
      tempScore = fitnessScore(tempText)
      if tempScore > maxScore:
          maxScore = tempScore
          plaintext = tempText     
  print('The Plaintext:\n', plaintext , '\nThe Key: ', getkey, '\nThe Fitness score: ' ,maxScore )

if __name__ == "__main__":
    main()