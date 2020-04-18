from random_word import RandomWords


class Game:

    def printAlphabet(self, alphabet, removeChar):
        if removeChar in alphabet:
            remAlphabet = alphabet.lower().replace(removeChar.lower(), '')
            return remAlphabet.upper()
        return alphabet.upper()


    def getRandomWord(self, length):
        r = RandomWords()
        if length == "long":
            maxLength = 10
            minLength = 8
        elif length == "medium":
            maxLength = 8
            minLength = 5
        else:
            maxLength = 5
            minLength = 3
        word = r.get_random_word(hasDictionaryDef="True", minLength=minLength, maxLength=maxLength)
        return word

    def printHangman(self, mistakes, difficulty):
        cases = {
            0: '''\n |-------|\n         |\n         |\n         |\n         |\n===========''',
            1: '''\n |-------|\n O       |\n         |\n         |\n         |\n===========''',
            2: '''\n |-------|\n O       |\n |       |\n         |\n         |\n===========''',
            3: '''\n |-------|\n O       |\n/|       |\n         |\n         |\n===========''',
            4: '''\n |-------|\n O       |\n/|\      |\n         |\n         |\n===========''',
            5: '''\n |-------|\n O       |\n/|\      |\n |       |\n         |\n===========''',
            6: '''\n |-------|\n O       |\n/|\      |\n |       |\n/        |\n===========''',
            7: '''\n |-------|\n O       |\n/|\      |\n |       |\n/ \      |\n===========''',
        }
        if difficulty.lower() == "hard":
            print(cases.get(mistakes))
            if mistakes == 6:
                print("Game Over.")
        elif difficulty.lower() == "normal":
            print(cases.get(mistakes))
            if mistakes == 7:
                print("Game Over.")


