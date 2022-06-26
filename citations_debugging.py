#Import the extract modules we are interested in
import os
import lexnlp.extract.en.citations


case = open("/home/tristan/Stage/TextesJuridiques/AmericansForProsperityFoundationvBontaRoberts.txt")


text = case.read()
text = text.replace("\n", "")
text = text.replace("\t", " ")
text = text.replace("\xa0", " ")
case.close()
#TODO Generalize the file loading to all the text from a directory in a list


#We store the output from get_citations in a variable, and we print the list obtained line per line.
citations_list = (list(lexnlp.extract.en.citations.get_citations(text)))


for citations in citations_list:
    print(citations)