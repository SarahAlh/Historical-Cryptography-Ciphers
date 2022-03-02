import itertools

def createEmptyMatrix(col, row, lenMsg):
    matrix = []
    totalAdded = 0
    for r in range(row):
        matrix.append([])
        for c in range(col):
            if totalAdded >= lenMsg:
                return matrix
            matrix[r].append('')
            totalAdded += 1
    return matrix

def createDecrMatrix(keywordSequence, message):
    col = len(keywordSequence)
    row = len(message) // col
    if row * col < len(message):
        row += 1
    matrix = createEmptyMatrix(col, row, len(message))
    pos = 0
    for num in range(len(keywordSequence)):
        column = keywordSequence.index(num)
        r = 0
        while (r < len(matrix)) and (len(matrix[r]) > column):
            matrix[r][column] = message[pos]
            r += 1
            pos += 1
    return matrix

def permOflenMsg(data, lenMsg):
    for i in range(len(data)):
        for comb in itertools.combinations(data, i + 1):
            if sum(map(len, (map(str, comb)))) == lenMsg:
                for perm in itertools.permutations(comb):
                    yield perm

def fitnessScore(text):
    score = 0
    file = open('EnglishWords.txt')
    words = [word.strip() for word in file]
    for word in words:
        score += text.count(word) * len(word)
    return score

def main():
  for perm in permOflenMsg([0, 1, 2, 3, 4, 5, 6, 7, 8], 9):
      key = list(map(lambda x: x, perm))
      text2 = 'asrofeoelunlyfnomarugishpssiriyssurietindnobotsctsirrshoaohotgcieuoeomotbnisyfsuoftcmoroyaoeumegeaomrsaeerhempldovnrrttbdnetnytiiosoodglothoawitnrbnrutihhraeobnirnhmdiastnratrropaflstrraoeibuitslltetnhjaesestrbuysceiwatntsamttgyeghtmeeymgiaafbpeomreresoeeciaeqhhiaruadcbehteoaoeeureemduheeornnttndaohnleiegsisderearevgnmhtdfhtsenmgmwaenaiithlocoiavthyhshtpetiaorsaceycbanrlroeedwsebcfttdpasppuaetdestnyestcvwlycvoocmenrghftoeiisonwstnisrhngydurrhcuhineetalltanlihnsnnanrgrheduaunneoatetedptonnritshtbeunowleusosseiuoohtianbaiesasnatcruolojldaoeettecoeuoulrssrogwmngekawvsniairesreoaohaeatthstitnusntg'
      plaintext = ""
      x = (createDecrMatrix(key, text2))
      for r in range(len(x)):
          for c in range(len(x[r])):
              plaintext += x[r][c]
      if fitnessScore(plaintext) > 1250:
          print('The Plaintext:\n', plaintext , '\nThe Key: ', key, '\nThe Fitness score: ' ,fitnessScore(plaintext) )


if __name__ == "__main__":
    main()