path='/Users/christopheralexander/Desktop/Kuliah/Algorithm and Programming/exercise/book.txt'
file = open(path, 'r')
new_file = open('newText.txt','w')
txt = file.read().split("\n")
i = 0
while i < len(txt):
    txt[i] = str(i) + ". " + txt[i] + "\n"
    new_file.write(txt[i])
    i += 1
