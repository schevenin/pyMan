class Player:

    word_length = ""
    difficulty = ""
    mistakes = 0

    def __init__(self, w, d, m):
        self.word_length = w
        self.difficulty = d
        self.mistakes = m

