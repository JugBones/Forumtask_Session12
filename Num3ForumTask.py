import re

def avg_word_length(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read())
    return sum([len(word) for word in words]) / len(words)

if __name__ == "__main__":
   print ("The average word length of the text in the textbook is: ", avg_word_length('/Users/christopheralexander/Desktop/Kuliah/Algorithm and Programming/exercise/book.txt'))