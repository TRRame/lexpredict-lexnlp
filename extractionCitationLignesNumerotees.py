import string
import lexnlp.extract.en.citations
import os
import csv
from pathlib import Path

#We ask the user the path to the file he wants to use.
file_path = Path(input("Enter the file path: ").strip())
file_name = input("Enter the file name with extension (.txt): ".strip())
file_full_path = file_path / file_name
case = open(file_full_path, 'r')

#This function process the given text to remove line break, tabulation, and non-breaking space.
def process_text(textToProcess):
    processed_text = []
    for line in textToProcess:
        
        unprocessed_line = line

        processed_line = unprocessed_line.replace("\n", "")
        processed_line = processed_line.replace("\t", " ")
        processed_line = processed_line.replace("\xa0", " ")

        processed_text.append(processed_line)
    return processed_text

processed_text = process_text(case)

#Return volume, reporter and page of citation, with which line it's extracted from in the text.
def get_result_with_line(text) :
    new_list = []
    i = 0
    for line in text :
        i = i+1
        line_result = lexnlp.extract.en.citations.get_citations(line)
        for item in line_result :
            result = (str(item[0]), item[1], str(item[3]))
            result = " ".join(result)
            new_list.append((i, result))
    return new_list

#We get the result using the get_result_with_line function and print it in the terminal.
citation_list = get_result_with_line(processed_text)
print(citation_list)

#We write the result in a csv file using another path given by the user
csv_file_path = Path(input("Enter the file path: ").strip())
csv_file_name = input("Enter the file name with extension (.csv): ".strip())
csv_file_full_path = csv_file_path / csv_file_name
with open(csv_file_full_path, "w", newline="") as file_writer:
    fields = ["Line", "Citation"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for citation in citation_list:
        writer.writerow({"Line": citation[0], "Citation": citation[1]})
