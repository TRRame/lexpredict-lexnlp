import os
import csv
import lexnlp.extract.en.dates

#We load the three texts we are interested in, and we put them in a list of string using read() function
cases = []

case1 = open("/home/tristan/Stage/TextesJuridiques/AmericansForProsperityFoundationvBontaRoberts.txt", 'r')
cases.append(case1)
case2 = open("/home/tristan/Stage/TextesJuridiques/AMGCapitalManagementvFTCBreyer.txt", 'r')
cases.append(case2)
case3 = open("/home/tristan/Stage/TextesJuridiques/BordenvUnitedStatesKagan.txt", 'r')
cases.append(case3)

unprocessed_texts = []
texts = []

for case in cases:
    unprocessed_texts.append(case.read())

#We delete the tabulation and nextline from the text has it can cause some parsing problems
for text in unprocessed_texts:
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    text = text.replace("\xa0", "")
    texts.append(text)


def function_applyer(func, list: list):
    '''
    Apply the chosen function to each item of the list, and display the result.
    :param func: function we give as argument
    :param list: list of texts we want to analyse
    :return: list of extracted datas
    '''
    result_object_list = map(func, list)


    returned_result_list = []
    for object in result_object_list:
        for result in object:
            returned_result_list.append(result)
    
    return returned_result_list


date_list = function_applyer(lexnlp.extract.en.dates.get_dates, texts)

#We write a csv file with the result we got from extraction.
with open("/home/tristan/Stage/EtudeLogiciels/EtudeLexNLP/DatesResult.csv", "w", newline="") as file_writer:
    fields = ["Date"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for date in date_list:
        writer.writerow({"Date":date.isoformat()})