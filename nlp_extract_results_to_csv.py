#For nlp extract function
import os
import csv
from unittest import result
from lexnlp.extract.en.dict_entities import DictionaryEntry
from lexnlp.extract.en.geoentities import get_geoentities, get_geoentity_annotations
import lexnlp.extract.en.entities.nltk_maxent
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

#We get the results from the lexnlp get_persons function in a list of tuple.
#You can use the get_companies function by changing "get_persons" by "get_companies"
geoentity_list = []
for text in processed_text:
    geo_result = lexnlp.extract.en.entities.nltk_maxent.get_persons(text)
    for res in geo_result:
        g = (res, text)
        geoentity_list.append(g)

#We write the result in a csv file using another path given by the user
csv_file_path = Path(input("Enter the file path: ").strip())
csv_file_name = input("Enter the file name with extension (.csv): ".strip())
csv_file_full_path = csv_file_path / csv_file_name
with open(csv_file_full_path, "w", newline="") as file_writer:
    fields = ["Persons", "Source"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for result in geoentity_list:
        writer.writerow({"Persons":result[0], "Source":result[1]})

case1.close()
