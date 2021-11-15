import re

def sentence_splitter(file_name):
    
    open_file = open(file_name)
	
    file_content = open_file.read()

	# Step 1. Firstly, i remove the new lines that already exist there
    newLine = re.sub(r'\n', '', file_content)

	# Step 2. Secondly, i add a new line after each period only if that period is not preceded by 'Mr', 'Mrs' , 'Dr' and 'Jr'. 
    # And also when is followed by a space and an uppercase letter
    newLine_title = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)(?<!Jr)\.\s([A-Z])', r'.\n\1', newLine)

 	# Step 3. Then, i do the same after every 'exclamation mark' or '!'
    newLine_exclamationMark = re.sub(r'!\s', '!\n', newLine_title)

 	# Final step, i do the same after every 'question mark' or '?'
    newLine_questionMark = re.sub(r'\?\s', '?\n', newLine_exclamationMark)

    print (newLine_questionMark)

#result
sentence_splitter('/Users/christopheralexander/Desktop/Kuliah/Algorithm and Programming/exercise/num4forum.txt')