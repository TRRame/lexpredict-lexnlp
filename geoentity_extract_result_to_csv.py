#For geoentities
import os
import csv
from unittest import result
from lexnlp.extract.en.dict_entities import DictionaryEntry
from lexnlp.extract.en.geoentities import get_geoentities, get_geoentity_annotations
import lexnlp.extract.en.geoentities

#We load the text and process it.
case1 = open("/home/tristan/Stage/TextesJuridiques/AmericansForProsperityFoundationvBontaRoberts.txt", 'r')
print(type(case1))

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

geoentity_list = []
for text in processed_text:
    geo_result = lexnlp.extract.en.geoentities.get_geoentities(text, GEO_CONFIG)
    for res in geo_result:
        g = (res, text)
        geoentity_list.append(g)

#We write a csv file with the result we got from extraction.
with open("/home/tristan/Stage/EtudeLogiciels/EtudeLexNLP/Geoentity_APFvBontaRobertsResults.csv", "w", newline="") as file_writer:
    fields = ["Geoentity", "Source"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for result in geoentity_list:
        writer.writerow({"Geoentity":result[0], "Source":result[1]})

case1.close()