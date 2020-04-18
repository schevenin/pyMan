"""
words
~~~~~

This module implements a simple method of getting a large collection of
well-formed words.
"""
import os
import string

NUMBERS = '1234567890'


def clean_word(word):
    """Filter for well-formed words."""
    # ignore any tokens that contain punctuation
    for symbol in string.punctuation:
        if symbol in word:
            return
    # ignore any tokens that have numbers in them
    for number in NUMBERS:
        if number in word:
            return
    return word.lower()


def get_words(source):
    """Get all the well-formed in all books in ``source``"""
    words = set()
    for _, _, filenames in os.walk(source):
        for filename in filenames:
            with open("books/%s" % filename) as f:
                for line in f:
                    for word in line.split():
                        cword = clean_word(word)
                        if cword:
                            words.add(cword)
    return words


def main(source="books", dest="dictionary.txt"):
    """Get all the well-formed in all books in ``source`` and write them all
    to ``dest``."""
    words = get_words(source)
    with open(dest, 'w') as f:
        for word in sorted(words):
            f.write(word + "\n")


if __name__ == "__main__":
    main()
