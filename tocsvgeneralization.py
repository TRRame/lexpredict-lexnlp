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

def get_results(func, text):
    citations_list = []
    for line in processed_text:
        citation_result = list(func(line))
        if citation_result != []:
            citations_list.append((citation_result, line))
    return citations_list

result_list = get_results(lexnlp.extract.en.definitions.get_definitions, processed_text)


#We write a csv file with the result we got from extraction.
with open("/home/tristan/Stage/EtudeLogiciels/EtudeLexNLP/Definitions_APFvBontaRobertsResults.csv", "w", newline="") as file_writer:
    fields = ["Definition", "Source"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for result in result_list:
        writer.writerow({"Definition":result[0], "Source":result[1]})

case1.close()