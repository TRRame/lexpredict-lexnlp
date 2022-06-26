#For nlp extract function
import os
import csv
from unittest import result
from lexnlp.extract.en.dict_entities import DictionaryEntry
from lexnlp.extract.en.geoentities import get_geoentities, get_geoentity_annotations
import lexnlp.extract.en.entities.nltk_maxent

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

geoentity_list = []
for text in processed_text:
    geo_result = lexnlp.extract.en.entities.nltk_maxent.get_persons(text)
    for res in geo_result:
        g = (res, text)
        geoentity_list.append(g)

#We write a csv file with the result we got from extraction.
with open("/home/tristan/Stage/EtudeLogiciels/EtudeLexNLP/NLP_Persons_APFvBontaRobertsResults.csv", "w", newline="") as file_writer:
    fields = ["Persons", "Source"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for result in geoentity_list:
        writer.writerow({"Persons":result[0], "Source":result[1]})

case1.close()
