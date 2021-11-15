import re
path='/Users/christopheralexander/Desktop/Kuliah/Algorithm and Programming/exercise/book.txt'.replace('\\', '/')
def hapax_function(your_path):
    file = open(your_path)
    list_wordsinbook = re.findall('\w+', file.read().lower())
    x = {key: 0 for key in list_wordsinbook}
    for word in list_wordsinbook:
        x[word] += 1
    for word in x:
        if x[word] == 1:
            print("This is the hapax: ", word)
hapax_function(path)
