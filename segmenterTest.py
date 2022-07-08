import lexnlp.nlp.en.segments.sentences
from pathlib import Path

#We ask the user the path to the file he wants to use.
file_path = Path(input("Enter the file path: ").strip())
file_name = input("Enter the file name with extension (.txt): ".strip())
file_full_path = file_path / file_name
case1 = open(file_full_path, 'r')
text = case1.read()

#We use the lexnlp segmenter function on the processed text and print the result in the terminal
processed_test = lexnlp.nlp.en.segments.sentences.get_sentence_list(text)

for item in processed_test:
    print(item)