import pandas
import csv
import lexnlp.extract.en.courts
from lexnlp.extract.en.tests.test_courts import build_dictionary_entry
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

#The chosen text is processed.
processed_text = process_text(case1)


#Configuration of pandas dataframe
court_df = pandas.read_csv("https://raw.githubusercontent.com/LexPredict/lexpredict-legal-dictionary/1.0.5/en/legal/us_courts.csv")
court_config_data = []

for _, row in court_df.iterrows():
    court_config_data.append(build_dictionary_entry(row))


#We get the result from the text in a list
result_list = []
for line in processed_text:
    for entity, alias in lexnlp.extract.en.courts.get_courts(line, court_config_data):
        c = ((entity, alias), line)
        result_list.append(c)

#We write the result in a csv file using another path given by the user
csv_file_path = Path(input("Enter the file path: ").strip())
csv_file_name = input("Enter the file name with extension (.csv): ".strip())
csv_file_full_path = csv_file_path / csv_file_name
with open(csv_file_full_path, "w", newline="") as file_writer:
    fields = ["Courts", "Source"]

    writer=csv.DictWriter(file_writer, fieldnames=fields)

    writer.writeheader()

    for result in result_list:
        writer.writerow({"Courts":result[0], "Source":result[1]})

case1.close()