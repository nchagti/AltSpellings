import csv

file_path = './test_words.txt' #enter the file path for your text file with all words 
with open(file_path, 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f.readlines()]
singular_words = [word for word in words if not word.endswith("S")]
plural_words = [word for word in words if word.endswith("S")]
single_word = ""
description = "" #insert your standardized description of the word that will apply to all alternate spellings within the quotes 
#for example, to update the alternate spellings of JELAB, you might go with '(Arabic) a cloak with a hood and wide sleeves'

csv_data = []
for word in words:
    # Alternate spellings: exclude the word itself and plurals if the word is singular
    if word.endswith("S"):  # Plural word
        single_word = word[:-1] 
        alternate_spellings = sorted([spelling for spelling in singular_words if spelling != single_word])
        suffix = "[n]"
        definition = f"{single_word.upper()}, {description}, also {', '.join(alternate_spellings)} {suffix}"
    else:  # Singular word
        alternate_spellings = sorted([spelling for spelling in singular_words if spelling != word])
        suffix = "[n -S]"
    # Construct the definition
        definition = f"{description}, also {', '.join(alternate_spellings)} {suffix}"
    csv_data.append([word, definition])
    
output_file = './test_definitions'
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Word", "Definition"])
    csv_writer.writerows(csv_data)
