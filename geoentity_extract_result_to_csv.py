#For geoentities
import os
import csv
from unittest import result
from lexnlp.extract.en.dict_entities import DictionaryEntry
from lexnlp.extract.en.geoentities import get_geoentities, get_geoentity_annotations
import lexnlp.extract.en.geoentities
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

#Geoentities setup
#Need to use make_geoconfig to create a geo_config usable in get_geoentities
def make_geoconfig():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ge_path = dir_path + '/test_data/lexnlp/extract/en/tests/test_geoentities/'
    entities_fn = ge_path + 'geoentities.csv'
    aliases_fn = ge_path + 'geoaliases.csv'
    return list(DictionaryEntry.load_entities_from_files(entities_fn, aliases_fn))


GEO_CONFIG = make_geoconfig()

#We get all the geoentities in a list. The list is a list of tuple with the lexnlp function result and the part of the text where it comes from.
geoentity_list = []
for text in processed_text:
    geo_result = lexnlp.extract.en.geoentities.get_geoentities(text, GEO_CONFIG)
    for res in geo_result:
        g = (res, text)
        geoentity_list.append(g)


#We write the result in a csv file using another path given by the user
csv_file_path = Path(input("Enter the file path: ").strip())
csv_file_name = input("Enter the file name with extension (.csv): ".strip())
csv_file_full_path = csv_file_path / csv_file_name
with open(csv_file_full_path, "w", newline="") as file_writer:
    fields = ["Geoentity", "Source"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for result in geoentity_list:
        writer.writerow({"Geoentity":result[0], "Source":result[1]})

case1.close()