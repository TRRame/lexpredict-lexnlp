import os
import csv
import lexnlp.extract.en.acts
import lexnlp.extract.en.citations
import lexnlp.extract.en.dates
import lexnlp.extract.en.copyright
import lexnlp.extract.en.durations
import lexnlp.extract.en.distances
import lexnlp.extract.en.conditions
import lexnlp.extract.en.constraints
import lexnlp.extract.en.money
import lexnlp.extract.en.percents
import lexnlp.extract.en.ratios
import lexnlp.extract.en.regulations
import lexnlp.extract.en.definitions
from pathlib import Path

#We ask the user the path to the file he wants to use.
file_path = Path(input("Enter the file path: ").strip())
file_name = input("Enter the file name with extension (.txt): ".strip())
file_full_path = file_path / file_name
case1 = open(file_full_path, 'r')

#This function process the given text to remove line break, tabulation, and non-breaking space.
def process_text(textToProcess):
    processed_text = []
    for line in case1:
        
        unprocessed_line = line

        processed_line = unprocessed_line.replace("\n", "")
        processed_line = processed_line.replace("\t", " ")
        processed_line = processed_line.replace("\xa0", " ")

        processed_text.append(processed_line)
    return processed_text

processed_text = process_text(case1)

#This function take a lexnlp method and the text we want to use it on, and give the results in a list of tuples.
#The tuple is made of the result of the function for a part of the text, and the path of the text where the results comes from.
def get_results(func, text):
    citations_list = []
    for line in processed_text:
        citation_result = list(func(line))
        if citation_result != []:
            citations_list.append((citation_result, line))
    return citations_list

result_list = get_results(lexnlp.extract.en.definitions.get_definitions, processed_text)


#We write the result in a csv file using another path given by the user
csv_file_path = Path(input("Enter the file path: ").strip())
csv_file_name = input("Enter the file name with extension (.csv): ".strip())
csv_file_full_path = csv_file_path / csv_file_name
with open(csv_file_full_path, "w", newline="") as file_writer:
    fields = ["Definition", "Source"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for result in result_list:
        writer.writerow({"Definition":result[0], "Source":result[1]})

case1.close()