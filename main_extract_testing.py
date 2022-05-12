#Import the extract modules we are interested in
import os
import csv
from unittest import result
import lexnlp.extract.en.acts
import lexnlp.extract.en.citations
import lexnlp.extract.en.dates
import lexnlp.extract.en.copyright
import lexnlp.extract.en.geoentities
import lexnlp.extract.en.durations
import lexnlp.extract.en.distances
import lexnlp.extract.en.conditions
import lexnlp.extract.en.constraints
import lexnlp.extract.en.money
import lexnlp.extract.en.percents
import lexnlp.extract.en.ratios
import lexnlp.extract.en.regulations

#For company extracting
import lexnlp.extract.en.entities.nltk_maxent
#Load the wanted text from the corpus in a variable so it can be read later


#For geoentities
from lexnlp.extract.en.dict_entities import DictionaryEntry
from lexnlp.extract.en.geoentities import get_geoentities, get_geoentity_annotations


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

def display_result(results):
    for object in results:
        print(object)


#TODO Generalize the file loading to all the text from a directory in a list

#Printing all the results we get from the different extraction modules
acts_list = function_applyer(lexnlp.extract.en.acts.get_acts, texts)
display_result(acts_list)

'''
#We store the output from get_citations in a variable, and we print the list obtained line per line.
#citations_list = (lexnlp.extract.en.citations.get_citation_annotations(text))
citations_list  = function_applyer(lexnlp.extract.en.citations.get_citations, texts)


#Company extractor
company_list = function_applyer(lexnlp.extract.en.entities.nltk_maxent.get_companies, texts)


#Date extractor
date_list = function_applyer(lexnlp.extract.en.dates.get_dates, texts)


#Copyright extractor
copyright_list = function_applyer(lexnlp.extract.en.copyright.get_copyright, texts)



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
for text in texts:
    geoentity_list.append(lexnlp.extract.en.entities.nltk_maxent.get_companies(text, GEO_CONFIG))

for geoentity in geoentity_list:
    for object in geoentity:
        print(object)


#Duration setup
duration_list = function_applyer(lexnlp.extract.en.durations.get_durations, texts)

#Distances setup
distance_list = function_applyer(lexnlp.extract.en.distances.get_distances, texts)

#Conditions setup
conditions_list = function_applyer(lexnlp.extract.en.conditions.get_conditions, texts)


#Constraints setup
constraints_list = function_applyer(lexnlp.extract.en.constraints.get_constraints, texts)


#Currency and money setup
currency_list = function_applyer(lexnlp.extract.en.money.get_money, texts)

display_result(currency_list)

#Percentage setup
percentage_list = function_applyer(lexnlp.extract.en.percents.get_percents, texts)

display_result(percentage_list)

#Ratios setup
ratio_list = function_applyer(lexnlp.extract.en.ratios.get_ratios, texts)

display_result(ratio_list)

#Regulation setup
regulation_list = function_applyer(lexnlp.extract.en.regulations.get_regulations, texts)
display_result(regulation_list)
'''