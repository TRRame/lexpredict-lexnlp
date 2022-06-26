import pandas
import csv
import lexnlp.extract.en.courts
from lexnlp.extract.en.tests.test_courts import build_dictionary_entry

#We load the text and process it.
case1 = open("/home/tristan/Stage/TextesJuridiques/AMGCapitalManagementvFTCBreyer.txt", 'r')
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

court_df = pandas.read_csv("https://raw.githubusercontent.com/LexPredict/lexpredict-legal-dictionary/1.0.5/en/legal/us_courts.csv")
court_config_data = []

for _, row in court_df.iterrows():
    court_config_data.append(build_dictionary_entry(row))


result_list = []
for line in processed_text:
    for entity, alias in lexnlp.extract.en.courts.get_courts(line, court_config_data):
        c = ((entity, alias), line)
        result_list.append(c)

with open("/home/tristan/Stage/EtudeLogiciels/EtudeLexNLP/Courts_AMGvFTCBreyerResults.csv", "w", newline="") as file_writer:
    fields = ["Courts", "Source"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for result in result_list:
        writer.writerow({"Courts":result[0], "Source":result[1]})

case1.close()